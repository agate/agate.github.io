---
title: "HTML: 当用户按下 Enter 的时候提交表单"
date: 2009-09-10
tags:
---

对这个问题今天作了一个跨浏览器的研究. 首先当一个 Form 中只有一个 Input 的时候, 例如:
{% codeblock lang:html %}
<form>
  <input type="text" name="name" value="name" />
</form>
{% endcodeblock %}
不管哪个浏览器都是可以通过 Enter 来提交当前表单的. 但是当 Form 中存在两个及两个以上 Input 的时候.

1. IE 和 Firefox
需要在 Form 中加入 type 为 submit 的 Input, 才能实现 Enter 提交. 例如:
{% codeblock lang:html %}
<form>
  <input type="text" name="name" value="name" />
  <input type="password" name="pwd" value="pwd" />
  <input type="submit" />
</form>
{% endcodeblock %}

2. Webkit 和 Opera
无论什么时候, 加不加 type 为 submit 的 Input 都可以直接 Enter 提交. 例如:
{% codeblock lang:html %}
<form>
  <input type="text" name="name" value="name" />
  <input type="password" name="pwd" value="pwd" />
</form>
{% endcodeblock %}
