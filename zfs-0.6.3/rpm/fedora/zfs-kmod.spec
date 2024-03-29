%define module  zfs

%if !%{defined ksrc}
%if 0%{?rhel}%{?fedora}
%define ksrc    ${kernel_version##*___}
%else
%define ksrc    "$( \
        if [ -e "/usr/src/linux-${kernel_version%%___*}" ]; then \
            echo "/usr/src/linux-${kernel_version%%___*}"; \
        elif [ -e "/lib/modules/${kernel_version%%___*}/source" ]; then \
            echo "/lib/modules/${kernel_version%%___*}/source"; \
        else \
            echo "/lib/modules/${kernel_version%%___*}/build"; \
        fi)"
%endif
%endif

%if !%{defined kobj}
%if 0%{?rhel}%{?fedora}
%define kobj    ${kernel_version##*___}
%else
%define kobj    "$( \
        if [ -e "/usr/src/linux-${kernel_version%%___*}" ]; then \
            echo "/usr/src/linux-${kernel_version%%___*}"; \
        else \
            echo "/lib/modules/${kernel_version%%___*}/build"; \
        fi)"
%endif
%endif

#define repo    rpmfusion
#define repo    chaos

# (un)define the next line to either build for the newest or all current kernels
%define buildforkernels newest
#define buildforkernels current
#define buildforkernels akmod

%bcond_with     debug
%bcond_with     debug_dmu_tx


Name:           %{module}-kmod

Version:        0.6.3
Release:        1%{?dist}
Summary:        Kernel module(s)

Group:          System Environment/Kernel
License:        CDDL
URL:            http://zfsonlinux.org/
Source0:        %{module}-%{version}.tar.gz
Source10:       kmodtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id} -u -n)

# The developments headers will conflict with the dkms packages.
Conflicts:      %{module}-dkms

%if %{defined repo}

# Building for a repository use the proper build-sysbuild package
# to determine which kernel-devel packages should be installed.
BuildRequires:  %{_bindir}/kmodtool
%{!?kernels:BuildRequires: buildsys-build-%{repo}-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu}}

%else

# Building local packages attempt to to use the installed kernel.
%{?rhel:BuildRequires: kernel-devel}
%{?fedora:BuildRequires: kernel-devel}
%{?suse_version:BuildRequires: kernel-source}

%if !%{defined kernels} && !%{defined build_src_rpm}
    %if 0%{?rhel}%{?fedora}%{?suse_version}
        %define kernels %(ls -1 /usr/src/kernels)
    %else
        %define kernels %(ls -1 /lib/modules)
    %endif
%endif
%endif

%if 0%{?rhel}%{?fedora}%{?suse_version}
BuildRequires:             kmod-spl-devel = %{version}
%global KmodsRequires      kmod-spl
%global KmodsDevelRequires kmod-spl-devel
%global KmodsMetaRequires  spl-kmod
%endif

%if 0%{?fedora} >= 17
%define prefix  /usr
%endif

# Kmodtool does its magic here.  A patched version of kmodtool is shipped
# with the source rpm until kmod development packages are supported upstream.
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=2714
%{expand:%(bash %{SOURCE10} --target %{_target_cpu} %{?repo:--repo %{?repo}} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} --devel %{?prefix:--prefix "%{?prefix}"} %{?kernels:--for-kernels "%{?kernels}"} %{?kernelbuildroot:--buildroot "%{?kernelbuildroot}"} 2>/dev/null) }


%description
This package contains the ZFS kernel modules.

%prep
# Error out if there was something wrong with kmodtool.
%{?kmodtool_check}

# Print kmodtool output for debugging purposes:
bash %{SOURCE10}  --target %{_target_cpu} %{?repo:--repo %{?repo}} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} --devel %{?prefix:--prefix "%{?prefix}"} %{?kernels:--for-kernels "%{?kernels}"} %{?kernelbuildroot:--buildroot "%{?kernelbuildroot}"} 2>/dev/null

%if %{with debug}
    %define debug --enable-debug
%else
    %define debug --disable-debug
%endif

%if %{with debug_dmu_tx}
    %define debug_dmu_tx --enable-debug-dmu-tx
%else
    %define debug_dmu_tx --disable-debug-dmu-tx
%endif

#
# Allow the overriding of spl locations
#
%if %{defined require_splver}
%define splver %{require_splver}
%else
%define splver %{version}
%endif

%if %{defined require_spldir}
%define spldir %{require_spldir}
%else
%define spldir %{_usrsrc}/spl-%{splver}
%endif

%if %{defined require_splobj}
%define splobj %{require_splobj}
%else
%define splobj %{spldir}/${kernel_version%%___*}
%endif


# Leverage VPATH from configure to avoid making multiple copies.
%define _configure ../%{module}-%{version}/configure

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions}; do
    %{__mkdir} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    cd _kmod_build_${kernel_version%%___*}
    %configure \
        --with-config=kernel \
        --with-linux=%{ksrc} \
        --with-linux-obj=%{kobj} \
        --with-spl="%{spldir}" \
        --with-spl-obj="%{splobj}" \
        %{debug} \
        %{debug_dmu_tx}
    make %{?_smp_mflags}
    cd ..
done


%install
rm -rf ${RPM_BUILD_ROOT}

# Relies on the kernel 'modules_install' make target.
for kernel_version in %{?kernel_versions}; do
    cd _kmod_build_${kernel_version%%___*}
    make install \
        DESTDIR=${RPM_BUILD_ROOT} \
        %{?prefix:INSTALL_MOD_PATH=%{?prefix}} \
        INSTALL_MOD_DIR=%{kmodinstdir_postfix}
    cd ..
done
chmod u+x ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/*/extra/*/*/*
%{?akmod_install}


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jun 12 2014 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.3-1
- Released 0.6.3-1
* Wed Aug 21 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.2-1
- Released 0.6.2-1
* Fri Mar 22 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.1-1
- First official stable release.
