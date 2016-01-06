---
title: "ubuntu 在 virtualbox 中的网络及共享设置"
date: 2010-05-01
tags:
---

现在一直使用的是 windows 7 加上 ubuntu server 的系统配置. 这里记录一下一些安装配置的细节:

<strong>1. 安装 Guest Additions</strong>
先在菜单中选择安装 Guest Additions
<code>$ sudo apt-get install dkms
$ cd /cdrom
$ sudo ./VBoxLinuxAdditions-amd64.run</code>

<strong>2. 关机并且设置 nat 端口映射</strong>
打开 cmd 并且进入 virtualbox 的安装目录
<code>PATH&gt; VBoxManage setextradata "<span style="color: blue;">[你的虚拟机名字]</span>" "VBoxInternal/Devices/<span style="color: blue;">[e1000]</span>/0/LUN#0/Config/<span style="color: blue;">[自己定义名字(根据需要比如ssh/http)]</span>/Protocol" <span style="color: blue;">[TCP 或者 UDP]</span>
PATH&gt; VBoxManage setextradata "<span style="color: blue;">[你的虚拟机名字]</span>" "VBoxInternal/Devices/<span style="color: blue;">[e1000]</span>/0/LUN#0/Config/<span style="color: blue;">[自己定义名字(根据需要比如ssh/http)]</span>/GuestPort" <span style="color: blue;">[端口号]</span>
PATH&gt; VBoxManage setextradata "<span style="color: blue;">[你的虚拟机名字]</span>" "VBoxInternal/Devices/<span style="color: blue;">[e1000]</span>/0/LUN#0/Config/<span style="color: blue;">[自己定义名字(根据需要比如ssh/http)]</span>/HostPort" <span style="color: blue;">[端口号]</span></code>
(如果你使用 PCNet 网卡, 就把 e1000 改成 pcnet. e1000 适用于 Intel PRO/1000 网卡)
一般来说, 映射 ssh 的 22 端口, http 的 80 端口, 基本就够用了.

<strong>3. 设置共享目录</strong>
首先在 virtualbox 中设置好共享目录
然后编辑 ubuntu 中的 <span style="color: #808000;">/etc/fstab</span> 并且加入:
<code><span style="color: blue;">[共享目录名]</span> <span style="color: blue;">[ubuntu下的目标目录]</span> vboxsf defaults 0 0</code>

virtualbox 提供了很好的文档 <a href="http://www.virtualbox.org/manual/">http://www.virtualbox.org/manual/</a>

<strong>备注: </strong>如果你使用原来的介质但是新建立了一个虚拟机的话, 会发现 ubuntu 找不到网卡了. 解决方法是:
<code>$ sudo rm /etc/udev/rules.d/70-persistent-net.rules
$ sudo reboot</code>
