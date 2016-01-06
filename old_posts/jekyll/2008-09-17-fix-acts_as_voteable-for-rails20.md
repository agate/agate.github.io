--- 
layout: post
title: "fix acts_as_voteable for rails2.0+"
wordpress_id: 191
wordpress_url: http://www.agatezone.cn/code/?p=191
---
在使用 acts_as_voteable 插件开发的过程中, 发现这个插件是服务于 rails1.2.x 的. 但是在 rails2.0+ 下执行某些方法的时候会出现如下错误.
<blockquote>ArgumentError: The :dependent option expects either :destroy, :delete_all, or :nullify (true)</blockquote>
解决方法是修改#{RAILS_ROOT}/vendor/plugins/acts_as_voteable/lib/acts_as_voteable.rb
<code>替换 :dependent => :true
为
:dependent => :nullify</code>
就OK了. 这种方法同样适用于 acts_as_commentable 等此类插件. 因为作者只不过简单重写了一下.
注意的是, 这些插件默认情况下都是真对 MYSQL 编写的. 在 SQLite 下要注意需要修改插件 lib 目录下主文件中的 SQL 语句, 把 FALSE 替换为 '0', TRUE 替换为 't'.
