--- 
layout: post
title: "Ruby的REXML库缺陷将导致DOS攻击"
wordpress_id: 120
wordpress_url: http://www.agatezone.cn/code/?p=120
---
Ruby官方网站在8月23日发布了安全通告:
http://www.ruby-lang.org/en/news/2008/08/23/dos-vulnerability-in-rexml/
在Ruby当前使用的XML解析库REXML在解析具有嵌套递归元素的XML文件的时候, 将会出现拒绝服务攻击的缺陷, 导致服务器资源耗尽!

凡是在Rails应用程序当中使用到了XML文件解析功能的都存在上述缺陷,需要进行修复. 在Rails当中的修复办法如下:

<strong>1. Rails2.0.2和以前的老版本</strong>
<a href="http://www.ruby-lang.org/security/20080823rexml/rexml-expansion-fix.rb">下载修复文件</a>, 拷贝到RAILS_ROOT/lib目录下, 并且在environment.rb当中加入语句
<code>require 'rexml-expansion-fix'</code>

<strong>2. Rails 2.1.0以上版本</strong>
<a href="http://www.ruby-lang.org/security/20080823rexml/rexml-expansion-fix.rb">下载修复文件</a>, 拷贝到RAILS_ROOT/config/initializers目录下即可。 
