---
title: "注意 jQuery 中的多重事件绑定"
date: 2009-01-10
tags:
---

一直以来都是简单地使用 w3c 的 dom 模式的 javascript 编程模式. 直到最近才开始使用 jquery. 也是由此发现其的强大! 在这里感叹一下: "这东西他妈太好了! 不过开始有依赖性了!!!"

言归正传, 在开发的过程中发现了一个小特点, 需要注意一下: 就是 jquery 的事件绑定机制是累加式的, 说白了就是可以重复注册事件的处理方式, 并在事件触发的时候统统执行. 明显, 这个是有好处的. 我们担心不必在大型前端的 javascript 脚本中覆盖我们原先的事件注册. 但是常常我们也遇到一个事件多次被执行的问题(其实就是某些情况下我们的时间注册了多次.)

在 dom scripting 中我们常常这么注册事件:
HTML:
<code>&lt;p id="clickable"&gt;click me!&lt;p&gt;</code>
JAVASCRIPT:
<code>document.getElementById("clickable").onclick = function () { alert(1); };
document.getElementById("clickable").onclick = function () { alert(2); };</code>
测试点击这个段落, 只会有一次 alert 并且内容为 2 (即最后一次注册的);

但是在 jquery 中我们这样:
HTML:
<code>&lt;p id="clickable"&gt;click me!&lt;p&gt;</code>
JAVASCRIPT:
<code>$('#clickable').onclick(function () { alert(1); });
$('#clickable').onclick(function () { alert(2); });</code>
测试点击这个段落, 两次 alert 都会出现.

所以如果需要只有一个事件绑定的话可以使用 jquery 自带的 unbind 方法来解除指定时间的所有绑定执行代码. 例如:
<code>$('#clickable').unbind('onclick');</code>
这样就解除了 onclick 的所有绑定方法.
(ps. jquery 中 jqObj.event(function) 相当于 jqObj.bind('event', function))

这个问题在开发中需要注意!
