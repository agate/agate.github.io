---
title: "让ruby正确处理中文长度"
date: 2008-06-19
tags:
---

ruby 对非西欧字符采用 utf8 编码，但是一个中文字符使用 String#length or String#size 就会得到 3 个字符的结果。是因为中文变成了 \xxx\xxx\xxx 的形式，就比如 "睡觉" -> "\347\235\241\350\247\211"。要是出现中英文混合的字符串统计字数就麻烦咯～这里给出一个简单的解决方安：使用 "jcode" 库
{% codeblock lang:ruby %}
irb(main):001:0> str = "睡觉ing"
=> "\347\235\241\350\247\211ing"
irb(main):002:0> str.length
=> 9
irb(main):003:0> $KCODE='utf8'
=> "utf8"
irb(main):004:0> require 'jcode'
=> true
irb(main):005:0> str.jlength
=> 5
{% endcodeblock %}
