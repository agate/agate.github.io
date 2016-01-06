---
title: "通过jaxws-ri于webservice来一次亲密接触"
date: 2007-10-30
tags:
---

关于SOA、Web Service已经在我耳边晃悠了很久了，但是一直以来我都因为技术上的问题以及实际需求的问题没有关照过这两个似乎已被企业提高到一个很高的关注度的现代技术。

借助这回培训，老师介绍了一个叫做jaxws-ri(reference implemention)的webservice工具，即jax的web服务参考实现。这个工具不敢说好不好，我也说不出个所以然，毕竟第一次接触吧，但是它能让初识webservice的程序员两三下就搭出webservice的服务！

不说太多过程的话了！现在开始：

1. 获得开发包

当然是到 SUN 的开发网站下载 <a href="https://jax-ws.dev.java.net/" target="_blank">JAX-WS RI</a> ，下载下来的只是一个jar包，参考官网上的方法在命令行调用：
<code>java -jar JAXWS2.1.2-20070917.jar
//注：这里根据你下的版本不同jar包的名字也会不同</code>

这时候会在调用这条命令的文件夹下生成一个文件夹，里头包括了bin、lib、doc等。其中bin中的有两个重要的生成工具！

2. 配置

在你的机器中配置好环境变量<strong>JAXWS_HOME</strong>以及在<strong>Path</strong>环境变量中加入<strong>%JAXWS_HOME%\bin</strong>

3. Start

部署基本完成了，开动我们的eclipse吧！创建一个java工程，导入jaxws下lib中的所有jar包到构建空间中。

4. 实现第一个服务类

让我们建一个包（名字随便啦！）我用server包，在里头建立一个HelloWorld.java类，代码如下：
{% codeblock lang:java %}
public class HelloWorld {
	public String getHello(String name) {
		return "Hello " + name + "!";
	}
}
{% endcodeblock %}
十分简单的代码对吧，不过做一个helloworld这个完全够了！不过既然是webservice当然有点不同咯！需要根据jdk5+的特性加入一些@符号的注释。完整代码如下
{% codeblock lang:java %}
@WebService
/*
* 如果出现找不到符号
* 在eclipse中按 ctrl+shift+o 导入对应包即可
*/
public class HelloWorld {
	public String getHello(String name) {
		return "Hello " + name + "!";
	}
}
{% endcodeblock %}
5. 接下来就是生成服务端所需使用的stub类了。

（庆幸这个完全由jaxws-ri工具包中的bin下的wsgen.bat批处理命令完成了）。我们现在需要的是在工程根目录下建立一个genServer.bat文件（当然也可以进到当前目录下的cmd中进行操作）。
<code>键入下列命令：（dos中相同）
wsgen -cp bin server.HelloWorld -s src -d bin</code>
<blockquote>请注意这里的
-cp 代表你项目的class编译文件存放的位置
(这里的server.HelloWorld就是那个服务类的类全名)
-s 代表你将把生成的stub类的源代码放置到的目录
-d 代表你将把生成的stub编译好的class放置到的目录</blockquote>
6. 发布服务

执行后刷新eclipse中的工程，你将发现多了一个包，以及包中的那些stub类。说明服务器端所需的准备已经完成了，你只需要的是把webservice启动起来（说白了是吧wsdl注册到URL上） 。

在server包中建立一个Main.java（只是为了启动罢了，名字随便）代码如下：

{% codeblock lang:java %}
public class Main {
	public static void main(String[] args) {
		Endpoint.publish("http://localhost:8001/HelloWorld", new HelloWorld());
	}
}
{% endcodeblock %}
写好运行就ok了！不信？登录 <a href="http://localhost:8001/HelloWorld">http://localhost:8001/HelloWorld</a>
就知道了！看看是不是出现了SOAP的xml节目了？

7. 客户端根据WSDL获取SOAP的服务描述

首先我们知道，一般来说，先要有服务才能调用对吧！但是有什么服务呢？我们需要问一下发布服务的网址，他会给出一个SOAP格式描述的服务来给我们参照实现自己的调用类。

你会说哇！我没学过这些我怎么知道怎么写客户端的stub类啊？（呵呵，我也没学过，我不是也写好了吗）其实啊！是jaxws-ri的另一个生成工具即：wsimport.bat这个命令让这些操作一步完成，自动生成了所以需要的客户端stub类。使用方式如下：

<code>建立genClient.bat(同genws，你也可以在工程目录的cmd下执行)
wsimport -s src -d bin -p client.jaxws http://localhost:8001/HelloWorld?wsdl</code>

再刷新eclipse中的工程，是不是又有一个包出来了？那个就是你的本地包了，RPC全靠它啦！

8. 建立客户端的应用来实现RPC

这里是最后一步了！你将看到如何在客户端调用WebService中提供的方法！

还记得我们前面写的那个HelloWorld类吗？他有个getHello方法，能够让你传入一个字符串并返回一个字符串。这是服务端的方法，现在以下代码将实现客户端的调用！
{% codeblock lang:java %}
package client;

import client.jaxws.HelloWorld;
import client.jaxws.HelloWorldService;

public class Main {
	public static void main(String[] args) {
		HelloWorld hw = new HelloWorldService().getHelloWorldPort();
		System.out.println(hw.getHello("agate"));
	}
}
{% endcodeblock %}
在保证你server.Main正在运行的前提下执行这个client.Main你会发现你的控制栏中出现了"hello agate"的输出。

Done！本文只是初识jaxws-ri的经验，只供初学者快速上手！
