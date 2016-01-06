---
title: "Struts1.x + Spring + Hibernate整合开发的一些建议"
date: 2008-04-08
tags:
---

最近使用struts1.x进行项目开发，发现虽然struts2的设计让功能更为强大，但是struts1.x的开发更好定制！完全servlet体系的扩展，虽然有耦合的嫌疑吧，但是让很多从Servlet/JSP开发转移过来的朋友大概会有很大的亲切感。
以下是我得出的Struts1 + Spring + Hibernate整合开发的一些建议：

1.所有页面都用struts来转发！不能直接访问到资源页面。把所有资源页面放在WEB-INF\pages下

2.虽然很多文档中似乎可以不用在struts-config.xml中以plugin的方式启用spring托管【在web.xml中声明监听器】，但是加载spring框架方式使用struts-plugin的这种老式的方式保守。

3.对此！我们的action的type通通改成org.springframework.web.struts.DelegatingActionProxy这个代理类！交给spring动态获取这个action实例！
对此必须设定对应action的bean配置，此bean的并非配置id标示属性，改为配置name属性其值为struts的action的path值。

4.使用ActionForm的validate方法来验证表单数据的合法性。用代码来控制，不使用xml配置。

5.显示页面部分，我们统一使用el表达式+struts标签形式！不使用scriptlet的脚本形式，保证页面的高可读性！

<span style="color: #ff0000;">其他</span>：有可能我们要使用到spring提供的open-session-view的过滤器，来处理持久层的东西，那么我们不得不吧spring的托管放在web.xml中因为这个过滤器要用到那个监听器……注意，事实证明这样是更为优秀的整合手段，可以放心使用！
<blockquote>还有的当然就是我们的编码问题咯！这是一个十分冗长的问题，需要时间来研究【特别是tomcat】的具体运作问题！接下来我会写一个文章来参数这个问题的</blockquote>
