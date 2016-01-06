---
title: "javascript 中 hash 或者 object 结构的迭代"
date: 2008-12-25
tags:
---

javascript 中的 objcet 很特别, 说白了还是一个 hash, 今天突然需要便利所有 hash 中的 keys. 所以就查阅了一下其迭代的方法:
{% codeblock lang:javascript %}
for (var key in hash) {
  // key is just what you need
  // you can get the value by hash['key']
}
{% endcodeblock %}
更多 javascript 的 hash 实现方式可以参阅 <a href="http://www.mojavelinux.com/articles/javascript_hashes.html">Hash Tables in Javascript</a>
