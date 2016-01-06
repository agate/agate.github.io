---
title: "ruby core 'obj.send' and 'eval'"
date: 2008-12-22
tags:
---

<strong>Eval</strong>
以 string 的格式执行 ruby 表达式. 比如
<code>eval "str = %{helloworld}"</code>
就会创建一个 str 变量, 其值为 "helloworld"

<strong>obj.send</strong>
调用 obj 中的方法以 symbol 的形式. 比如
<code>class User
&nbsp;&nbsp;def say(str)
&nbsp;&nbsp;&nbsp;&nbsp;"user says: #{str}"
&nbsp;&nbsp;end
end
u = User.new
u.send :say, 'i am a boy~' #=&gt; "user says: i am a boy~"</code>
如果这个 obj 中有方法覆盖了 send 方法, 那么我们可以使用 __send__ 来代替 send 方法
