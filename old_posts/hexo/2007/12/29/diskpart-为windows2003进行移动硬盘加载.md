---
title: "DISKPART 为windows2003进行移动硬盘加载"
date: 2007-12-29
tags:
---

最近用了windows2003，觉得比xp稳定很多，大概服务没xp开的多吧，PF分页率也小了很多，对于我这个垃圾机器的程序开发者来说是比较好的系统了。

但是问题来了，我的移动硬盘插入后检查到硬件但是没有在“我的电脑”中出现对应盘符，但是似乎U盘不存在此类问题……

开始很是疑惑，于是google了，发现只要在“管理” 中的“磁盘管理”中手动分配分区号就可以认到了（大概是服务器安全设置问题吧……）

问题是解决了，但是似乎不太方便，我觉得windows系列的系统好在他总有一个银弹可以完美的解决系统问题，于是再google，发现了一个叫做“DISKPART” 的自带硬盘管理工具，具体使用细节我没深入研究，但是完全解决了我的“移动硬盘”加载问题，方法如下：

进入CMD的DOS命令窗口，键入diskpart回车，系统会进入diskpart的操作命令行，继续键入automount enable回车，系统会提示“已经启用自动装载新卷”，那么就OK了，插入移动硬盘即可实现自动识别了！

大概显示看看这个截图：

<img src="http://photo14.yupoo.com/20071229/172648_774162697_gpzxppxa.jpg" alt="screenshot" height="161" width="522" />
