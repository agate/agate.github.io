--- 
layout: post
title: "struts2中使用Spring的OpenSessionInView出现Session关闭异常的解决"
wordpress_id: 37
wordpress_url: http://www.agatezone.cn/code/?p=37
---
其实这个问题一句话就可以讲清楚：过滤器气垫的顺序要有规则的！

在 Struts2 （或者 WebWork ）这个展现层框架的配置中，我们使用的前端控制器也是使用 Filter 这种方式管理的。一样是在 web.xml 中配置 Filter 的属性，但是由于我们需要由 Spring 托管整个 web 项目的东西，就拿我们这个 OpenSessionInView 的主角 Session 来说吧，如果这个 Session 是由 Spring 在整个程序运行过程中全权负责的话，它啥时候建立，啥时候消亡是 Spring 说的算的，固然必须由 Spring 先建立好在负责发配个对应的适用对象。啥时候建立呢？当时是当请求来的时候咯，当然得让 Spring 先知道吧！所以啊，这个 Spring 的 OpenSessionInViewFilter 的过滤器必须在 Struts2 的 FilterDispatcher 过滤器前配置。

部分代码大致如下：

{% highlight xml %}
<!-- Spring的OpenSessionInView实现 -->
<filter>
	<filter-name>openSessionInViewFilter</filter-name>
	<filter-class>
		org.springframework.orm.hibernate3.support.OpenSessionInViewFilter
	</filter-class>
</filter>
<filter-mapping>
	<filter-name>openSessionInViewFilter</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>

<!-- 添加 Struts2 过滤器 -->
<filter>
	<filter-name>struts2</filter-name>
	<filter-class>
		org.apache.struts2.dispatcher.FilterDispatcher
	</filter-class>
</filter>
<filter-mapping>
	<filter-name>struts2</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
{% endhighlight %}

这样，Spring 的过滤器就可以先于 Struts2 的过滤器得知请求的到来，提前做好开启 Session 转载 bean 的各项准备任务。
