--- 
layout: post
title: "Ubuntu 下开发 Objective C"
wordpress_id: 634
wordpress_url: http://www.agatezone.cn/code/?p=634
---
安装如下的包:
<code>$ sudo apt-get install build-essential gnustep gobjc gnustep-make libgnustep-base-dev gnustep-devel</code>

建立一个 alias 在 .bashrc 中:
<code>alias objcc='gcc `gnustep-config --objc-flags` -lgnustep-base'</code>

这样只要:
<code>$ objcc source_file_name</code>

备注:
gnustep-config --objc-flags 用于 gcc 对于 objc 的参数
