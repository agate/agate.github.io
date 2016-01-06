--- 
layout: post
title: "ATI 显卡在 Ubuntu 9.04 | Ubuntu 9.10 上启用 Compiz 延迟的问题的解决方法"
wordpress_id: 473
wordpress_url: http://www.agatezone.cn/code/?p=473
---
本人所使用的笔记本 T400 搭载的是 ATI 3470 的显卡, 在 Ubuntu 8.10 的时代一直工作良好. 但是当使用了 Ubuntu 9.04 并装好 ATI 驱动之后, 每次开启 Compiz 的视觉特效总会让 UI 行为出现严重的延迟问题. 我每次都不得不放弃很多 UI 特效, 退而使用基本视觉效果.

今日在查阅资料的时候发现已经有人知道如何解决这个问题了. 原来这个是 ATI 显卡的通病. 据一篇文章的作者说, 是一个 xorg 的 Bug, 据说已经 patch 过了, 但是在 Ubuntu 9.04 发布的时候不知什么原因把这个给去掉了. 于是乎导致了这个问题.

解决方案:
9.04
<code># 添加认证:
$ sudo apt-key adv --recv-keys --keyserver keyserver.Ubuntu.com 0x643dc6bd56580ceb1ab4a9f63b22ab97af1cdfa9
#
# 修改/etc/apt/sources.list 加入以下源:
deb http://ppa.launchpad.net/ubuntu-x-swat/xserver-no-backfill/ubuntu jaunty main
deb-src http://ppa.launchpad.net/ubuntu-x-swat/xserver-no-backfill/ubuntu jaunty main
#
# 保存后运行:
$ sudo apt-get update
$ sudo apt-get upgrade</code>

9.10
<code># 添加认证:
$ sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com DBDD06BF16E70E3E
#
# 修改/etc/apt/sources.list 加入以下源:
deb http://ppa.launchpad.net/launchpad-weyland/xserver-nobackfill/ubuntu karmic main 
deb-src http://ppa.launchpad.net/launchpad-weyland/xserver-nobackfill/ubuntu karmic main
#
# 保存后运行:
$ sudo apt-get update
$ sudo apt-get upgrade</code>

这样就搞定了.

<blockquote>或者自己下补丁打包安装:
下载xorg补丁地址
http://launchpadlibrarian.net/32728179/xserver-xorg-backclear.patch

编译xorg并打上补丁，然后安装
sudo apt-get build-dep xorg-server
apt-get source xorg-server
cd xorg-server-1.6.3
patch -p1 < /path/to/xserver-xorg-backclear.patch
debuild
cd ..
sudo dpkg --install xserver-xorg-core*.deb</blockquote>

资料引用自[<a href="http://www.linuxidc.com/Linux/2009-06/20382.htm">link</a>]</blockquote>
