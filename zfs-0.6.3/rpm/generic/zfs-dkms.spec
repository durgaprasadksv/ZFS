%{?!packager: %define packager Brian Behlendorf <behlendorf1@llnl.gov>}

%define module  zfs
%define mkconf  scripts/dkms.mkconf

Name:           %{module}-dkms

Version:        0.6.3
Release:        1%{?dist}
Summary:        Kernel module(s) (dkms)

Group:          System Environment/Kernel
License:        CDDL
URL:            http://zfsonlinux.org/
Source0:        %{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       dkms >= 2.2.0.3-20
Requires:       spl-dkms = %{version}
Requires:       gcc, make, perl
Requires:       kernel-devel
Provides:       %{module}-kmod = %{version}

%description
This package contains the dkms ZFS kernel modules.

%prep
%setup -q -n %{module}-%{version}

%build
%{mkconf} -n %{module} -v %{version} -f dkms.conf

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/usr/src/
cp -rf ${RPM_BUILD_DIR}/%{module}-%{version} $RPM_BUILD_ROOT/usr/src/

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    rm -rf $RPM_BUILD_ROOT
fi

%files
%defattr(-,root,root)
/usr/src/%{module}-%{version}

%post
for POSTINST in /usr/lib/dkms/common.postinst; do
    if [ -f $POSTINST ]; then
        $POSTINST %{module} %{version}
        exit $?
    fi
    echo "WARNING: $POSTINST does not exist."
done
echo -e "ERROR: DKMS version is too old and %{module} was not"
echo -e "built with legacy DKMS support."
echo -e "You must either rebuild %{module} with legacy postinst"
echo -e "support or upgrade DKMS to a more current version."
exit 1

%preun
# Only remove the modules if they are for this %{version}-%{release}.  A
# package upgrade can replace them if only the %{release} is changed.
RELEASE="/var/lib/dkms/%{module}/%{version}/build/%{module}.release"
if [ -f $RELEASE ] && [ `cat $RELEASE`%{?dist} = "%{version}-%{release}" ]; then
    echo -e
    echo -e "Uninstall of %{module} module (version %{version}) beginning:"
    dkms remove -m %{module} -v %{version} --all --rpm_safe_upgrade
fi
exit 0

%changelog
* %(date "+%a %b %d %Y") %packager %{version}-%{release}
- Automatic build by DKMS
