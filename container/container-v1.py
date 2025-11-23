import os

os.system("mkdir -p /tmp/minimal")
os.system("cp /bin/busybox /tmp/minimal/")

pid = os.fork()

if (pid == 0):
    os.chroot("/tmp/minimal")
    os.chdir("/")

    os.execvp("/busybox", ["busybox", "sh"])

else:
    print(f"container id is {pid}")
    os.waitpid(pid, 0)
    print("container stopped")
