---
title: "可恶的Struts2白痴的OGNL，为何不支持中文"
date: 2008-04-02
tags:
---

最近一直使用struts2进行项目开发，因为之前就是用的webwork进行学习的，可是一直没有使用到页面逻辑的 if 标签。谁知今天用来比较一个String是否等于一个String的时候出现了问题。

这里先对自己不扎实的OGNL知识表示惭愧，我现学现卖地使用了包括EL格式的${}，以及参见的${}和#{}以及直接输入属性的方式都无法识别，可是在我使用输出型标签&lt;s:property/&gt;时竟是完好显示的……

百思不得其解。忽然想到Struts2的Ajax是使用Dojo的，这个框架对于除西欧字符以外的所有字符都是使用Unicode的方式进行编码的(所有的字符都要编程类似 'ऩ' 的格式)。莫非……我马上在action端把属性的值进行了url转换，并写了一个测试用的jsp模板页面，里头也对应的把对比的字符串使用url格式的字符串代替了，结果真的通过了……我的妈呀！不会这么弱吧，这个框架的标签功能岂能这样啊！

没法，只好正规点使用其他标签来替代这种页面标签逻辑的方法。打算努力学几天OGNL和“白痴”的Struts2的标签，知道了结果陆续文章跟进……

补充后续探讨：
<a href="http://www.agatezone.cn/code/?p=48">《续：Struts2的OGNL的中文识别》</a>
