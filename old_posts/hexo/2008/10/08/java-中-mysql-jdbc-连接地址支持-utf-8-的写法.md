---
title: "java 中 mysql jdbc 连接地址支持 UTF-8 的写法"
date: 2008-10-08
tags:
---

不多说, 上代码:
<code>jdbc:mysql://host:port/db?user=root&amp;password=root&amp;useUnicode=true&amp;characterEncoding=UTF8</code>
这段代码可以用在 "DriverManager.getConnection()" 中, 当然, 在 hibernate 的 xml 配置文件中也是可以使用的. 但是要注意的是在 xml 中记得把 '<span style="color: #ff0000;">&amp;</span>' 替换成 '<span style="color: #ff0000;">&amp;amp;</span>'
