---
title: "migrate 的 references 原来就是 integer"
date: 2008-09-07
tags:
---

从 rails 2.x 之后, 常用的 migrate 中就多了一个 references 的属性. 一开始还以为 rails 2.x 牛逼了吧数据库中的 references 都给加上了(就是说那个外键啦!). 结果跑到 sqlite 里头一看米有... 怀疑 sqlite 太差了没有外键功能, 于是换了 mysql 的 InnoDB 结果还是一样... 其实就是根据 references 属性指向的那个 model 找到对应 model_id 填充到数据表中罢了!

奶奶的! 和 integer 一样...

从 rails 2.x 之后, 常用的 migrate 中就多了一个 references 的属性. 一开始还以为 rails 2.x 牛逼了吧数据库中的 references 都给加上了(就是说那个外键啦!). 结果跑到 sqlite 里头一看米有... 怀疑 sqlite 太差了没有外键功能, 于是换了 mysql 的 InnoDB 结果还是一样... 其实就是根据 references 属性指向的那个 model 找到对应 model_id 填充到数据表中罢了!

奶奶的! 和 integer 一样...

引用 <a href="http://www.arthurgeek.net/" target="_blank">Arthur</a> 的观点就是 "xxx:references makes migrations even sexier. To compare, xxx_id:integer is the old way of doing the same thing"

附 generate 用例:
<code>$ ./script/generate model User name:string group:references</code>
