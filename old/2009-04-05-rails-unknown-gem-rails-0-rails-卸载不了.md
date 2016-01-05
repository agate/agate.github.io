--- 
layout: post
title: "Rails: Unknown gem rails >= 0: Rails 卸载不了"
wordpress_id: 387
wordpress_url: http://www.agatezone.cn/code/?p=387
---
我一般不喜欢改动系统的总体配置, 所以一般我使用 gem 安装的时候都是不加 sudo 的. 于是我的大多数 gems 都是安装在 ~/.gem 下的(包括 rails). 今天装了 rails 2.3.2 似乎有点不爽(感觉). 于是想卸载. 但是在我执行:
<code>$ gem uninstall rails
<span class="message">ERROR:  While executing gem ... (Gem::InstallError)
&nbsp;&nbsp;Unknown gem rails >= 0</span></code>
弄了半天, 也查了是不是路径拼写错误. 还是没弄出来...
后来 google 了一下, 得知由于非默认安装位置(非 sudo 嘛). 所以需要指定 --install-dir 参数. 于是乎我就这么写了:
<code>$ gem uninstall --install-dir ~/.gem/ruby/1.8
<span class="message">ERROR:  While executing gem ... (Gem::InstallError)
&nbsp;&nbsp;Unknown gem rails >= 0</span></code>
还是一样噢... 无奈, 继续 google! 发现一个命令:
<code>$ gem list -d rails
<span class="message">*** LOCAL GEMS ***
rails (2.3.2, 2.2.2)
&nbsp;&nbsp;Author: David Heinemeier Hansson
&nbsp;&nbsp;Rubyforge: http://rubyforge.org/projects/rails
&nbsp;&nbsp;Homepage: http://www.rubyonrails.org
&nbsp;&nbsp;Installed at (2.3.2): /home/agate/.gem/ruby/1.8
&nbsp;&nbsp;&nbsp;&nbsp;(2.2.2): /home/agate/.gem/ruby/1.8</span></code>
这样就十分方便地晓得了具体 gem 安装的路径了, 直接拷贝下来作为 --install-dir 参数即可.
<code>$ gem uninstall --install-dir /home/agate/.gem/ruby/1.8 rails
<span class="message">Select gem to uninstall:
 1. rails-2.2.2
 2. rails-2.3.2
 3. All versions
> 2
Successfully uninstalled rails-2.3.2</span></code>
至此, 小问题解决.

PS. 你会说: 呀 "/home/agate/.gem/ruby/1.8" 和 "~/.gem/ruby/1.8" 不是一样么? 怎么第一次用 --install-dir ~/.gem/ruby/1.8 不行呢?
因为就是不行! 我也不知道, 他就是要绝对路径罢了...
