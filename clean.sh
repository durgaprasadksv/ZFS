sudo zpool destroy tank
sudo dpkg -r kmod-zfs-3.13.0-45-generic kmod-zfs-devel kmod-zfs-devel-3.13.0-45-generic libzfs2 libzfs2-devel zfs zfs-dracut zfs-test libuutil1 libzpool2 libnvpair1
sudo dpkg --purge kmod-zfs-3.13.0-45-generic kmod-zfs-devel kmod-zfs-devel-3.13.0-45-generic libzfs2 libzfs2-devel zfs zfs-dracut zfs-test libuutil1 libzpool2 libnvpair1
sudo rmmod zpios zfs zcommon zunicode znvpair zavl
