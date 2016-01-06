--- 
layout: post
title: "Gnome 下使用 root 权限在 GUI 环境下操作"
wordpress_id: 285
wordpress_url: http://www.agatezone.cn/code/?p=285
---
常常在 Ubuntu 这种使用 Gnome 的操作西统辖打开一个文件夹, 可是不能往里头添加东西, 或者删除东西等等. 这个是因为我们的权限不够.

在终端下我们可以
1. 单独一个命令
<code>$sudo 命令</code>
2. 长效权限
<code>$sudo -s</code>

但是这些都是终端下的, 很多时候我们喜欢在 GUI 环境中寻找东西并修改/删除/添加. 这里给出多种解决方案:
1. 使用终端命令:
<code>$sudo nautilus</code>
2. 使用 nautilus-scripts 扩展右键, 在 ~/.gnome2/nautilus-scripts 下建立一个名为 "作为ROOT浏览" 的文件. 内容如下:
<code>#!/bin/bash
script-worker browse $NAUTILUS_SCRIPT_SELECTED_URIS root</code>
然后把这个文件改为可执行的属性.(在属性中改, 或者在终端中 chmod +x 都可以)
3. 干脆直接安装帮助扩展
<code>sudo apt-get install nautilus-gksu</code>
安装后会多出 "以管理员打开"
