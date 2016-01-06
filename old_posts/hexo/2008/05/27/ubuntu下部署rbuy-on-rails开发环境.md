---
title: "Ubuntu下部署ruby on rails开发环境"
date: 2008-05-27
tags:
---

开头说一句话，windows的确方便！不过终归要到linux上面来的……太多人在这个平台上开发了，windows下很多都不好用，借助cygwin又不是很舒服＝。＝|||

好言归正传：

1、使用新立得软件包管理器安装
<blockquote>ruby
ruby1.8[自动会勾上,因为这里1.8是默认版本]
ruby1.8-dev
rubygems
rubygems-ruby1.8[自动会勾上,因为这里1.8是默认版本]
其他的依赖管理器会帮你搞定</blockquote>

2、更新rubygem,源里的是0.9的,之所以使用管理器安装是为了解决依赖,如果知道gem依赖什么的话可以直接安装.到<a href="http://rubyforge.org/frs/?group_id=126">官方网站</a>下载最新的版本后,解压到某个文件夹中然后执行
<blockquote>sudo ruby setup.rb</blockquote>
安装之后由于之前安装的gem是0.9的所以bin中的gem还是那样,不能用了,而取而代之的是gem1.8这个执行文件.所以可以执行下面的语句来完成目的.
<blockquote>sudo rm /usr/bin/gem
sudo cp /usr/bin/gem1.8 /usr/bin/gem</blockquote>

3、安装rails,由于最新版本的rails已经到了2.0.2了,但是我还是习惯用1.2.6版本的(因为最新版本改动太大了),所以如果安装最新版本的rails直接
<blockquote>sudo gem install rails --include-dependencies</blockquote>
使用老版本的可以到<a href="http://rubyforge.org/frs/?group_id=307">官方网站</a>上下载对应gem到本地安装
<blockquote>sudo gem install rails-2.0.2.gem --include-dependencies</blockquote>

4、对应安装数据库.之所以说是对应,是因为2.0.2已经不是默认使用mysql数据库了,它迁移到使用sqlite3.这里数据库的安装拜托给新立得软件包管理器安装就ok了.

5、安装对应的数据库驱动.
<blockquote>sudo gem install mysql
如果出现类似
<blockquote>Error installing mysql:
ERROR: Failed to build gem native extension.</blockquote>说明你没有安装libmysqlclient15-dev,到软件包管理器中安装即可.</blockquote>
<blockquote>sudo gem install sqlite3-ruby
如果出现类似
<blockquote>Error installing sqlite-ruby:
ERROR: Failed to build gem native extension.</blockquote>说明你没有安装 libsqlite3-dev, 到软件包管理器中安装即可.</blockquote>

基本OK了,试试看使用rails创建一个工程,启动服务器看看首页中的about连接是不是不会出错,不会出错就对了!

============================================

[2009-7-25]
今天我第一次安装 postgres, 也碰到了一些包依赖的问题. 还是通过 google 的方式来解决的. 发现一个不错的配置步骤网页, 是 UBUNTU 官方的.

<blockquote><strong>Install the sqlite3 connector:</strong>

$ sudo apt-get install libsqlite3-dev
$ sudo gem install sqlite3-ruby

<strong>Install the MySQL database and it's connector:</strong>

$ sudo apt-get install mysql-server mysql-client
$ sudo apt-get install libmysql-ruby libmysqlclient-dev
$ sudo gem install mysql

<strong>Install the PostgreSQL database and it's connector:</strong>

$ sudo apt-get install postgresql-server postgresql-client
$ sudo apt-get install libpq-dev
$ sudo gem install pg</blockquote>

其实只要根据这个安装数据库基本没问题了.
更重要的这次更新是记录: <a href="https://help.ubuntu.com/community/RubyOnRails">Ubuntu-RubyOnRails</a>
