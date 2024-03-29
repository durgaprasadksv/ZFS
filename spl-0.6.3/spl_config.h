/* spl_config.h.  Generated from spl_config.h.in by configure.  */
/* spl_config.h.in.  Generated from configure.ac by autoheader.  */

/* Atomic types use spinlocks */
/* #undef ATOMIC_SPINLOCK */

/* Define to 1 to enable basic kmem accounting */
#define DEBUG_KMEM 1

/* Define to 1 to enable detailed kmem tracking */
/* #undef DEBUG_KMEM_TRACKING */

/* Define to 1 to enable basic debug logging */
#define DEBUG_LOG 1

/* new shrinker callback wants 2 args */
#define HAVE_2ARGS_NEW_SHRINKER_CALLBACK 1

/* old shrinker callback wants 2 args */
/* #undef HAVE_2ARGS_OLD_SHRINKER_CALLBACK */

/* register_sysctl_table() wants 2 args */
/* #undef HAVE_2ARGS_REGISTER_SYSCTL */

/* vfs_fsync() wants 2 args */
#define HAVE_2ARGS_VFS_FSYNC 1

/* vfs_getattr wants 2 args */
/* #undef HAVE_2ARGS_VFS_GETATTR */

/* vfs_unlink() wants 2 args */
#define HAVE_2ARGS_VFS_UNLINK 1

/* zlib_deflate_workspacesize() wants 2 args */
#define HAVE_2ARGS_ZLIB_DEFLATE_WORKSPACESIZE 1

/* on_each_cpu wants 3 args */
#define HAVE_3ARGS_ON_EACH_CPU 1

/* old shrinker callback wants 3 args */
/* #undef HAVE_3ARGS_SHRINKER_CALLBACK */

/* vfs_unlink() wants 3 args */
/* #undef HAVE_3ARGS_VFS_UNLINK */

/* vfs_rename() wants 4 args */
#define HAVE_4ARGS_VFS_RENAME 1

/* device_create wants 5 args */
#define HAVE_5ARGS_DEVICE_CREATE 1

/* proc_handler() wants 5 args */
#define HAVE_5ARGS_PROC_HANDLER 1

/* vfs_rename() wants 5 args */
/* #undef HAVE_5ARGS_VFS_RENAME */

/* vfs_rename() wants 6 args */
/* #undef HAVE_6ARGS_VFS_RENAME */

/* kernel defines atomic64_cmpxchg */
#define HAVE_ATOMIC64_CMPXCHG 1

/* kernel defines atomic64_t */
#define HAVE_ATOMIC64_T 1

/* kernel defines atomic64_xchg */
#define HAVE_ATOMIC64_XCHG 1

/* class_device_create() is available */
/* #undef HAVE_CLASS_DEVICE_CREATE */

/* struct cred exists */
#define HAVE_CRED_STRUCT 1

/* struct ctl_table has ctl_name */
/* #undef HAVE_CTL_NAME */

/* unnumbered sysctl support exists */
/* #undef HAVE_CTL_UNNUMBERED */

/* device_create() is available */
#define HAVE_DEVICE_CREATE 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* fops->fallocate() exists */
#define HAVE_FILE_FALLOCATE 1

/* first_online_pgdat() is available */
/* #undef HAVE_FIRST_ONLINE_PGDAT */

/* fls64() is available */
#define HAVE_FLS64 1

/* struct fs_struct uses spinlock_t */
#define HAVE_FS_STRUCT_SPINLOCK 1

/* get_vmalloc_info() is available */
/* #undef HAVE_GET_VMALLOC_INFO */

/* get_zone_counts() is available */
/* #undef HAVE_GET_ZONE_COUNTS */

/* global_page_state() is available */
#define HAVE_GLOBAL_PAGE_STATE 1

/* groups_search() is available */
/* #undef HAVE_GROUPS_SEARCH */

/* init_utsname() is available */
#define HAVE_INIT_UTSNAME 1

/* fops->fallocate() exists */
/* #undef HAVE_INODE_FALLOCATE */

/* struct inode has i_mutex */
#define HAVE_INODE_I_MUTEX 1

/* truncate_range() inode operation is available */
#define HAVE_INODE_TRUNCATE_RANGE 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* kallsyms_lookup_name() is available */
#define HAVE_KALLSYMS_LOOKUP_NAME 1

/* kern_path_locked() is available */
/* #undef HAVE_KERN_PATH_LOCKED */

/* kern_path_parent() is available */
#define HAVE_KERN_PATH_PARENT_HEADER 1

/* kern_path_parent() is available */
/* #undef HAVE_KERN_PATH_PARENT_SYMBOL */

/* kmalloc_node() is available */
#define HAVE_KMALLOC_NODE 1

/* struct kmem_cache has allocflags */
#define HAVE_KMEM_CACHE_ALLOCFLAGS 1

/* struct kmem_cache has gfpflags */
/* #undef HAVE_KMEM_CACHE_GFPFLAGS */

/* kuid_t/kgid_t in use */
/* #undef HAVE_KUIDGID_T */

