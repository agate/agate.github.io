--- 
layout: post
title: "再谈对象匹配之HashCode&Equals"
wordpress_id: 40
wordpress_url: http://www.agatezone.cn/code/?p=40
---
相信每位初学OOP的同学都知道在这面向对象的世界里比较两个对象的方法是使用Equals来实现，可是如何写一个比较完美的又代码量小的Equals函数呢？

还有就是在散列表的数据结构中，散列表自身的数据结构算法需要用到对象比较的方法HashCode，所以常常我们会听到“老者”对我们谆谆而训曰：重写Equals方法是必须的，可是别忘了重写HashCode哦！

HashCode和Equals这两个方法的渊源可谓不浅，在这里我通过简单的代码片段，展示一个目前常用的比较完美且代码量小的方法重写方式：

{% highlight java %}
	/**
	 * 这里我们假定改类的名字为Example
	 */

	@Override
	public int hashCode() {
		int result = 关键属性.hashCode();
		//这里31其实可以由任何一个质素代替，用来保证hashcode的不重复
		result = 31 * result;
		//关键属性不止一个的话可以加上
		//result = result + 关键属性2.hashCode() + ……;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}

		if (obj == null) {
			return false;
		}

		if (getClass() != obj.getClass()) {
			return false;
		}

		Example other = (Example) obj;

		//如果关键属性不止一个的话就多写几个判断
		if (!关键属性.equals(other.关键属性)) {
			return false;
		}

		return true;
	}
{% endhighlight %}
