Name:           spl
Version:        0.6.3
Release:        1%{?dist}
Summary:        Commands to control the kernel modules

Group:          System Environment/Kernel
License:        GPLv2+
URL:            http://zfsonlinux.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  i386 i686 x86_64

# May build but untested on ppc/ppc64
ExcludeArch:    ppc ppc64

Requires:       %{name}-kmod = %{version}
Provides:       %{name}-kmod-common = %{version}

%description
This package contains the commands to verify the SPL
kernel modules are functioning properly.

%prep
%setup -q

%build
%configure --with-config=user
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=%{?buildroot}

%files
%doc AUTHORS COPYING DISCLAIMER
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Thu Jun 12 2014 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.3-1
- Released 0.6.3-1
* Wed Aug 21 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.2-1
- Released 0.6.2-1
* Fri Mar 22 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.1-1
- First official stable release.
