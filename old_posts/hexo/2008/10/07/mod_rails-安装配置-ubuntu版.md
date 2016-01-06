---
title: "mod_rails 安装配置 [Ubuntu版]"
date: 2008-10-07
tags:
---

mod_rails 是<a href="http://izumi.plan99.net/blog/index.php/2008/03/31/benchmark-passenger-mod_rails-vs-mongrel-vs-thin/">赖洪礼</a>和他的团队开发的一种基于 apache module 机制的 RoR 部署运行方式. 这种方式可以充分利用apache的功能, 提供了基于apache的比较好的RoR性能, 而且无需烦琐的部署方式. 甚至在作者的 blog 中的测试方法下 mod_rails 的性能略微超过了 mongrel 和 thin, 是一种相当快的运行方式.

<img src="http://izumi.plan99.net/blog/wp-content/uploads/2008/03/passenger_mongrel_thin_benchmark.png" alt="" />

Rails 的作者 DHH 和 Ruby 作者 Matz 更是对 mod_rails 赞誉有加:
David Heinemeier Hansson 写道
<blockquote>This could definitely become very popular, very fast ;)</blockquote>
Yukihiro Matsumoto 写道
<blockquote>It is often said that Rails is weak on deployment; PHP runs fairly fast just by uploading scripts. Rails is slow on development mode, and requires restarting on production mode (and bit complex to configure). modrails might be the answer for it.</blockquote>
以下的描述当然是建立在你已经安装好 Apache 和 Ruby &amp; Rails 的前提下. 你会发现安装Passenger倒也很简单(你会问, 也? Passenger 是虾米? 嗨~ 就当作 mod_rails 啦!)

在你的命令行下键入:
<code>$sudo gem install passenger
$sudo passenger-install-apache2-module</code>
第一句话就是安装 passenger , 而第二句就是安装和配置 passenger ! 放心, 这个安装配置是向导式的, 十分简单. 安装过程中如果出现什么必要组件没有安装的, 该向导会明确地指出, 并给出解决方案(一般就是让你 apt-get 一下安装东西), 十分智能. 在安装好必要组件后, 重新执行 "$sudo passenger-install-apache2-module" 即可.

一路回车后发现安装向导给出了三行代码让我们放到 Apache 的配置文件中(apache2.conf -- 一般在 /etc/apache2 下). 你放到这个文件的最后一行就 ok 了. 这样便安装好了!

使用也很简单: 比如我有一个 rails 项目放在 /home/agate/dev/rails-app/demo 目录中. 我只许在 Apache 的虚拟主机配置文件中(httpd.conf -- 一般在 /etc/apache2 下)加入:
<code>&lt;VirtualHost *:80&gt;
&nbsp;&nbsp;ServerName xxx.xxx.xxx
&nbsp;&nbsp;DocumentRoot /home/agate/develop/ror/notebook/<span style="color: #ff0000;">public</span>
&lt;/VirtualHost&gt;
<span style="color: #339966;">&lt;!-- 注意这里的 DocumentRoot 路径要精确到 public --&gt;</span></code>
这样, 重启你的 Apache 服务器, 在我的 ubuntu 系统中可以键入:
<code>/etc/init.d/apache2 restart</code>
访问你的域名 xxx.xxx.xxx (当然, 你要事先绑定好!). 你就可以看到你的 rails 应用了!
