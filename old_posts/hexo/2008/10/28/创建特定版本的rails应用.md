---
title: "创建特定版本的Rails应用"
date: 2008-10-28
tags:
---

看看我的 rails 版本吧!
<code>$ gem list rails</code>
<blockquote>*** LOCAL GEMS ***
rails (2.1.2, 2.1.1, 2.1.0, 2.0.2, 1.2.6)</blockquote>
是不是很多呀? 用 rails 命令创建一个新应用的时候, 默认使用最新的版本进行构建. 很多情况下要创建特定版本的应用, 可以使用一个额外的参数来达到这个目的, 具体如下:
<code>$rails _[version number]_ appname</code>
例如, 我要建立一个基于 rails 1.2.6 版本的经典 depot 应用就可以:
<code>$rails _1.2.6_ depot</code>
