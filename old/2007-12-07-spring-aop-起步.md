--- 
layout: post
title: "Spring AOP 起步"
wordpress_id: 27
wordpress_url: http://www.agatezone.cn/code/?p=27
---
其实我的个人表达能力不是很好……估计小时候语文没学好～也可能是aop这个概念本身意会的程度很大吧！呵呵寒暄一下！

正式进入主题：AOP 即 Aspect Oriented Programming 的缩写，中文译为"面向切面编程"。本篇没那么学术化，只是为了快速入门了解真实的使用方式！我们不用那么早去想这个名词的意义，fellow me，用真实的代码透析AOP的含义。

不知各位有没有项目开发的经验，如果有的话你应该可以清楚地了解到我们的代码中常常充斥着大量的日志记录代码，我们用log4j等日志记录工具一段一段地记录程序运行的信息。也许有个别是十分特殊的，但是似乎大部分都是例行公事吧！或者在丢出exception的时候捕获其message然后记入日志对吗？这样的代码难道不觉得碍眼？修改起来是不是也很麻烦？要是我们换了一个日志记录工具怎么办？呵呵，别吓到了，没这么严重啦，这些都是极端情况，平时我们还是很开心地写着这些东西。但是今天要说到的这个aop可以将一些特别的操作提取出来，作为我们的"通知-advice"，在运行时加载到对象中。就是说，我们可以在代码中不写日志记录段，但是在运行时加载一些"通知"到需要记录日志的"切入点-pointcut"动态地加入日志记录功能。
<!--more-->
呼～～～怎么还是文绉绉的……说个简单的例子，来配合我们的代码：一个人，他要吃饭，当然就要吃咯，我们实现了一个Person借口，告诉有eat点方法！也写了一个该接口的实现PersonImpl.java
{% highlight java %}
package cn.agatezone.spring.aop;

public interface Person {
    public void eat();
}
{% endhighlight %}
{% highlight java %}
package cn.agatezone.spring.aop;

public class PersonImpl implements Person {
    public void eat() {
        System.out.println("oh! i'm eating now!");
    }
}
{% endhighlight %}
这个人原本是下层阶级的典型，饭前不洗手。但是有一天他变成了中层阶级的典型，要洗手再吃饭了，怎么办？重写Person借口，加入一个方法washhands()？还是在PersonImpl的实例中重写eat方法，在原本方法段前加入洗手方法调用？着不太好吧，这个还是简单的例子，要是项目大了，Person的实现多了好多，怎么办？还是一个一个重写？不用的，aop来帮助我们，不就是饭前洗手吗？我们只要实现一个MethodBeforeAdvice借口就解决这个问题啦！看看我的代码：
{% highlight java %}
package cn.agatezone.spring.aop;

import java.lang.reflect.Method;

import org.springframework.aop.MethodBeforeAdvice;

public class BeforeEat implements MethodBeforeAdvice {
    /*
     * 这里的method就是被托管的bean(我们这里的Person)中的方法
     * 这里的args是指 对应方法(这里是指Person中的任何方法)中的参数
     */
    public void before(Method method, Object[] args, Object target)
    throws Throwable {
        if(method.getName().equals("eat")) {
            System.out.println("before eat something i must wash my hands!");
        }
    }
}
{% endhighlight %}
哦，如何使用呢？当然还是xml配置文件啦！详情看我的xml如下：
{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
    <bean id="beforeEat" class="cn.agatezone.spring.aop.BeforeEat"/>
    <bean id="person" class="org.springframework.aop.framework.ProxyFactoryBean">
        <!-- 被代理对象实现的接口-->
        <property name="proxyInterfaces">
            <value>cn.agatezone.spring.aop.Person</value>
        </property>
        <!-- 拦截器(advice)的ids -->
        <property name="interceptorNames">
            <list>
                <!-- 指定前面声明的那个处理bean:beforeEat -->
                <value>beforeEat</value>
            </list>
        </property>
        <!-- 被代理的目标对象-->
        <property name="target">
            <bean class="cn.agatezone.spring.aop.PersonImpl"/>
        </property>
    </bean>
</beans>
{% endhighlight %}
现在配置好了，我们写个测试代码用用看！
{% highlight java %}
package cn.agatezone.spring.aop;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import junit.framework.TestCase;

public class AopTest extends TestCase {
    private static String path =
        "cn/agatezone/spring/aop/applicationContext.xml";

    private ApplicationContext ctx;

    protected void setUp() throws Exception {
        ctx = new ClassPathXmlApplicationContext(path);
    }

    protected void tearDown() throws Exception {
        ctx = null;
    }

    public void testAop() {
        Person p = (Person) ctx.getBean("person");
        p.eat();
    }
}
{% endhighlight %}
运行吧！看看是不是出现了
<blockquote>  before eat something i must wash my hands!
oh! i'm eating now!</blockquote>
这就是一个再简单不过的aop例子了……至少我这么觉得。好让我们回味一下，什么是切入点？说白了就是一个方法嘛！处理这个方法无非在它1.运行前2.返回值的时候3.抛出异常的时候我们来针对其做"通知"就是我们这里的BeforeEat啦，但是我们例子只用了aop中的一种通知-运行前，即实现MethodBeforeAdvice这个接口的通知。还有返回值 和 抛异常 的大家通知可以参照文档进行自我研究啦！本文只为Spring 的 aop 开个头，进一步的学习会在以后发布。

提供些学习资料：

dev2dev 网站中有一个aop的学习文章分两部分

第一部分：<a href="http://dev2dev.bea.com.cn/techdoc/20051216709.html">http://dev2dev.bea.com.cn/techdoc/20051216709.html</a>
第二部分：<a href="http://dev2dev.bea.com.cn/techdoc/20051223712.html">http://dev2dev.bea.com.cn/techdoc/20051223712.html</a>
