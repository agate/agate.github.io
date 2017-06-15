title: shm in Docker
date: 2017-06-15 09:55:18
tags:
  - linux
  - docker
---

首先啥是 shm 就不详细说了. 有兴趣的可以去查看 wikipedia. 这里引述一下一个小片段.

> Linux distributions based on the 2.6 kernel and later offer /dev/shm as shared memory in the form of a RAM disk, more specifically as a world-writable directory (a directory in which every user of the system can create files) that is stored in memory. Both the RedHat and Debian based distributions include it by default. Support for this type of RAM disk is completely optional within the kernel configuration file.
>
> FROM: [wikipedia](https://en.wikipedia.org/wiki/Shared_memory)

简单来说在 linux 下 /dev/shm 这个目录可以让用户以内存的速度来操纵文件. 可以把它当做一个 RAM disk — 内存磁盘, 因为是内存所以很快. (但是细节没有这么简单, 有兴趣具体还是看文档).

那么默认情况下, 如果使用 `docker run` 启动一个 container. 用 `df -h | grep shm` 看到的默认只有 64M 大小. 

```terminal
root@docker:~# docker run -it ubuntu df -h | grep shm
shm              64M     0   64M   0% /dev/shm
```

那么如何修改这个大小呢? docker 提供了一个启动参数 `--shm-size=2g` 这样就可以精确的定义 shm 大小啦.

```terminal
root@docker:~# docker run -it --shm-size=2g ubuntu df -h | grep shm
shm             2.0G     0  2.0G   0% /dev/shm
```

那这里是不是直接占用 host 上的 /dev/shm 空间呢? 答案是不是的. host 上的 /dev/shm 和 docker container 里头的 /dev/shm 是相互独立的. 都是使用 host 机器上的内存.

```terminal
root@docker:~# df -h | grep shm
tmpfs            3.7G   84K  3.7G   1% /dev/shm
root@docker:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           7.3G        3.1G        413M         16M        3.8G        2.2G
Swap:           15G        244K         15G
```

```terminal
root@docker:~# docker run -it --shm-size=2g ubuntu bash
root@35afbd3955f2:/# fallocate -l 1G /dev/shm/foo
root@35afbd3955f2:/# df -h
Filesystem      Size  Used Avail Use% Mounted on
none            174G  134G   40G  78% /
tmpfs           3.7G     0  3.7G   0% /dev
tmpfs           3.7G     0  3.7G   0% /sys/fs/cgroup
zpool/docker    174G  134G   40G  78% /etc/hosts
shm             2.0G  1.0G  1.0G  50% /dev/shm
tmpfs           3.7G     0  3.7G   0% /sys/firmware
```

```terminal
root@docker:~# df -h | grep shm
tmpfs            3.7G  124K  3.7G   1% /dev/shm
shm              2.0G  1.0G  1.0G  50% /var/lib/docker/containers/35afbd3955f2c66542868e27eb074b6af132c259f4b865960bcd0804582731e3/shm
root@docker:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           7.3G        2.6G        127M        1.0G        4.6G        1.8G
Swap:           15G        2.4M         15G
```
