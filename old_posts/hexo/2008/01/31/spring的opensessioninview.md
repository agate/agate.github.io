---
title: "Spring的OpenSessionInView"
date: 2008-01-31
tags:
---

所谓 OpenSessionInView 就是真对 Hibernate 这个数据持久层框架的一个Web下的使用技巧。我们在日常 MVC 程序开发的过程中，如果使用的是 Hibernate 的数据持久层框架，一定常常在业务逻辑层中出现 Session is closed 的 laze 异常，这是由于 Hibernate 的Session 在上一个操作中我们为了保证 Session  已经及时的回收时被我们关掉了。

我们常常被放在一个很尴尬的地带：我们的 DAO 成负责 CRUD  在执行完成后根据我上面说的那个“好习惯”，肯定要把本次操作的Session关掉，或者说在一个点统一被关掉。那么导致的结果是，当我拿到我们需要的对象时，该对象虽然说是数据完整的，但是他可能有一个 Link 对象，这个对象可是不完整的！顶多是一个包含 ID 的空壳。那很自然的，当我们要访问这个对象中的 Link 对象的某个非ID值的时候，必然抛出“Laze”异常。如果我们之前不关闭那个 Session 似乎一般的解决方案没法告诉在下一个使用层的代码何时关闭，虽然可以成功访问 Link 对象，但是长此以往 Session 就大大占用内存了。

如何设计才好呢？在很多 Hibernate 的使用者中就有人很早地提出了 Open Session In View 这个Web开发的重要理念，即让 Hibernate 的 Session 在整个请求周期中生存（包括建立和消亡）。当然这个是理念，实现手段有很多种了，包括什么参数传递、建立辅助包等等等等。这里我们专门提及 Spring 这个万能的整合型框架是如何处理的。

Spring 为我们提供了一个叫做 OpenSessionInViewFilter 的过滤器，他是标准的 Servlet Filter 所以我们把它按照规范配置到 web.xml 中方可使用。使用中我们必须配合使用 Spring 的 HibernateDaoSupport 来进行开发，也就是说，我们的dao层的类都要继承于 HibernateDaoSupport，从中由 Spring 来控制 Hibernate 的 Session 在请求来的时候开启，走的时候关闭，保证了我们访问数据对象时的稳定性。

下面我大概描述一下使用的方法：

1. 在 web.xml 中加入对应过滤器配置文件
{% codeblock lang:xml %}
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
{% endcodeblock %}

2. 在我们访问持久层数据是使用 Spring 为我们的 HibernateDaoSupport 的支持，并使用其中的对应方法操作我们的持久层数据
{% codeblock lang:java %}
import org.springframework.orm.hibernate3.support.HibernateDaoSupport;

public class XxxDAO extends HibernateDaoSupport {

	public void save(Xxx transientInstance) {
		try {
			getHibernateTemplate().save(transientInstance);
		} catch (RuntimeException re) {
			throw re;
		}
	}

	public void delete(Xxx persistentInstance) {
		try {
			getHibernateTemplate().delete(persistentInstance);
		} catch (RuntimeException re) {
			throw re;
		}
	}

	public Xxx findById(Integer id) {
		try {
			Role instance = (Xxx) getHibernateTemplate().get("Xxx", id);
			return instance;
		} catch (RuntimeException re) {
			throw re;
		}
	}

	public List findByProperty(String propertyName, Object value) {
		try {
			String queryString = "from Xxx as model where model."
					+ propertyName + "= ?";
			return getHibernateTemplate().find(queryString, value);
		} catch (RuntimeException re) {
			throw re;
		}
	}
}
{% endcodeblock %}

其实啊，就是调用 HibernateDaoSupport 中的 getHibernateTemplate() 这个模板方法，再使用里头的对应对持久层操作的方法。

这样，Spring 这个优秀的整合型框架就是轻松地帮我们把烦恼已久的问题解决了。
