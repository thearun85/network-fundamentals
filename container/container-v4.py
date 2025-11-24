import os
import ctypes
import sys

os.system("mkdir -p /tmp/minimal/proc")
os.system("cp /bin/busybox /tmp/minimal/")

libc = ctypes.CDLL("libc.so.6")
CLONE_NEWNS = 0x00020000
CLONE_NEWPID = 0x20000000
CLONE_NEWUTS = 0x04000000  # Add UTS namespace

pid = os.fork()
if (pid == 0):
    libc.unshare(CLONE_NEWNS | CLONE_NEWPID | CLONE_NEWUTS)  # Add UTS
    
    pid2 = os.fork()
    if pid2 == 0:
        os.chroot("/tmp/minimal")
        os.chdir("/")
        os.execvp("/busybox", ["busybox", "sh", "-c", 
                  "/busybox mount -t proc proc /proc && exec sh"])
    else:
        os.waitpid(pid2, 0)
        sys.exit(0)
else:
    print(f"container id is {pid}")
    os.waitpid(pid, 0)
    print("container is stopped")
