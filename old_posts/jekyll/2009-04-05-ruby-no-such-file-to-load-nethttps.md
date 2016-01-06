--- 
layout: post
title: "Ruby: no such file to load -- net/https"
wordpress_id: 384
wordpress_url: http://www.agatezone.cn/code/?p=384
---
今天在新的 Ubuntu 上面安装 rails 的时候碰到了这样的问题:
<blockquote>`require_frameworks': no such file to load -- net/https (RuntimeError)</blockquote>
原来是缺少 libopenssl-ruby library:
解决方案:
<code>$sudo apt-get install libopenssl-ruby</code>
本文作为 <a href="http://www.agatezone.cn/code/archives/61">Ubuntu下部署rbuy on rails开发环境</a> 补充
