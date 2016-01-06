---
layout: post
title: js to coffee 转换中的一些需要注意的地方
---

这几天工作上需要把一些 javascript 的源码转换成 coffeescript.
当然完全可以用 [js2coffee](http://js2coffee.org) 来实现啦.
但是多数情况下这样生成的代码是不可读的,
比如 class 的封装等等. 还是需要很多人力进行人工转换.
在这些工作中我渐渐发现了一些需要注意的地方, 以及 tips. 于是乎有了这个列表:

* 都记得 coffee 的最后一行是返回值. 但是转换的时候很多时候会忽略这个特性.
  特别是在一些 callback 返回值有特殊处理的时候格外需要注意.
  比如 jquery 的 each 方法. 如果你 return false 那么就相当于 break.

* jquery 事件很多时候可以在 callback 中直接 $(this) 来封装自己为 jquery 对象.
  但是如果 coffee 使用 => 时候还可以通过
  [e.currentTarget](http://api.jquery.com/event.currenttarget/)
  来替代

* javascript 中
{% highlight javascript %}
try {
  // foobar
} catch (e) {
}
{% endhighlight %}
如果 catch 里头什么都没处理.
在 coffee 里头可以连 catch 都不写:
{% highlight coffeescript %}
try
  # foobar
{% endhighlight %}


* ? 在 coffee 里头可以和一个变量连写. 比如 if user? 等价于
  if (typeof user !== "undefined" && user !== null)
