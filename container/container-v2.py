import os
import ctypes

os.system("mkdir -p /tmp/minimal/proc")
os.system("cp /bin/busybox /tmp/minimal/")

libc = ctypes.CDLL("libc.so.6")
CLONE_NEWNS = 0x00020000
pid = os.fork()

if (pid == 0):
    libc.unshare(CLONE_NEWNS)
    os.chroot("/tmp/minimal")
    os.chdir("/")
    
    os.execvp("/busybox", ["busybox", "sh", "-c", "/busybox mount -t proc proc /proc && exec sh"])

else:
    print(f"container id is {pid}")
    os.waitpid(pid, 0)
    print("contaner is stopped")
