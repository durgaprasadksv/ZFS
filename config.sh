sudo dpkg -i /home/ubuntu/zfs/ZFS/spl-0.6.3/*deb
sudo dpkg -i /home/ubuntu/zfs/ZFS/zfs-0.6.3/*deb

sudo insmod /lib/modules/3.13.0-46-generic/extra/spl/spl/spl.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/spl/splat/splat.ko

sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/avl/zavl.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/nvpair/znvpair.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/unicode/zunicode.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/zcommon/zcommon.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/zfs/zfs.ko
sudo insmod /lib/modules/3.13.0-46-generic/extra/zfs/zpios/zpios.ko

sudo chmod a+rw /dev/zfs
sudo zpool create -f tank /dev/vdb
sudo chmod a+rwx /tank
