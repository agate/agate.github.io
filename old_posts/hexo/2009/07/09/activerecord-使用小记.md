---
title: "ActiveRecord: 使用小记"
date: 2009-07-09
tags:
---

今天为修一个 bug 到 ActiveRecord 模型层逛了一圈, 学了 2 个知识点.
1. Model 中的 belongs_to 和 has_many 如果指定了 :class_name 注意一定要写完整噢. 比如一个 Reply 类的完整类名是 Post::Reply 的话, 记得写这个完整的名字. 不要只写 Reply
{% codeblock lang:ruby %}
has_many :replies,
         :class_name => 'Post::Reply'
{% endcodeblock %}

2. 在 find 的时候 :order 参数中如果是根据别的对象的某个属性来排序的, 记得用 "表名.属性名", <strong>注意不是</strong> <del datetime="2009-07-09T06:09:43+00:00">"类名(对象名).属性名"</del>

举个例子:
环境: 有一个 Post 类, 一个 User 类, 一个 User 有多个 Post, 一个 Post 对应一个 User.
需求: 找出所有的 Post 并且根据其对应的 User 的 name 排序.
方法:
{% codeblock lang:ruby %}
Post.find :all,
          :include => :user, #这里 :user 其实就是在 Post 类中 belongs_to 写的那个 symbol
          :order   => 'users.name' #这里 users 是表名
{% endcodeblock %}

还有就是谢谢 wujiang 在我面前一步一步调试. 让我学了挺多的!

================================================================

补充一下, 昨天发现 belongs_to 和 has_many 这种写法还不一定好使. 原因在于这样写还不够 <strong>"绝对"</strong>. 聪明的可能恍然大悟 --> <em><strong>::Post::Reply</strong></em> 才是正解.
