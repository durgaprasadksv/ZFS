%define module  spl
#define repo    rpmfusion
#define repo    chaos

# (un)define the next line to either build for the newest or all current kernels
%define buildforkernels newest
#define buildforkernels current
#define buildforkernels akmod

%bcond_with     debug
%bcond_with     debug_log
%bcond_with     debug_kmem
%bcond_with     debug_kmem_tracking
%bcond_with     atomic_spinlocks


Name:           %{module}-kmod

Version:        0.6.3
Release:        1%{?dist}
Summary:        Kernel module(s)

Group:          System Environment/Kernel
License:        GPLv2+
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

%if 0%{?fedora} >= 17
%define prefix  /usr
%endif

# Kmodtool does its magic here.  A patched version of kmodtool is shipped
# because the latest versions may not be available for your distribution.
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=2714
%{expand:%(bash %{SOURCE10} --target %{_target_cpu} %{?repo:--repo %{?repo}} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} --devel %{?prefix:--prefix "%{?prefix}"} %{?kernels:--for-kernels "%{?kernels}"} %{?kernelbuildroot:--buildroot "%{?kernelbuildroot}"} 2>/dev/null) }


%description
This package contains the kernel modules required to emulate
several interfaces provided by the Solaris kernel.

%prep
# Error out if there was something wrong with kmodtool.
%{?kmodtool_check}

# Print kmodtool output for debugging purposes:
bash %{SOURCE10} --target %{_target_cpu} %{?repo:--repo %{?repo}}  --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} --devel  %{?prefix:--prefix "%{?prefix}"} %{?kernels:--for-kernels "%{?kernels}"} %{?kernelbuildroot:--buildroot "%{?kernelbuildroot}"} 2>/dev/null

%if %{with debug}
    %define debug --enable-debug
%else
    %define debug --disable-debug
%endif

%if %{with debug_log}
    %define debug_log --enable-debug-log
%else
    %define debug_log --disable-debug-log
%endif

%if %{with debug_kmem}
    %define debug_kmem --enable-debug-kmem
%else
    %define debug_kmem --disable-debug-kmem
%endif

%if %{with debug_kmem_tracking}
    %define debug_kmem_tracking --enable-debug-kmem-tracking
%else
    %define debug_kmem_tracking --disable-debug-kmem-tracking
%endif

%if %{with atomic_spinlocks}
    %define atomic_spinlocks --enable-atomic-spinlocks
%else
    %define atomic_spinlocks --disable-atomic-spinlocks
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
%if 0%{?rhel}%{?fedora}
        --with-linux="${kernel_version##*___}" \
        --with-linux-obj="${kernel_version##*___}" \
%else
        --with-linux="$( \
        if [ -e "/lib/modules/${kernel_version%%___*}/source" ]; then \
            echo "/lib/modules/${kernel_version%%___*}/source"; \
        else \
            echo "/lib/modules/${kernel_version%%___*}/build"; \
        fi)" \
        --with-linux-obj="/lib/modules/${kernel_version%%___*}/build" \
%endif
        %{debug} \
        %{debug_log} \
        %{debug_kmem} \
        %{debug_kmem_tracking} \
        %{atomic_spinlocks}
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
