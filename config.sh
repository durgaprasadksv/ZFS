sudo dpkg -i ./spl-0.6.3/*deb
sudo dpkg -i ./zfs-0.6.3/*deb

sudo insmod /lib/modules/3.2.0-56-generic/kernel/lib/zlib_deflate/zlib_deflate.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/spl/spl/spl.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/spl/splat/splat.ko

sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/avl/zavl.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/nvpair/znvpair.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/unicode/zunicode.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/zcommon/zcommon.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/zfs/zfs.ko
sudo insmod /lib/modules/3.2.0-56-generic/extra/zfs/zpios/zpios.ko

sudo chmod a+rw /dev/zfs
sudo zpool create -f tank /dev/sdb
sudo chmod a+rwx /tank
zfs set dedup=on tank