/* kvasprintf() is available */
#define HAVE_KVASPRINTF 1

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* monotonic_clock() is available */
/* #undef HAVE_MONOTONIC_CLOCK */

/* mutex_lock_nested() is available */
#define HAVE_MUTEX_LOCK_NESTED 1

/* struct mutex has owner */
#define HAVE_MUTEX_OWNER 1

/* struct mutex owner is a task_struct */
#define HAVE_MUTEX_OWNER_TASK_STRUCT 1

/* next_online_pgdat() is available */
/* #undef HAVE_NEXT_ONLINE_PGDAT */

/* next_zone() is available */
/* #undef HAVE_NEXT_ZONE */

/* struct path used in struct nameidata */
#define HAVE_PATH_IN_NAMEIDATA 1

/* yes */
/* #undef HAVE_PDE_DATA */

/* pgdat helpers are available */
#define HAVE_PGDAT_HELPERS 1

/* pgdat_list is available */
/* #undef HAVE_PGDAT_LIST */

/* __put_task_struct() is available */
#define HAVE_PUT_TASK_STRUCT 1

/* linux/sched/rt.h exists */
/* #undef HAVE_SCHED_RT_HEADER */

/* set_fs_pwd() is available */
/* #undef HAVE_SET_FS_PWD */

/* set_fs_pwd() needs const path * */
/* #undef HAVE_SET_FS_PWD_WITH_CONST */

/* set_normalized_timespec() is available as export */
#define HAVE_SET_NORMALIZED_TIMESPEC_EXPORT 1

/* set_normalized_timespec() is available as inline */
#define HAVE_SET_NORMALIZED_TIMESPEC_INLINE 1

/* struct shrink_control exists */
#define HAVE_SHRINK_CONTROL_STRUCT 1

/* shrink_dcache_memory() is available */
/* #undef HAVE_SHRINK_DCACHE_MEMORY */

/* shrink_icache_memory() is available */
/* #undef HAVE_SHRINK_ICACHE_MEMORY */

/* ->count_objects exists */
/* #undef HAVE_SPLIT_SHRINKER_CALLBACK */

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* task_curr() is available */
/* #undef HAVE_TASK_CURR */

/* timespec_sub() is available */
#define HAVE_TIMESPEC_SUB 1

/* linux/uaccess.h exists */
#define HAVE_UACCESS_HEADER 1

/* kernel defines uintptr_t */
#define HAVE_UINTPTR_T 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* user_path_dir() is available */
#define HAVE_USER_PATH_DIR 1

/* usleep_range is available */
#define HAVE_USLEEP_RANGE 1

/* vfs_fsync() is available */
#define HAVE_VFS_FSYNC 1

/* yes */
/* #undef HAVE_VMALLOC_INFO */

/* Page state NR_ACTIVE is available */
/* #undef HAVE_ZONE_STAT_ITEM_NR_ACTIVE */

/* Page state NR_ACTIVE_ANON is available */
#define HAVE_ZONE_STAT_ITEM_NR_ACTIVE_ANON 1

/* Page state NR_ACTIVE_FILE is available */
#define HAVE_ZONE_STAT_ITEM_NR_ACTIVE_FILE 1

/* Page state NR_FREE_PAGES is available */
#define HAVE_ZONE_STAT_ITEM_NR_FREE_PAGES 1

/* Page state NR_INACTIVE is available */
/* #undef HAVE_ZONE_STAT_ITEM_NR_INACTIVE */

/* Page state NR_INACTIVE_ANON is available */
#define HAVE_ZONE_STAT_ITEM_NR_INACTIVE_ANON 1

/* Page state NR_INACTIVE_FILE is available */
#define HAVE_ZONE_STAT_ITEM_NR_INACTIVE_FILE 1

/* Define to the sub-directory in which libtool stores uninstalled libraries.
   */
#define LT_OBJDIR ".libs/"

/* get_zone_counts() is needed */
/* #undef NEED_GET_ZONE_COUNTS */

/* rwsem_is_locked() acquires sem->wait_lock */
/* #undef RWSEM_IS_LOCKED_TAKES_WAIT_LOCK */

/* struct rw_semaphore member wait_lock is raw_spinlock_t */
#define RWSEM_SPINLOCK_IS_RAW 1

/* Define the project alias string. */
#define SPL_META_ALIAS "spl-0.6.3-1"

/* Define the project author. */
/* #undef SPL_META_AUTHOR */

/* Define the project release date. */
/* #undef SPL_META_DATA */

/* Define the libtool library 'age' version information. */
/* #undef SPL_META_LT_AGE */

/* Define the libtool library 'current' version information. */
/* #undef SPL_META_LT_CURRENT */

/* Define the libtool library 'revision' version information. */
/* #undef SPL_META_LT_REVISION */

/* Define the project name. */
#define SPL_META_NAME "spl"

/* Define the project release. */
#define SPL_META_RELEASE "1"

/* Define the project version. */
#define SPL_META_VERSION "0.6.3"

