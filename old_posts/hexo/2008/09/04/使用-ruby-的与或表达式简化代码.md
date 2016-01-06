---
title: "使用 ruby 的与或表达式简化代码"
date: 2008-09-04
tags:
---

今天再看 &lt;&gt; 里头其中一位作者的写法给我很大的启示. 在过去我们常常遇到这样的一种判断:
<code>if session[:user_id]
  @user = User.find_by_id(session[:user_id])
else
  xxx
end</code>
文中作者很简单地使用如下代码进行替代:
<code>@user = session[:user_id] &amp;&amp; User.find_by_id(session[:user_id])</code>
是不是很简单? 同样还有 "||" 这种或运算啊~ 就是指但前面非 nil 的时候就取前面的值, 如果是 nil 就去后面的值!
同样可以试试看 "&amp;&amp;=" 和 "||=" 这种赋值方式哦~
