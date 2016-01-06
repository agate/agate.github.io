---
title: "webwork+spring+hibernate 整合时出现“Error listenerStart”问题的分析与解决"
date: 2007-09-13
tags:
---

这几天学习几大框架的整合运用，挺简单的，但是有点搞人耐性… 出了一些包啊，tag 啊之类的小问题。其中就有这个奇怪的问题，在网上找了些资料贴到这里！

一下引用自"[吴星](http://diracstar.spaces.live.com/)"的MSN空间：

很多人在做 webwork + spring + hibernate 整合时遇到"严重:Error listenerStart"问题
tomcat启动时报如下错误：

    2007-5-31 14:27:13 org.apache.catalina.core.StandardContext start
    严重: Error listenerStart
    2007-5-31 14:27:13 org.apache.catalina.core.StandardContext start
    严重: Context [/testWSH] startup failed due to previous errors

有一种解决方案是把web.xml文件中的
{% codeblock lang:xml %}
    <listener>
      <listener-class>
        org.springframework.web.context.ContextLoaderListener
      </listener-class>
    </listener>
{% endcodeblock %}
改为
{% codeblock lang:xml %}
    <servlet>
      <servlet-name>SpringContextServlet</servlet-name>
      <servlet-class>.....</servlet-class>
      <load-on-startup>1</load-on-startup>
    </servlet>
{% endcodeblock %}

但这种方法可能会出现其他问题（网上又说会导致其他文件无法打开）。

最终解决方案如下：
我用的是tomcat5.5，配置了日志之后打印出下列信息：

    ERROR main org.springframework.web.context.ContextLoader - Context initialization failed
    org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'dataSource' defined in ServletContext resource [/WEB-INF/applicationContext.xml]: Instantiation of bean failed; nested exception is java.lang.NoClassDefFoundError: org/apache/commons/pool/impl/GenericObjectPool
    Caused by:
    java.lang.NoClassDefFoundError: org/apache/commons/pool/impl/GenericObjectPool
    at java.lang.Class.getDeclaredConstructors0(Native Method)
    at java.lang.Class.privateGetDeclaredConstructors(Class.java:2328)
    at java.lang.Class.getConstructor0(Class.java:2640)
    at java.lang.Class.getDeclaredConstructor(Class.java:1953)
    ……

从日志信息看问题已经很明显了，是<span style="color: #0000ff">applicationContext.xml</span>的<span style="color: #0000ff">dataSource</span>问题。

    将
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    改为
    <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">

出现"Error listenerStart"一般是<span style="color: #0000ff">applicationContext.xml</span>中的bean加载有问题。在用eclipse做webwork + spring + hibernate 的项目时一般都是用Myeclipse自动生成那些配置文件，而有些相关的jar&lt;!--[if !supportEmptyParas]--&gt;或者文件并没有加载在至项目中，以至引出奇怪的问题，又因为是自动生成的东西所以往往会忽略一些文件，而问题确恰恰是这些生成的文件所致，所以自动化的东西也未必一定是正确的，呵呵……

<span style="color: #ff8000">org.springframework.jdbc.datasource.DriverManagerDataSource</span> 不可以使用连接池。<span style="color: #ff8000">org.apache.commons.dbcp.BasicDataSource</span>作为注入的DataSource源，为了使用 DBCP的功能，必须要将commons-dbcp.jar加入CLASSPATH中，<span style="color: #ff0000">另外还需要commons-pool.jar和commons- collections.jar</span>，这些都可以在Spring的lib目录下找到。
<span style="color: #ff8000">org.springframework.jdbc.datasource.DriverManagerDataSource</span>并没有提供连接池的功能，只能作作简单的单机连接测试。
使用org.apache.commons.dbcp.BasicDataSource时缺少commons-pool.jar所以会出现如题的问题。
