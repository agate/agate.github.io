---
title: "java编译和执行的一些技巧"
date: 2007-06-03
tags:
---

这里自以为是觉得这个是技巧……

因为自己在初学的时候只会
> javac [ClassName].java
接着各式各样的IDE就开始开心地使用起来了……结果很基础的东西就这样Say Good Bye 了。

最近开始学习Hibernate，因为不会ANT进行应用部署，不得不重拾java这些基础东西，发现很多问题本应该是IDE简单的自动生成在黑漆漆的CMD下就发愣起来了……

觉得要记一些有用的东东：（呵呵，至少慢慢连载吧）

1. javac编译时把Class编译到对应的包中：
> javac -d . [ClassName].java
2. java运行包中文件时不能到包中运行java [ClassName]，而应该：
> java [PackageName].[ClassName]

【more】待续……
