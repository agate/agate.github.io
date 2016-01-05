--- 
layout: post
title: "Hibernate的Set排序"
wordpress_id: 51
wordpress_url: http://www.agatezone.cn/code/?p=51
---
其实也没有什么，内行的人觉得这个是小Case吧。呵呵，这里我不是想说具体的方法，主要是一个感想：
<code>&lt;map
&nbsp;&nbsp;name="propertyName"
&nbsp;&nbsp;table="table_name"
&nbsp;&nbsp;lazy="true|false"
&nbsp;&nbsp;inverse="true|false"
&nbsp;&nbsp;cascade="all|none|save-update|delete|all-delete-orphan"
&nbsp;&nbsp;<span style="color: #99cc00;">sort="unsorted|natural|comparatorClass"</span>
&nbsp;&nbsp;<span style="color: #ff0000;">order-by="column_name asc|desc"</span>
&nbsp;&nbsp;... 其他属性
&gt;
<br />
&nbsp;&nbsp;&lt;key ... /&gt;
&nbsp;&nbsp;&lt;map-key ... /&gt;
&nbsp;&nbsp;&lt;element ... /&gt;
&lt;/map&gt;</code>
很多人首先想到的是sort，而且sort已经给出了排序的实现，我们只管天上属性方可。可是我们大多程序员是从学 SQL 转到 Hibernate 这个 ORM 的持久层框架上来的，旧有的观念还是喜欢“order by xxxx desc”。不是说自己怀旧，我发现很多朋友都有这个习惯。所以，一般来说还是建议使用 order-by="column_name asc|desc" 这个属性进行对应表字段的排序配置。在一些特殊时候，我也不建议使用 sort 所自带的属性，建议根据需要来具体实现 java.util.Comparator 这个接口来具体实现自定义排序。
