--- 
layout: post
title: "解决 Wordpress 无法自动升级"
wordpress_id: 430
wordpress_url: http://www.agatezone.cn/code/?p=430
---
明明已经安装好了 vsftp 的 server, ssh 在 terminal 下也是没有问题的, 可以奇怪的是为什么在 wordpress 下自动升级的就无法成功呢?

我确认了 ip 地址, 确认了 用户名/密码, 并且选用了 sftp... 我甚至使用了 ssh 的端口 22 加载 ip 地址后面, 还是不行.

最后还是老外帮了忙. 其实如果你只填写 ip 地址的话 wordpress 是去请求 21 端口的. 但是由于我是使用 ssh 协议, 所以呢 vsftp 的监听端口并非 21. 只要将对应的 vsftp 监听端口加在你 ip 地址的后面就好了.

具体你的 vsftp 是监听那个端口可以在 /etc/vsftpd.conf 下查看 listen_port 来得知. 当然每个不同的系统 vsftp 的配置文件放的地方不尽相同.

来个例子:
在 /etc/vsftpd.conf 文件中
listen_port=9999
我的 ip 是 xxx.xxx.xxx.xxx
所以在自动更新的那个表单中地址栏中填写的应该是 xxx.xxx.xxx.xxx:9999
