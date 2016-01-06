---
title: "DOM 元素的 innerHTML 只读问题"
date: 2009-10-29
tags:
---

今天在 chrome 下发现一个 innerHTML 调用的时候抛出 DOM Error 问题. 经过一番折腾之后发现是 webkit 对于某些 DOM 元素的 innerHTML 属性有只读保护机制. 但是 firefox 上面确没有这类问题.

经过 google 的一番查证之后, 发现这个不仅仅是 webkit 类浏览器的问题. 其实 ie 也是. msdn 文档如是说:
<blockquote>innerHTML:
The property is read/write for all objects except the following, for which it is read-only: COL, COLGROUP, FRAMESET, HEAD, HTML, STYLE, TABLE, TBODY, TFOOT, THEAD, TITLE, TR. The property has no default value.</blockquote>
说白了就是这几个特殊的 DOM 元素的 innerHTML 属性是只读的.

当当当当~ 经验值 +320.
