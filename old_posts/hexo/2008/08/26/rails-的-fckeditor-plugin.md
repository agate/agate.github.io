---
title: "rails 的 FCKeditor plugin"
date: 2008-08-26
tags:
---

java的老习惯, 就奔着这个富文本编辑器了, 免得我再做一个图片和 flash 的上传组件~ 省时省力.

废话少说, 上地址:<a href="http://github.com/bilson/fckeditor/tree/master" target="_blank">http://github.com/bilson/fckeditor/tree/master</a>

使用方式: 
1. 解压到 rails 项目中 vendor/plugins 目录下, 并重命名为 fckeditor
2. 在命令行下(rails 目录下)执行 $rake fckeditor:install

ps. 也许真的是 java 中毒太深, 老是觉得配置文件是什么文本啊 xml 啊这类的东东. 在为 fckeditor 上传文件类型限制找设置点的时候, 甚至翻到了 fckeditor 源目录下, 可是那里的设置并没有问题. 却忽略了 ruby 一直是代码维护配置的! 其实这个插件中上传的 MIME 类型设置在本插件目录下 app/controllers/fckeditor_controller.rb 文件中.
