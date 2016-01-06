---
title: "为了使用 scaffold 换回 rails1.2.6"
date: 2008-07-11
tags:
---

在 rails 升级到2.0+之后, 我们熟悉的 scaffold 似乎用法不大一样了~ 这里包括所谓的动态和静态 scaffold. 可以说动态的 scaffold 基本上是用来快速实现功能的, 很多情况下我们用不到他. 一般来说大多数开发这会习惯于使用 generate 方式的scaffold 来生成基础代码框架.

rails2.0+ 版本中, 静态的scaffold使用方法从原来的:
<code>$./script/generate scaffold ModelName [ControllerName] [action, ...]</code>
变成了:
<code>$./script/generate scaffold ModelName [field:type, field:type]</code>
还句话说原本的自定义Controller名字就不好实现了~ 呵呵, 但是有利有弊拉~ 可以像 hibernate 这类 orm 工具那样生成数据库表结构拉!

当然在 rails2.0+ 下如果需要动态的 scaffold 还可以通过加载 scaffold plugin 来实现(因为在 rails2.0+ 版本中, 动态的 scaffold 被作为插件来实现了! ). 具体操作步骤如下:
<code>$./script/plugin install scaffolding</code>
当然, 不仅仅是 scaffold 很多类似功能都在 rails2.0+ 中转化成 plugin 了. 具体需要什么插件可以使用如下命令来查看需要的插件:
<code>$./script/plugin list</code>

这样当然不是很方便(特别是对于我们这种拿这 agile web development with rails 这本书学习的小朋友来说). 看了网上这么多建议之后, 我还是采纳了"使用 rails1.2.6 来学习, 之后过渡到 rails2.0+ 这种方式". 但是我们平时使用的 gem install 方式, 默认会安装 rails2.0+ (即最新版本). 使用如下命令可以实现指定版本的目的:
<code>$sudo gem install rails --version 1.2.6 </code>

这样就可以使用到我们最熟悉的旧版本的命令了. 但是你会说这两个 rails 共存有问题吗? 我不是很清楚, 当然你可以删除一个 rails 的 gem 包来保证其版本的唯一性:
<code>$sudo gem uninstall rails</code>
他会列出你所有的 rails 版本, 并且询问你是否卸载.
这里我说一个我使用的方式, 保证了两个 rails 同时存在, 同时可用:
<code>$rails _x.x.x_ {app_name}</code>
这样就可以建立对应 rails 版本的应用目录了, 当然里头的 script 们也是对应版本的用法!
<em>注: 默认情况下直接输入 rails {app_name} 是建立最新版本 rails 的应用目录.</em>
