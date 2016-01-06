---
title: "Thin: 安装小记"
date: 2009-07-19
tags:
---

今天在 Ubuntu上安装 Sinatra 后准备试试看是否成功, 但是在执行写好的 ruby 脚本的时候发现原来 Sinatra 是没有自带 Server 的. 需要安装 thin, mongrel, webrick 其中至少一个.(都是 rack 服务器好像)

由于 mongrel 和 webrick 都使用过了, 怀着好奇的心情今天试着装了一下 thin, 同时遇到了一些问题, 记录下来.

0. 不用说了 gem install thin

1. g++
我安装到一半就告诉我出错:


<blockquote>make: g++: Command not found
make: *** [rubymain.o] Error 127</blockquote>

我其实不清楚 g++ 和 gcc 的区别, 我觉得很奇怪, 一般不是都默认装了 gcc 么? 怎么安装的时候却找不到 g++ 呢? 怀着怀疑的态度我试着 apt 了一下 g++ 没想到真的有这么一个玩意. 只要安装好了就可以成功通过 gem 安装 thin

2. openssl
装完了当然是用用看咯. 我在命令行键入 thin 却被告知:
<blockquote>/usr/lib/ruby/1.8/rubygems/custom_require.rb:31:in `gem_original_require': no such file to load -- openssl (LoadError)</blockquote>
可是 openssl 我的确装了啊, google 了一下原来还要装 libopenssl-ruby

DONE
