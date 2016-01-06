---
title: "Struts2古怪的IOC"
date: 2008-04-01
tags:
---

IOC(DI)即依赖注入，参见的就是Spring的IOC容器，实现就是实现符合java bean的规范的带有无参构造函数的带有对应set和get方法的一个java类(pojo)。前面都是废话，我们都知道注入一般就是使用set方法，对需要的成员变量进行动态的赋值指向。一般get没有什么用，所以我们用spring管理的时候一般只需写入需要注入对象的set方法即可。

但是今天开发展现层的时候……我用struts的表单自动注入的特性写了一个CRUD模块，当然我还是使用原先的逻辑：只写set方法。结果值没有正确被赋值(有的时候只有部分值被获取)。而且发现如果是简单的数值类型的参数在只设置set方法的情况下是可以被赋值的，但是要是参数是一个ValueObject这样的一个实体对象：
{% codeblock lang:java %}
public class User {
	private String userName;
	private String userPwd;
	// --------other private property
	// --------setter
	// --------getter
}
{% endcodeblock %}
那么，如果我们在action中只对user属性写了set方法
{% codeblock lang:java %}
public class UserAction {
	private User user;
	// --------setter
	public String execute() {
		// --------code...
	}
}
{% endcodeblock %}
那么经过我不下10次的不同试验，保证是无法正确赋值的！因为……还缺了个get方法。也不知道具体原因是什么(猜想在struts2的IOC中，对于复杂对象的注入可能同时用到了set和get方法)，但是经验告诉的是set和get方法最好都写！
