---
title: "[APT] 使用 PROXY 设置"
date: 2010-01-04
tags:
---

出于中国某种不可抗拒的力量所致, 我们很多的 apt 源都无法正常访问. 所以使用代理翻墙是必不可免的. 可是如何让 apt 也同样使用这个代理有很多人不是很清楚. 其实有两种方法:

1. apt 配置修改法 (推荐)
编辑 /etc/apt/apt.conf
<blockquote>$ sudo vi /etc/apt/apt.conf
<code>Acquire::http::Proxy "http://server:port/";</code></blockquote>

2. 给 bash 设定 http_proxy 和 ftp_proxy
<blockquote>$ export http_proxy=http://server:port/
$ export ftp_proxy=http://server:port/</blockquote>

现在只要执行 apt 的各个命令就是通过 proxy 走了.
