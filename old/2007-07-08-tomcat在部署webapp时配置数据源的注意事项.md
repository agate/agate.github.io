--- 
layout: post
title: "Tomcat在部署webapp时配置数据源的注意事项"
wordpress_id: 19
wordpress_url: http://www.agatezone.cn/?p=19
---
今天同学在用eclipse导出war包放入tomcat中运行的时候发生了一个奇怪的异常，原本在eclipse中可以正常显示的页面全部不能显示了，在log中分明地写着：

    java.sql.SQLException: [Microsoft][ODBC 驱动程序管理器] 未发现数据源名称并且未指定默认驱动程序

（ps.他是用access通过odbc数据源进行连接的）

看了 odbc 中的用户数据源中也有对应的数据源。结构折腾了半天，怀疑是odbc驱动不对把 **Driver do Microsoft Access** 改成了 **Microsoft Access Driver** 问题依然继续… 莫名的发现是不是应该放在“系统”的数据源里。这不，就这么一试，好了！和上面的那些odbc驱动完全不大噶的！还以为什么问题，以为做了这么就的软件就这么废了……虚惊一场！
