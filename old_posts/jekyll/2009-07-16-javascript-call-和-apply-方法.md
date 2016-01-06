--- 
layout: post
title: "javascript: call 和 apply 方法"
wordpress_id: 451
wordpress_url: http://www.agatezone.cn/code/?p=451
---
call写法为: fun.call(thisArg[, arg1[, arg2[, ...]]])
apply写法为: fun.apply(thisArg, [argsArray])

其中 call 和 apply 的第一个参数是一致的, 其实就是设定 this 对象. 两个方法的区别在于 call 的参数是分开传的, apply 是拼成数组传的(很适合直接传递 arguments)

{% highlight javascript %}
// 以下两个实现效果一致.

jq.click(function (e) {
  fun.call(this, e);
});

jq.click(function () {
  fun.apply(this, arguments);
});
{% endhighlight %}
