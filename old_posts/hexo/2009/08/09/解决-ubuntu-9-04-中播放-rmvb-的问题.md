---
title: "解决 Ubuntu 9.04 中播放 RMVB 的问题"
date: 2009-08-09
tags:
---

在 Ubuntu 下看不了 RMVB 的最重要的原因是因为没有 w32codecs 这个解码包. 

我们的确可以使用 apt-get 看到它的确在控制范围中. 但是 ubuntu 官方的源中竟然没有包括这个东西. 所以直接使用 apt-get 是安装不上的. 网上流传的解决方法普遍都是给出一些源地址, 然后让我们加入 source.lst 中. 这里我推荐一个比较简单好记的方法, 使用 ubuntu-tweak, 在其第三方软件那里勾选 Medibuntu. 然后点击 Refresh 按钮, 等待更新结束.

最后你只需要在 Terminal 中输入:
<code>$ sudo apt-get install w32codecs libdvdcss</code>
其中 libdvdcss 装不装取决于看不看 DVD.
到此问题就解决了.

参考地址[<a href="http://www.ubuntugeek.com/install-mplayer-and-multimedia-codecs-libdvdcss2w32codecs-in-ubuntu-710-gutsy-gibbon.html">link</a>]
