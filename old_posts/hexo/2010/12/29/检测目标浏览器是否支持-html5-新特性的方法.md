---
title: "检测目标浏览器是否支持 HTML5 新特性的方法"
date: 2010-12-29
tags:
---

目前 HTML5 已经是趋势了, 但是也有不幸的问题: 不是所有浏览器都支持 html5, 就算支持也只是部分支持. 于是问题来了, 如果我要用到 html5 的某一个新特性的话我该如何检测用户浏览器是否支持这个特性呢? 答案就是 <a href="http://www.modernizr.com/">modernizr</a>

Modernizr 是一个 Javascript 脚本, 通过简单的调用就可以知道某个属性是否支持. 比如:

{% codeblock lang:javascript %}
// 如果我需要知道用户浏览器支不支持 video 标签, 那么我只需要用
Modernizr.video // 它会返回 true 或者 false

// 如果我要知道用户浏览器的 input 标签支不支持 placeholder 就只需要用
Modernizr.input.placeholder // 它会返回 true 或者 false
{% endcodeblock %}

更多的用例可以访问 Modernizr 的官方文档页面: <a href="http://www.modernizr.com/docs/">http://www.modernizr.com/docs/</a>
