---
title: "javascript 数组使用备忘"
date: 2008-12-23
tags:
---

在 javascript 中使用数组(哈希表)有很多小技巧(因为其是动态语言的缘故, 要比 java 灵活很多), 虽然基础了点, 但是还是想记录下来以备日后查阅:

<b>基本特性</b>
javascript 的数组不需要事先定义长度用时只要定义好数组的类型即可直接使用. 例如
{% codeblock lang:javascript %}
var arr = []; // arr = new Array();
arr[1] = 111; // arr = [,1];
// 当然, hash 也是如此 hash = {}; 一样可以!
{% endcodeblock %}

<b>常用方法</b>
<em>push & pop</em>
作为数组实现栈数据结构的方法组合. push 把给定参数加载数组最后, pop 则对应取出数组的最后一个元素.(改变数组本身)

<em>push & shift</em>
最为数组实现队数据结构的方法组合. shift 取出数组的第一个元素.(改变数组本身)

<em>unshift</em>
插入给定参数到数组之前. 比如 [2,3].unshift(0,1) => [0,1,2,3]

<em>join</em>
就是和 ruby 里头的 join 一样, 使用给定参数连接每个数组元素(方便处理最后一个连接, 而且效率很快). 例如
{% codeblock lang:javascript %}
['CCTV', 'SMG', 'MTV'].join(', ') => 'CCTV, SMG, MTV'
{% endcodeblock %}

<em>sort & reverse</em>
对应的两种排序方式, sort 为从小到达, reverse 为从大到小.

<em>slice & splice</em>
对应的两种数组截取方式. slice 只是截取出数组的某个区间段并输出(其不改变数组本身), splice 截取了某个区间段并替换成给定参数(没有给定参数就等于直接删除这个区间, 当然会改变数组本身). 例如
{% codeblock lang:javascript %}
arr      = [1,2,3,4,5]
arr_temp = arr.slice(2,4) // arr_temp = [3,4] & arr = [1,2,3,4,5]
arr.splice(2,4,0) // arr = [1,2,0]
// 注意了 slice(m,n) 是取出 [m,n)
// splice(m,n,...) 是替换 [m,n]
{% endcodeblock %}

<b>总结</b>
其实呢~ javascript 是一个很奇特的脚本语言, 其中所有的东西都是变量/hash/数组, 而且只要声明了类型就可以直接使用, 不用担心什么越界之类的.
