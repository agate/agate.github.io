---
title: "解决 DNS 故障的方法"
date: 2008-10-16
tags:
---

这里说的 DNS 故障不是你自己电脑上 DNS 服务器设置的问题. 而是说我们笨笨的电信运营商们的 DNS 服务器出现了问题. 或者说被可爱的 GFW 浅封杀的域名们. 说这个解决方法的原因是: 我们的 github 登录不上了, 就算登录上了还是无法 clone 出版本. 解决方案十分简单, 就是在 hosts 文件中手动映射.

在 linux 下嘛就是 /etc/hosts 文件
加入:
<code>65.74.177.129	github.com</code>

其他不能登录的网站也是可以这么解决的(如果不是 gfw 封锁这个 ip 的就没问题). 但是如何找到这些对应的 ip 地址呢? 这里提供一个线查询 DNS 的网站: <a href="http://www.subnetonline.com/pages/network-tools/online-nslookup.php">online nslookup</a>(当然~ 用 google 查一下有很多类似网站).
