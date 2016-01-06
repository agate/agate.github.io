---
title: "硬盘安装Ubuntu8.04"
date: 2008-05-27
tags:
---

为了模拟出Mac下的开发状态，又没有时间去考虑刻录Mac os x的DVD的我干脆就用Linux了。装Ubuntu也是要刻录的～可怜我那个饱经风霜的combo光驱阿！现在不要说刻录了，读它都比较吃力=。=|||

于是乎寻找硬盘安装的方式。下载下来的就是ISO镜像，我想最好的方式无外乎直接用这个镜像咯！Google了一下，果然可以，就是利用Linux下的硬盘引导工具：grub

准备工作
<blockquote>1、<a href="http://www.ubuntu.org.cn/products/GetUbuntu" target="_blank">ubuntu 8.04 desktop安装镜像 </a>

2、<a href="http://www.linuxidc.com/upload/2008_03/08032814359358.rar" target="_blank">grub for dos</a></blockquote>
分区的问题，我这里不想说什么了，接下来开始做安装前的准备工作

1、把ubuntu 8.04 desktop镜像放到系统根目录下，我这里是C盘。

2、用winrar打开ubuntu-8.04-desktop-i386.iso，提取casper目录内的initrd.gz和vmlinuz两个文件到C根目录下。

3、打开那个“grub for dos”，提取里头的grldr文件，放到C盘下。

4、创建一个menu.lst文件，放在C盘下，内容：

<code>title Install Ubuntu
root (hd0,0)
kernel /vmlinuz boot=casper iso-scan/filename=/ubuntu-8.04-desktop-i386.iso
initrd /initrd.gz</code>

5、编辑 c:\boot.ini

去掉该文件的隐含系统只读属性
用记事本打开 boot.ini
（把 timeout=0 改成 timeout=5 如果需要的话，一般都是30秒的）
在最后一行添加 C:\grldr="Install Ubuntu 8.04 desktop"    保存退出即可！

6、重启计算机，在启动菜单位置，选择Install Ubuntu 8.04 desktop，然后选择最下面一个选项：Install Ubuntu就可以进入安装过程了
