---
title: "Gnome 下在当前文件夹下打开终端"
date: 2008-11-08
tags:
---

<code>$sudo apt-get install nautilus-open-terminal</code>
这样便会在每个文件夹的右键菜单中出现 "在终端中打开" 的一个选项, 选择便会打开一个终端, 路径为当前文件夹!

当然, 可以使用 nautilus-scripts 添加右键扩展. 在 ~/.gnome2/nautilus-scripts/ 目录下新建一个文件名为 "从这里打开终端", 内容如下:
<code>gnome-terminal --working-directory=$PWD</code>
之后把这个文件设置为可执行(在属性中选择, 或者命令行 chmod +x 怎么设置随你开心)
然后在右键有个 "脚本" 里头就有了!

记得重启 X环境噢! Ctrl + Alt + Backspace
