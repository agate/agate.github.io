---
title: "压缩 VDI 镜像文件"
date: 2010-02-28
tags:
---

<strong>[Windows 虚拟机]</strong>
步骤:
1. 使用 windows 自己磁盘整理把碎片都搞掉

2. 使用微软的 sdelete 把 zero 设为 0
<blockquote>sdelete 的下载地址: http://technet.microsoft.com/en-us/sysinternals/bb897443.aspx</blockquote>
在 CMD 中输入:
<code>sdelete -c</code>

3. 关机

4. 在真实系统中输入:
<code>VBoxManage modifyhd VDI_FILE_NAME --compact</code>

<strong>[Linux 虚拟机]</strong>
步骤:
1. 用一张 LiveCD 启动虚拟机, 使用 GParted 分区软件, 无损改变硬盘大小到最小, 并把释放出来的空间建立一个新的分区

2. 在新分区上执行: 
<code>dd if=/dev/zero of=/dev/{?}</code>

3. 删除这个新分区, 发释放出来的空间并入主分区. 关机!

4. 在真实系统中输入:
<code>VBoxManage modifyhd VDI_FILE_NAME --compact</code>
