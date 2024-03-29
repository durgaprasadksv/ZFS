%global _sbindir    /sbin
%global _libdir     /%{_lib}

# Set the default udev directory based on distribution.
%if %{undefined _udevdir}
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7 || 0%{?centos} >= 7
%global _udevdir    %{_prefix}/lib/udev
%else
%global _udevdir    /lib/udev
%endif
%endif

# Set the default udevrule directory based on distribution.
%if %{undefined _udevruledir}
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7 || 0%{?centos} >= 7
%global _udevruledir    %{_prefix}/lib/udev/rules.d
%else
%global _udevruledir    /lib/udev/rules.d
%endif
%endif

# Set the default dracut directory based on distribution.
%if %{undefined _dracutdir}
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7 || 0%{?centos} >= 7
%global _dracutdir  %{_prefix}/lib/dracut
%else
%global _dracutdir  %{_prefix}/share/dracut
%endif
%endif

%bcond_with    debug
%bcond_with    blkid
%bcond_with    systemd

# Generic enable switch for systemd
%if %{with systemd}
%define _systemd 1
%endif

# RHEL >= 7 comes with systemd
%if 0%{?rhel} >= 7
%define _systemd 1
%endif

# Fedora >= 15 comes with systemd, but only >= 18 has
# the proper macros
%if 0%{?fedora} >= 18
%define _systemd 1
%endif

# opensuse >= 12.1 comes with systemd, but only >= 13.1
# has the proper macros
%if 0%{?suse_version} >= 1310
%define _systemd 1
%endif

Name:           zfs
Version:        0.6.3
Release:        1%{?dist}
Summary:        Commands to control the kernel modules and libraries

Group:          System Environment/Kernel
License:        CDDL
URL:            http://zfsonlinux.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  i386 i686 x86_64

# May build but untested on ppc/ppc64
ExcludeArch:    ppc ppc64

Requires:       spl = %{version}
Requires:       libzpool2 = %{version}
Requires:       libnvpair1 = %{version}
Requires:       libuutil1 = %{version}
Requires:       libzfs2 = %{version}
Requires:       %{name}-kmod = %{version}
Provides:       %{name}-kmod-common = %{version}

# zfs-fuse provides the same commands and man pages that ZoL does. Renaming
# those on either side would conflict with all available documentation.
Conflicts:      zfs-fuse

