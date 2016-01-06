--- 
layout: post
title: "html: label 原来可以用作容器使用哦"
wordpress_id: 428
wordpress_url: http://www.agatezone.cn/code/?p=428
---
过去一直以为 label 标签中的 for 属性是关键. 只有指定了对应的 id 给 for 属性, 才能让 label 起作用. 但是最近看到一种写法:

{% highlight html %}
<label>
  <input type="checkbox" />
  check it
</label>
<!-- 其实只要把你那个对应的元素包含在 label 中就可以了 -->
{% endhighlight %}

这样你点击文本 "check it" 就和点击那个 checkbox 的效果是一样的了.
(P.S. 当然咯 如果 label 和 目标元素 距离很远, 那还是用 id 属性指定为好.)
