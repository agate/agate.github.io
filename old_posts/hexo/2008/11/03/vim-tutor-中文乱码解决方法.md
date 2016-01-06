---
title: "VIM Tutor 中文乱码解决方法"
date: 2008-11-03
tags:
---

我是使用 Ubuntu 操作系统的, 其默认的终端编码方式是 UTF-8. 在我使用中文语言作为系统的语言环境后, 我在使用 VIM 自带的 Tutor 教程学习的时候就出现了乱码现象. 究其原因是因为默认中文的 Tutor 是以 GB2312 的编码方式进行编码的. 所以很简单的解决方式是:
<code>$sudo cp /usr/share/vim/vim71/tutor/tutor.zh.euc /usr/share/vim/vim71/tutor/tutor.zh.euc_bak
$sudo gedit  /usr/share/vim/vim71/tutor/tutor.zh.euc
另存为 --> 设置为 UTF-8 编码 --> 确认 --> Done</code>
解决! 这里注意的是不同的操作系统可能 VIM 安装的路径以及版本不同, 具体的修改一下就好了!
