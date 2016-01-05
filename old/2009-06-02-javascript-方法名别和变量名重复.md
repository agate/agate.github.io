--- 
layout: post
title: "Javascript: 方法名别和变量名重复"
wordpress_id: 419
wordpress_url: http://www.agatezone.cn/code/?p=419
---
今天在写程序的时候发现我明明写了一个名为 isOpen 的方法, 可是在调用的时候 firebug 就死活提示没有该方法. 甚至以为有缓存... 百思不得其解. 还好 leon 发现我在当前这个对象中有一个同名的变量名... 这个太恶心了!

{% highlight javascript %}
function isOpen () {
  return this.isOpen; // 这个是错误的原因: 两个 isOpen...
}

function isOpen () {
  return this.opened; // 这样就没事了!
}
{% endhighlight %}
