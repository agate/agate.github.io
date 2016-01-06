---
title: "linux 也需要绿色"
date: 2008-07-17
tags:
---

最近忙于 linux(主要是Debian) 下面的工作, 发觉安装软件时不论是使用自带的 apt-get 或者是下载源下来自己编译总是不知所云... 换句话说就是安装好了, 可以用了, 就是不知道他做了些什么, 放了些什么在哪里...

觉得能不能有一个类似 win 下面那样的 installer 工具啊? 这样自定义安装地址就好多了! 而且还可以卸载. 基于这个想法就在 google code 上面建立了一个工程托管:
<blockquote>link: <a href="http://code.google.com/p/green-softs-for-linux/">http://code.google.com/p/green-softs-for-linux/</a>
svn: svn checkout http://green-softs-for-linux.googlecode.com/svn/trunk/ green-softs-for-linux-read-only</blockquote>
并且把 mysql 和 tomcat 都做了绿化定制. mysql 绿化精简过后解压处在只有 15M 不到. tomcat 呢只做了安装和卸载部分(呵呵, 其实就是在 /usr/bin 下加了软链接罢了), 放入down下来的tomcat目录即可使用.
<em>具体请见 google code svn 中或 google code download 中 README 文件部分.</em>