%if 0%{?rhel}%{?fedora}%{?suse_version}
BuildRequires:  zlib-devel
BuildRequires:  libuuid-devel
%if %{with blkid}
BuildRequires:  libblkid-devel
%endif
%endif
%if 0%{?_systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
%endif

%description
This package contains the ZFS command line utilities.

%package -n libzpool2
Summary:        Native ZFS pool library for Linux
Group:          System Environment/Kernel

%description -n libzpool2
This package contains the zpool library, which provides support
for managing zpools

%post-n libzpool2 -p /sbin/ldconfig
%postun -n libzpool2 -p /sbin/ldconfig

%package -n libnvpair1
Summary:        Solaris name-value library for Linux
Group:          System Environment/Kernel

%description -n libnvpair1
This package contains routines for packing and unpacking name-value
pairs.  This functionality is used to portably transport data across
process boundaries, between kernel and user space, and can be used
to write self describing data structures on disk.

%post-n libnvpair1 -p /sbin/ldconfig
%postun -n libnvpair1 -p /sbin/ldconfig

%package -n libuutil1
Summary:        Solaris userland utility library for Linux
Group:          System Environment/Kernel

%description -n libuutil1
This library provides a variety of compatibility functions for ZFS on Linux:
 * libspl: The Solaris Porting Layer userland library, which provides APIs
   that make it possible to run Solaris user code in a Linux environment
   with relatively minimal modification.
 * libavl: The Adelson-Velskii Landis balanced binary tree manipulation
   library.
 * libefi: The Extensible Firmware Interface library for GUID disk
   partitioning.
 * libshare: NFS, SMB, and iSCSI service integration for ZFS.

%post-n libuutil1 -p /sbin/ldconfig
%postun -n libuutil1 -p /sbin/ldconfig

%package -n libzfs2
Summary:        Native ZFS filesystem library for Linux
Group:          System Environment/Kernel

%description -n libzfs2
This package provides support for managing ZFS filesystems

%post-n libzfs2 -p /sbin/ldconfig
%postun -n libzfs2 -p /sbin/ldconfig

%package -n libzfs2-devel
Summary:        Development headers
Group:          System Environment/Kernel
Requires:       libzfs2 = %{version}
Requires:       libzpool2 = %{version}
Requires:       libnvpair1 = %{version}
Requires:       libuutil1 = %{version}
Provides:       libzpool2-devel
Provides:       libnvpair1-devel
Provides:       libuutil1-devel
Obsoletes:      zfs-devel

%description -n libzfs2-devel
This package contains the header files needed for building additional
applications against the ZFS libraries.

%package test
Summary:        Test infrastructure
Group:          System Environment/Kernel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       parted
Requires:       lsscsi
Requires:       mdadm
Requires:       bc

%description test
This package contains test infrastructure and support scripts for
validating the file system.

%package dracut
Summary:        Dracut module
Group:          System Environment/Kernel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dracut

%description dracut
This package contains a dracut module used to construct an initramfs
image which is ZFS aware.

%prep
%if %{with debug}
    %define debug --enable-debug
%else
    %define debug --disable-debug
%endif
%if %{with blkid}
    %define blkid --with-blkid
%else
    %define blkid --without-blkid
%endif
%if 0%{?_systemd}
    %define systemd --enable-systemd --with-systemdunitdir=%{_unitdir} --with-systemdpresetdir=%{_presetdir} --disable-sysvinit
%else
    %define systemd --enable-sysvinit --disable-systemd
%endif

%setup -q

%build
%configure \
    --with-config=user \
    --with-udevdir=%{_udevdir} \
    --with-udevruledir=%{_udevruledir} \
    --with-dracutdir=%{_dracutdir} \
    --disable-static \
    %{debug} \
    %{blkid} \
    %{systemd}
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=%{?buildroot}
find %{?buildroot}%{_libdir} -name '*.la' -exec rm -f {} \;

%post
%if 0%{?_systemd}
%systemd_post zfs.target
%else
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add zfs
%endif
exit 0

%preun
%if 0%{?_systemd}
%systemd_preun zfs.target
%else
if [ $1 -eq 0 ] ; then
    [ -x /sbin/chkconfig ] && /sbin/chkconfig --del zfs
fi
%endif
exit 0

%postun
%if 0%{?_systemd}
%systemd_postun zfs.target
%endif

%files
%{_sbindir}/*
%{_bindir}/*
%{_libexecdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_udevdir}/vdev_id
%{_udevdir}/zvol_id
%{_udevdir}/rules.d/*
%config(noreplace) %{_sysconfdir}/%{name}
%if 0%{?_systemd}
/usr/lib/modules-load.d/*
%{_unitdir}/*
%{_presetdir}/*
%else
%{_sysconfdir}/init.d/*
%endif

%files -n libzpool2
%{_libdir}/libzpool.so.*

%files -n libnvpair1
%{_libdir}/libnvpair.so.*

%files -n libuutil1
%{_libdir}/libuutil.so.*

%files -n libzfs2
%{_libdir}/libzfs*.so.*

%files -n libzfs2-devel
%{_libdir}/*.so
%{_includedir}/*
%doc AUTHORS COPYRIGHT DISCLAIMER
%doc OPENSOLARIS.LICENSE README.markdown

%files test
%{_datadir}/%{name}

%files dracut
%doc dracut/README.dracut.markdown
%{_dracutdir}/modules.d/*

%changelog
* Thu Jun 12 2014 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.3-1
- Released 0.6.3-1
* Wed Aug 21 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.2-1
- Released 0.6.2-1
* Fri Mar 22 2013 Brian Behlendorf <behlendorf1@llnl.gov> - 0.6.1-1
- First official stable release.
