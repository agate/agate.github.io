---
title: bundle path
date: 2014-11-26
tags:
---


过去一直以为 bundle 使用的都是 gem list 里头的 gem.
如果没有他就会安装一个 ( gem install ).

现在才知道原来他使用的 gem 可以存放在其他地方.
你只要在 bundle install 的时候指定 --path 属性就行了.

那你会问了:
那 bundle exec 的时候怎么知道去哪里找这些 gem 呢?
是不是每一次运行程序的时候都需要指定 --path 呢?

其实不用啦~ bundle install 的时候,
它会在你的 project 目录下生成一个 .bundle 的目录.
里头有一个 config 文件,
这个记录了你 bundle install 时候指定的 path.
这样 bundle 在运行你的 code 的时候,
就会去 config 里头设置的 path 里去找 gems 了.
