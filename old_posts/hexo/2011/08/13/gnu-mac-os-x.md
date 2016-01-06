---
title: "GNU Mac OS X"
date: 2011-08-13
tags:
---

Mac 下开发我总是没法适应 BSD 的命令参数. 就比如:
> rm -rf dirname

可是我比较喜欢在我忘记这个是一个目录后在后头加上参数, 比如:
> rm dirname -rf

但是 BSD 的 rm 就是不给力, 这样的例子还有很多...

解决方法很简单: **brew** + **gnu tools**

> brew install findutils gnu-sed gnu-tar coreutils gawk --default-names

(其中 --default-names 是为了 coreutils 安装的时候使用默认的名字, 要不然他会给每个命令前面加上 "g" -- 保证和现存的 mac 命令兼容罢了)

还有一点要注意的就是 path 的先后, 请编辑 /etc/paths 文件, 把里头的 /usr/local/bin 和 /usr/local/sbin 放到对应的前面先加载即可.

OK, 好好享受 GNU 的命令吧!
