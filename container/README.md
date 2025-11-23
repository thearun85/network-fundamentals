# All about containers

Do you know that we dont images to run containers. Yes this was an eye opener for me.

In Linux world, containers actually serves 2 purposes if I may so so.
1. To test an app so that it does not interfere with everything else on your system - something similar to a python virtual environment

2. To run multiple applications - multi tenancy without having to run everything on a single server.

Lets explore more as we go.

## v1 - 

it is a minimal container - there is no namespace isolation.
  we create a filesyste, child process, copy the busybox executable to the root filesystem and execute it.
  when the container is started, it presents a shell and we can run all the utilities provided by busybox. however we need to note that there is no isolation between the process and the container.

  ps and other command which need access to proc doesnt work. no access to internet

## v2

we mount the proc space so that we can run ps command within the container to see its processes. In order to mount, we need to create a namespace using the libc unshare command and the CLONE_NEWNS flag which is a constant defined in linux systems.

also, we do the mounting while running the execvp. this is because, when I tried running the mount before execvp, it was not executed on the container for some reason.

