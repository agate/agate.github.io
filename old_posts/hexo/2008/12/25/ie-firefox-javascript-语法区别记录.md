---
title: "IE & Firefox javascript 语法区别记录"
date: 2008-12-25
tags:
---

随着 IE 不断升级, 其也越来越规范化. 渐渐地和大多数浏览器也越来越表现一致化了~ 但是还是有一些不同. 这里就记录一下我所碰到的 IE 和 Firefox 解析 javascript 时候的语法区别:

<strong>1. 结尾逗号问题</strong>
[ 1, 2, 3 ]
{ a:1, b:2, c:3 }
一个 array 一个 hash 都是我们在 javascript 中常见的数据结构. 但是在 Firefox 中是可以在最后一个元素后面继续加入逗号的, 例如
[ 1, 2, 3, ]
{ a:1, b:2, c:3, }
但是 IE 就比较严格, 不可这么写, 必须去掉最后一个空格.
( PS 这点上我觉得 IE 比较规范... )

<strong>2. for 关键字</strong>
这里不是说循环, 而是说 hash 的赋值方式. 当我们的一个 hash 有一个 key 名字叫做 for 的话, 在 Firefox 中我们可以这么写:
hash.for = xxx  OR xxx = hash.for OR hash['for'] = xxx OR xxx = hash['for']
但是很可惜, IE 中这样就会出错! 有可能其把 for 当作是关键字了或者什么其他特性( 不清楚 ), 总之 IE 中只能写成:
hash['for'] = xxx OR xxx = hash['for']

<strong>3. debugger 关键字</strong>
同 2 关键字. 一样的, debugger 在 ie 中也是一个关键字. 具体原因不知, 可能是俺装了 iedebugger 导致的. 总之最好改成其他名字, 或者使用 ['debugger']

[ updating ]
