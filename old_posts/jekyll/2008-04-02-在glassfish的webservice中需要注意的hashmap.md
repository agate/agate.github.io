--- 
layout: post
title: "在GlassFish的WebService中需要注意的HashMap"
wordpress_id: 45
wordpress_url: http://www.agatezone.cn/code/?p=45
---
虽然如今的ws标准都已经很智能了，大多的数据类型都可以识别。但是在GlassFish中，发布的ws方法中参数和返回值不可以为hashmap的，但是如果非要要使用键值对该如何使用呢？
最简单的方法就是再次包装：
{% highlight java %}
public class MapBean {
	private HashMap<String,String> hm;
	public HashMap<String, String> getHm() {
		return hm;
	}
	public void setHm(HashMap<String, String> hm) {
		this.hm = hm;
	}
}
{% endhighlight %}
{% highlight java %}
@WebService()
public class HelloWorld {
	public HelloWorld() {
	}
	@WebMethod
	public MapBean getMapBean(HashMap<String,String> hm) {
		MapBean mb = new MapBean();
		hm.put("server", "serverHashMap");
		mb.setHm(hm);
		System.out.println("Hello HashMap...");
		return mb;
	}
}
{% endhighlight %}
这样，加一层包装之后，就可以间接地使用Map了。
