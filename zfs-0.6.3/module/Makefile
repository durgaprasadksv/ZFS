subdir-m += avl
subdir-m += nvpair
subdir-m += unicode
subdir-m += zcommon
subdir-m += zfs
subdir-m += zpios

INSTALL_MOD_DIR ?= extra

ZFS_MODULE_CFLAGS += -include /usr/src/spl-0.6.3/3.13.0-45-generic/spl_config.h
ZFS_MODULE_CFLAGS += -include /home/ubuntu/zfs/ZFS/zfs-0.6.3/zfs_config.h
ZFS_MODULE_CFLAGS += -I/home/ubuntu/zfs/ZFS/zfs-0.6.3/include -I/usr/src/spl-0.6.3/include -I/usr/src/spl-0.6.3
export ZFS_MODULE_CFLAGS

modules:
	@# Make the exported SPL symbols available to these modules.
	@# They may be in the root of SPL_OBJ when building against
	@# installed devel headers, or they may be in the module
	@# subdirectory when building against the spl source tree.
	@if [ -f /usr/src/spl-0.6.3/3.13.0-45-generic/Module.symvers ]; then \
		/bin/cp /usr/src/spl-0.6.3/3.13.0-45-generic/Module.symvers .; \
	elif [ -f /usr/src/spl-0.6.3/3.13.0-45-generic/module/Module.symvers ]; then \
		/bin/cp /usr/src/spl-0.6.3/3.13.0-45-generic/module/Module.symvers .; \
	else \
		echo -e "\n" \
		"*** Missing spl symbols ensure you have built the spl:\n" \
		"*** - /usr/src/spl-0.6.3/3.13.0-45-generic/Module.symvers, or\n" \
		"*** - /usr/src/spl-0.6.3/3.13.0-45-generic/module/Module.symvers\n"; \
		exit 1; \
	fi
	$(MAKE) -C /usr/src/linux-headers-3.13.0-45-generic SUBDIRS=`pwd`  CONFIG_ZFS=m $@

clean:
	@# Only cleanup the kernel build directories when CONFIG_KERNEL
	@# is defined.  This indicates that kernel modules should be built.
	$(MAKE) -C /usr/src/linux-headers-3.13.0-45-generic SUBDIRS=`pwd`  $@

	if [ -f Module.symvers ]; then $(RM) Module.symvers; fi
	if [ -f Module.symvers ]; then $(RM) Module.symvers; fi
	if [ -f Module.markers ]; then $(RM) Module.markers; fi

modules_install:
	@# Install the kernel modules
	$(MAKE) -C /usr/src/linux-headers-3.13.0-45-generic SUBDIRS=`pwd` $@ \
		INSTALL_MOD_PATH=$(DESTDIR)$(INSTALL_MOD_PATH) \
		INSTALL_MOD_DIR=$(INSTALL_MOD_DIR)
	@# Remove extraneous build products when packaging
	kmoddir=$(DESTDIR)$(INSTALL_MOD_PATH)/lib/modules/3.13.0-45-generic; \
	if [ -n $$kmoddir ]; then \
		find $$kmoddir -name 'modules.*' | xargs $(RM); \
	fi
	sysmap=$(DESTDIR)$(INSTALL_MOD_PATH)/boot/System.map-3.13.0-45-generic; \
	if [ -f $$sysmap ]; then \
		depmod -ae -F $$sysmap 3.13.0-45-generic; \
	fi

modules_uninstall:
	@# Uninstall the kernel modules
	kmoddir=$(DESTDIR)$(INSTALL_MOD_PATH)/lib/modules/3.13.0-45-generic
	list='$(subdir-m)'; for subdir in $$list; do \
		$(RM) -R $$kmoddir/$(INSTALL_MOD_DIR)/$$subdir; \
	done

distdir:

distclean maintainer-clean: clean
install: modules_install
uninstall: modules_uninstall
all: modules
check:
