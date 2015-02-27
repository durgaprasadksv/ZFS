sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/avl/zavl.ko
sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/nvpair/znvpair.ko
sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/unicode/zunicode.ko
sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/zcommon/zcommon.ko
sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/zfs/zfs.ko
sudo insmod /lib/modules/3.13.0-45-generic/extra/zfs/zpios/zpios.ko

sudo chmod a+rw /dev/zfs
