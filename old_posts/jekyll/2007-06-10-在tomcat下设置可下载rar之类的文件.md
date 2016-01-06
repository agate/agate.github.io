--- 
layout: post
title: "在tomcat下设置可下载rar之类的文件"
wordpress_id: 14
wordpress_url: http://www.agatezone.cn/?p=14
---
在做jsp文件上传下载页面的时候，其实有很多格式的文件，但是tomcat总是很不聪明将其当作servlet或者jsp页面打开了，导致反应大大变慢，甚至出错……就比如rar文件竟然直接打开了~~

后来发现只要进行一下操作就可以解决问题：
打开: `%TOMCAT_HOME%/conf/web.xml`
找到一大堆这类的代码：
{% highlight xml %}
<mime-mapping>
  <extension>xxx</extension>
  <mime-type>yyy</mime-type>
</mime-mapping>
{% endhighlight %}
然后在后面加入对应的代码（这里红色的xxx就是这个文件的后缀名，绿色的yyy是文件的web类型，比如：image/pict或者application/pdf）

里面增加rar文件的mime映射就可以了。  
具体的添加格式可以对照doc之类的后缀（默认的web.xml里有这种文件的MIME映射），rar的MIME网上搜索一下就有了。
{% highlight xml %}
<mime-mapping>
  <extension>rar</extension>
  <mime-type>application/octet-stream</mime-type>
</mime-mapping>
{% endhighlight %}
其实就是这样来解决这类文件在ie中乱码显示或者是直接被应用程序启动的结果。
