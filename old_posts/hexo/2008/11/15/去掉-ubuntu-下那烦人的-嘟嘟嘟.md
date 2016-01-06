---
title: "去掉 Ubuntu 下那烦人的 \"嘟嘟嘟\""
date: 2008-11-15
tags:
---

不知道大家有没有觉得在默认情况下, 我们的 Ubuntu 在出现警告音的时候不是像 windows 那样亲切地 "叮叮叮", 而是才用 PC 的蜂鸣器来大声地 "嘟嘟嘟". 特别是在我们使用 shell 不全, 或者 vim 在行首/尾时候也会出现这个愤恨的声音. google 了一下找到了解决方法.
1. 就是干脆把 x 环境和 shell 环境通通关闭声音.
方法就是编辑你的 ~/.bashrc 文件, 加入
<code>xset b off</code>
2. 如果你像我一样只是烦恼 shell 下开发烦人问题的话, 就只要把 gnome-terminal 的 profile 中的那个 "终端响铃" 去掉就好了!
