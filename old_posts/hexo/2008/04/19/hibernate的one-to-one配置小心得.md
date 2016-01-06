---
title: "Hibernate的one-to-one配置小心得"
date: 2008-04-19
tags:
---

今天再配置hibernate的hbm配置文件的时候使用了one-to-one的关系，主对象使用cascade="all"属性，子对象使用constrained="true"属性。出乎我意料的是在使用hbm2ddl的自动数据库生成功能后发现：子表竟然没有主表的id字段，而主表也没有子表的id字段……为什么呢？那两个对象是如何找到对方的呢？我纳闷了……

呵呵，其实是我配置错了！主表负责生成id，子表有一个外键引用主表的主键，这样就建立了关系【主表子表都有一致的主键值】。但是我竟然在hbm中配置了两个主键生成器……傻了~~~

这个问题是解决了！了解了hibernate中的one-to-one的实现本质，但是我又出现了问题了：要是两个表都要有自己的主键生成器呢？两者可以独立存在，即：存在 (1,0) - to - (1,0) 这样的关联方式~上面那种方式是无法实现这种方式的呀！！！

通过老师的指点，得知需要配置 many-to-one 的属性
<code>&lt;many-to-one name="group" unique="true" column="group_id" fetch="join"/&gt;</code>
特别是这个<span style="color: #ff0000;">unique="true"</span>【指明是否该字段具有惟一约束：true具有唯一约束、false不具有唯一约束】就等同于等同于one-to-one了，只是这种是使用额外的一个字段，配置外键，这样就可以实现两个表不同外键的一一对应了！
