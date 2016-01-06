--- 
layout: post
title: "修正了 syntaxhighlighter-plus 的样式~"
wordpress_id: 147
wordpress_url: http://www.agatezone.cn/code/archives/147
---
老是觉得 syntaxhighlighter-plus 默认的样式和现在的模板不是很搭配, 就是觉得宽度稍微窄了点~ 就操刀小改了一下这个插件的样式表. 改动如下:
{% highlight css %}
.dp-highlighter {
	/* 修改 */
	width: 640px;
	/* 添加 */
	height: expression(this.scrollHeight > 320 ? "320px" : "auto");
	max-height: 320px;
	/* 注释 */
	/* overflow: auto; */
}
{% endhighlight %}
这样便达到刚好的宽度, 合适的高度. 这里要提及一下从中学了一招~ 就是 IE 不支持 css 的 max-height 属性, 但是支持自家的 expression 表达式! 所以可以如上进行 hack 得到和标准同样的效果! 这个方法学习自 <a href="http://perishablepress.com/press/2007/01/16/maximum-and-minimum-height-and-width-in-internet-explorer/" target="_blank">LINK</a>
