---
title: "spring ioc 快速入门"
date: 2007-12-06
tags:
---

一直以来我们总是使用new的方式来创建对象或对象层级之间的关系
<code>ClassOne one = new <span style="color: #ff0080">ClassOneImpl</span>();</code>
用 UML 图示很明确的告诉我们一个引用只是一个箭头，那我们平时那种new的方式建立关系的方法让我们在以后的代码修改还是添加功能的时候会造成大量的代码修改，比如我们把上面这个 <span style="color: #ff00ff">ClassOneImpl</span> 实现更换成新的一个实现 <span style="color: #00ff00">ClassOneImpl2</span> 那么我们就要修改所有代码中 <span style="color: #ff00ff">ClassOneImpl</span> 的部分……如果这个工程很大的话，这个可是件可怕的修改工程啊！

IOC，即 Inversion of control 中文意思为"控制反转"，个人理解即为把过去在代码中 new 的方式在编译时绑定关系进而在运行时使用的对象关系方式，转化成在运行时加载的方式，即所谓的"反转"。

现在我用一个十分简单的例子实现IOC的HelloWorld
<!--more-->
建立以下一系列java文件：具体请看代码注释！
{% codeblock lang:java %}
package cn.agatezone.spring.helloworld;

public class BeanA {
	private String str = "Hello World";
	public String getStr() {
		return str;
	}
}
{% endcodeblock %}
{% codeblock lang:java %}
package cn.agatezone.spring.helloworld;

public class BeanB {
	private BeanA beanA;
	public void setBeanA(BeanA beanA) {
		this.beanA = beanA;
	}
	public void sayHelloWorld() {
		System.out.println(beanA.getStr());
	}
}
{% endcodeblock %}
这两个是十分简单的两个类对吧！BeanA.java没什么好说的，我们看看那个BeanB.java，不知道你有没有发现我们这里的成员变量beanA没有实例化过……也许你会问：难道这样在sayHelloWorld()方法中使用beanA.getStr()不会出错？呵呵，当然，在我们传统的编码方式下这个代码是会出错的！因为beanA为null嘛！但是我们这里介绍的spring的ioc可以将过去传统的那种new方式获得对象引用的方式利用"依赖注入"（DI）的方式在运行时把BeanA的实例加载到BeanB的实例对象中去！
<blockquote>这里我们介绍一下 <span style="color: #0000ff">DI-Dependency Injection</span> 即"依赖注入"，只是一种形象的说法，意图与IOC如出一辙，就是在运行时期，动态地将实例化的对象加入到要使用这些对象的对象中去。呵呵很拗口对吧，就比如我们这里的BeanA.java中的beanA这个引用，咋一看没有实例化，但是我们可以利用spring的ioc容器在运行时给他加入一个实例化，避免我们new咯！这个就是注入！</blockquote>
要使用spring的ioc托管当然我们要告诉spring如何管理他们咯，如何管理呢？聪明的你一定会晓得是用xml配置文件啦！

那么请看下面这段配置文件代码：
{% codeblock lang:xml %}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
"http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
	<!-- 这里是我们需要配置的地方,其他的是固定格式! -->
	<!-- 在spring的世界里,多有的java对象都成为bean -->
	<!--
		声明beanA的实例
		给定id(就是实例的名称)
		给定class(就是对应实例的完整类路径)
	-->
	<bean id="beanA" class="cn.agatezone.spring.helloworld.BeanA">
	</bean>
	<!-- 声明beanB的实例 -->
	<bean id="beanB" class="cn.agatezone.spring.helloworld.BeanB">
	<!--
		我们的BeanB.java中有一个BeanA的成员变量叫做beanA
		我们把前面的那个声明的bean:beanA在此注入到beanB这个实例中去
	-->
		<property name="beanA" ref="beanA">
		</property>
	</bean>
</beans>
{% endcodeblock %}
我们有了这些以后就可以实现一个简单的ioc的helloworld应用了！

请看我们的测试代码：
{% codeblock lang:java %}
package cn.agatezone.spring.helloworld;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloWorld {
	public static void main(String[] args) {
		//声明一个string来给出配置文件相对类的路径
		String path = "cn/agatezone/spring/helloworld/applicationContext.xml";
		/*
		 * ApplicationContext为spring的一个主要上下文工厂
		 * 其功能很多，我们这里只用其来拿出bean(就是我们的实例)
		 * 因为它是借口，这里我们用对应类路径的ClassPathXmlApplicationContext来实例化他
		 */
		ApplicationContext act = new ClassPathXmlApplicationContext(path);
		//简单吧!像工厂一样使用，获得BeanB的实例
		BeanB bean = (BeanB)act.getBean("beanB");
		//注意哦!这时候我们强大的spring容器已经将beanA注入到beanB这中了!
		bean.sayHelloWorld();
	}
}
{% endcodeblock %}
结果在你运行之后应该不难想象吧！控制台输出HelloWorld，说明即使我们不在类中显式地声明对象实例，依靠我们的spring-ioc容器一样可以在运行时将对象注入！这样对我们未来的代码维护以及功能扩展都有很深远的意义！
