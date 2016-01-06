--- 
layout: post
title: "VirtualBox 命令备忘"
wordpress_id: 650
wordpress_url: http://www.agatezone.cn/code/?p=650
---
VirtualBox 是一个很不错的虚拟机. 它提供了很多命令行的工具帮助我们管理和使用虚拟机. 这里写一个备忘记录用过的命令:

<strong>VBoxHeadless</strong>
1. 后台启动虚拟机
$ VBoxHeadless -s [server_name] -v off

<strong>VBoxManage</strong>
1. 查看虚拟机的参数
$ VBoxManage guestproperty enumerate [server_name]

[updating...]

