sudo zpool destroy tank

sudo dpkg -r kmod-spl-3.2.0-56-generic kmod-spl-devel kmod-spl-devel-3.2.0-56-generic spl

sudo dpkg --purge kmod-spl-3.2.0-56-generic kmod-spl-devel kmod-spl-devel-3.2.0-56-generic spl

sudo dpkg -r kmod-zfs-3.2.0-56-generic kmod-zfs-devel kmod-zfs-devel-3.2.0-56-generic libzfs2 libzfs2-devel zfs zfs-dracut zfs-test libuutil1 libzpool2 libnvpair1

sudo dpkg --purge kmod-zfs-3.2.0-56-generic kmod-zfs-devel kmod-zfs-devel-3.2.0-56-generic libzfs2 libzfs2-devel zfs zfs-dracut zfs-test libuutil1 libzpool2 libnvpair1

sudo rmmod zpios zfs zcommon zunicode znvpair zavl

sudo rmmod splat spl
