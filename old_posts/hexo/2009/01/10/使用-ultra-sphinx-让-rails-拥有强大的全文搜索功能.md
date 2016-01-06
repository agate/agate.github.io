---
title: "使用 ultra sphinx 让 rails 拥有强大的全文搜索功能"
date: 2009-01-10
tags:
---

最近项目中使用了 sphinx 作为数据库的全文搜索引擎. 加之使用的是 ror 开发组合, 固然使用到了比较流行的 ultra sphinx plugin. 觉得十分易用就在这里记录一下使用的大致方式(就一 helloworld).

1. 当然是下载安装 sphinx.
可以到 http://www.sphinxsearch.com/downloads.html 网站下载最新的源码编译安装.
(ps 如果你要加入中文分词的支持就要安装 libmmseg. 编译前需要打个补丁. 或者直接使用作者打好补丁的进行编译安装. 具体的方式可以 google 一下)

2. 安装 rails 的 sphinx 插件 "ultra sphinx"
安装依赖 gem
<code>$sudo gem install chronic</code>
进入你的 rails 应用目录中
<code>$./script/plugin install git://github.com/fauna/ultrasphinx.git</code>

3. 开始使用.
其实具体的还是查阅官方 <a href="http://blog.evanweaver.com/files/doc/fauna/ultrasphinx/">doc</a> 比较好. 比较全面一些!
这里还是为了回顾方便, helloworld 来也!

第一步 [准备准备]
<code>$rails sphinx -d mysql
$cd sphinx
$./script/plugin install git://github.com/fauna/ultrasphinx.git
$./script/generate scaffold post title:string body:text
$rake db:create:all
$rake db:migrate</code>
(这些只是大步骤, 具体的什么数据库用户名密码设置这类的自己补上就是了. 还有, 目前 ultrasphinx 仅仅支持 mysql 和 PostgreSQL)

第二步 [声明 model 为 searchable]
编辑 [rails_root]/app/models/post.rb, 内容如下:
{% codeblock lang:ruby %}
class Post < ActiveRecord::Base
  is_indexed :fields => ['created_at', 'title', 'body']
end
{% endcodeblock %}

第三步 [配置/索引/启动]
首先复制配置文件的模板到 config/ultrasphinx 下.
<code>$mkdir config/ultrasphinx
$cp vendor/plugins/ultrasphinx/examples/default.base config/ultrasphinx/</code>
修改 default.base 中的 path 为这个 rails 工程的绝对地址
<blockquote>吧 <% path = "/opt/local/var/db/sphinx/" %>
改成 <% path = "/home/[你]/....." %></blockquote>
<code>$rake ultrasphinx:configure
$rake ultrasphinx:index
$rake ultrasphinx:daemon:start</code>
(第一次执行时候,顺序不能颠倒!)

第四步 [添加点数据试试看]
添加数据我就不说了, 自己启动服务器到对应页面 new 几个出来. <strong>然后重新索引 sphinx.</strong> 然后开启 rails 的 console:
<code>$./script/console
>>@query = '自己写吧'
>>@search = Ultrasphinx::Search.new(:query => @query)
>>@search.run
>>@search.results</code>
