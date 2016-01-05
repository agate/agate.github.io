--- 
layout: post
title: "rails 中 namespace 的嵌套问题"
wordpress_id: 244
wordpress_url: http://www.agatezone.cn/code/?p=244
---
<a href="http://chinaonrails.com/topic/view/2249.html">http://chinaonrails.com/topic/view/2249.html</a> 先是我发起了这个帖子, 问题和这篇文章一样... 纳闷的是为什么 rails 规定如此死板.

我想要建立一个名为 admin 的管理命名空间, 把所有的后台操作放置在这个命名空间下. 于是我就有一个想法, 把链接管理 -- LinksController 分解成一个文本链接和一个图片链接来方便细致管理. 但是还是想保留 LinksController 这个控制器. 于是我这么写 routes.rb 了:
{% highlight ruby %}
map.namespace :admin do |admin|
	admin.resources :posts
	admin.resources :links
	admin.namespace :links do |link|
		link.resources :texts
		link.resources :images
	end
end
{% endhighlight %}
明显, 我想把 :links 即当作 resources 的资源, 又当作 namespace 这个空间的名字. 当时我想是完全行得通的! 我想可以有如下地址规则:
<blockquote>http://host:port/admin/links
http://host:port/admin/links/1
http://host:port/admin/links/texts
http://host:port/admin/links/texts/1
http://host:port/admin/links/images
http://host:port/admin/links/images/2</blockquote>
可是并非如此. 情况是这个 namespace 不认了. 当然前两条地址路由规则是没问题的, 问题是后面几个地址路由规则中 rails 会把 texts 和 images 当作 links 控制器的 action 方法, 情况大致就是这样的.

直到 ashchan 大哥提到他曾经在很老的 rails 版本中完成过 namespace 的嵌套, 我才回过头考虑我的配置和代码书写. 首先我重装了所有 gems 在一个隔离的 sandbox linux 虚拟机环境中, 并重新运行我的工程. 但是发现并不是 gems 的问题. 于是反思我的 routes.rb 代码. 得到如下解决方案:
{% highlight ruby %}
map.namespace :admin do |admin|
	admin.resources :posts
	# 主要是下面这句 named routes[命名路由]
	admin.links "/links", :controller => "links"
	admin.namespace :links do |link|
		link.resources :texts
		link.resources :images
	end
end
{% endhighlight %}
这样即保证了 links 的控制器访问, 又保证了 links 命名空间下的 texts 和 images 控制器的访问.

从这件事情我发现 rails 真的不是我说的那么死板, 而是非常聪明灵活. 看看这个 admin.links 的命名路由吧! 过去我一直以为命名路由只能在 map 这个对象下使用, 现在看来, 其实这个 map 也只是代表着 / 这个根目录的一个命名空间对象罢了! 所以我们自定义的 namespace 的对象一样可以使用命名路由写法!

这里谢谢 ashchan 谢谢 rails!
