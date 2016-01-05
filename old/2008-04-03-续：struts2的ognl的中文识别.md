--- 
layout: post
title: "续：Struts2的OGNL的中文识别"
wordpress_id: 48
wordpress_url: http://www.agatezone.cn/code/?p=48
---
原来还是自己的问题……首先自我检讨一下，常常总是自以为是用自己的思维方式想问题。呵呵，这个真的是打开眼界啊！原来 OGNL 这个玩意有如此大的魔力，难怪 Struts2 使用他哈！厉害……

说道上回写的那个中文问题，本来是以为是转换成什么 Unicode 编码方式了，其实不然，只不过 Struts2 的 OGNL 有点低智商，只认 <span style="color: #ff0000;">''</span> 符号里的西欧字符为字符串，其他的字符出现就会抛个 FormatException 异常……比较罕见，但是这个也使我研究了一小下 OGNL 的“真才实学”。

发现 Struts2 中
<code>&lt;s:if test="#user.sex == 'male' "&gt; ... &lt;/s:if&gt;
是可以的</code>
<code>&lt;s:if test="#user.sex == '男' "&gt; ... &lt;/s:if&gt;
是不行的，必须改成
&lt;s:if test="#user.sex == '男'.toString() "&gt; ... &lt;/s:if&gt;</code>

发现牛逼在何处了吧…… OGNL 竟然除了属性的调用，还可以调用方法。像上面这样使用的话，中文的 OGNL 比较就基本没有问题了。
