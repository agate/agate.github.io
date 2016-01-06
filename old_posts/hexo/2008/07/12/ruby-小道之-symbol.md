---
title: "Ruby 小道之 Symbol"
date: 2008-07-12
tags:
---

在Ruby中symbol是Symbol类的实例。symbol的语法为一个冒号后面接一个标识符。

symbol就像一个字符串，它表示了一个字符序列。它不像字符串，每个symbol只有一个实例(和Fixnum一样)。因此，有一个内存或
性能问题需要弄清楚。例如，在下面的代码中，"foo"字符串以三个单独的对象存储在内存中，但是symbol :foo作为一个单独的对
象存储(被引用了多次):
<code>array = ["foo", "foo", "foo", :foo, :foo, :foo]</code>
有些人被symbol前面的冒号弄糊涂了。其实没有必要糊涂；这只是一个简单的语法形式。字符串，数组和哈希都有开始和结束界定
符；而symbol只有一个开始界定符。把它当成一个单界定符而不是二元界定符即可。开始时你可能认为这个语法很奇怪，但事实上
没有什么神秘的。
<!--more-->
值得注意的是在老版本的Ruby(1.6之前)中，symbol常量不是第一类对象而是转换成Fixnum来存储。现在在内核中这仍然是对的；
symbol对应于一个数字并作为一个immediate value来存储。这个值可以使用to_i来得到，但是没有必要。

根据Jim Weirich，symbol是"有名字的对象"。Austin Ziegler更喜欢说"an object that is a name"。无论怎样，在symbol和名字
间始终有一个一对一的对应。什么样的东西我们需要使用名字？例如变量，方法和任意的常量。

一个常见的symbol使用场景是表示变量或方法的名字。例如，我们知道如果我们想添加一个读/写属性到类中，我们可以这样做:
<code>class SomeClass
&nbsp;&nbsp;attr_accessor :whatever
end</code>
这等价于:
<code>class SomeClass
&nbsp;&nbsp;def whatever
&nbsp;&nbsp;&nbsp;&nbsp;@whatever
&nbsp;&nbsp;end
&nbsp;&nbsp;def whatever=(val)
&nbsp;&nbsp;&nbsp;&nbsp;@whatever = val
&nbsp;&nbsp;end
end</code>
换句话说，:whatever这个symbol告诉attr_accessor方法"getter"和"setter(以及实例变量)都将根据该symbol来给予名字。

你可能想问为什么我们不能使用一个字符串来替代。我们可以。大部分希望使用symbol的核心方法都可以使用字符串来替代。
<code>attr_reader :alpha
attr_reader "beta"   # This is also legal</code>
事实上，symbol就"像"一个字符串，它对应于一个字符序列。这导致有些人说"a symbol is just an immutalbe string"。
但是，Symbol类并不是继承于String，并且对于字符串典型的操作并不适合symbol。

另一个误解是认为symbol没必要直接对应于标识符。这导致有些人说"the symbol table"(as they would in referring to
an assembled object program)。但是这不是一个真正有用的概念；尽管在内部symbol存储在一种table里，Ruby并没有将
这个table作为一个实体暴露给我们访问，而我们作为编程者也不关心它的存在。

而且，symbol不需要看起来像标识符。虽然它们像标识符，但是它们也可以包含标点，如果它们被引号包围的话。如下也是
合法的Ruby symbol:
<code>sym1 = :"This is a symbol"
sym2 = :"This is, too1"
sym3 = :")(*&^%$"             # and even this</code>
你甚至可以使用这些symbol来定义实例变量和方法，但是这样的话你需要send和instance_variable_get技术来引用它们。
一般来说不推荐使用字符串形式的symbol。

<strong>Symbols As Enumerations</strong>
Pascal以及后期版本的C等语言有一个enumerated type的概念。Ruby没有这样的东西；Ruby没有类型检查。但是symbol
非常有用；我可以用:north，:south，:east和:west来表示方向。

将这些symbol存储为常量可能更清晰。
<code>North, South, East, West = :north, :south, :east, :west</code>
如果它们是字符串而不是symbol，将它们定义为常量会节省内存，但无论如何每个symbol都只在对象空间里存在一次。
(像Fixnum一样Symbol存储为immediate value)

<strong>Symbols As Metavalues</strong>
我们经常使用异常来作为避免返回代码的方式。但是如果你宁愿使用返回代码的话也可以。RUby的方法不限于单返回类型，
这让传回"out of band"值成为可能。

我们经常需要这样的值。ASCII NUL字符被认为根本就不是一个字符。C有NULL指针，Pascal有nil指针，SQL有NULL等等。
Ruby当然也有nil。

这些metavalue的问题是它们成为合法的值。现在每个人都认为NUL是一个ASCII字符。在Ruby中，nil不是真的non-object；
它可以被存储和操作。这样我们有了如hash[key]返回nil这样的小烦恼；是因为key没有找到而返回nil，还是由于这个key
真的指向nil?

这里symbol可以用来作为好的metavalue。假设一个方法从忘了攫取一个字符串(可能通过http或其他类似的东西)。我们可以
返回非字符串值来表示出现异常。
<code>str = get_string
case str
&nbsp;&nbsp;when String
&nbsp;&nbsp;&nbsp;&nbsp;# Proceed normally
&nbsp;&nbsp;when :eof
&nbsp;&nbsp;&nbsp;&nbsp;# end of file, socket closed, whatever
&nbsp;&nbsp;when :error
&nbsp;&nbsp;&nbsp;&nbsp;# I/O or network error
&nbsp;&nbsp;when :timeout
&nbsp;&nbsp;&nbsp;&nbsp;# didn't get a reply
end</code>
这比使用异常更好或更清晰?没必要。但是记住，这是处理可能为"edge cases"但不一定是异常的条件时的一项技术。

<strong>Symbols, Variables, and Methods</strong>
可能使用symbol的最知名的地方是定义类的属性:
<code>class MyClass
&nbsp;&nbsp;attr_reader :alpha, :beta
&nbsp;&nbsp;attr_writer :gamma, :delta
&nbsp;&nbsp;attr_accessor :epsilon
&nbsp;&nbsp;# ...
end</code>
attr_accessor使用symbol名字来觉得实例变量和读写方法的名字。这不代表symbol和实例变量名之间有绝对的关系。
例如，如果你使用instance_variable_set，我们必须指定变量的名字，包括@符号:
<code>sym1 = :@foo
sym2 = :foo
instance_variable_set(sym1, "str")   # Works
instance_variable_set(sym2, "str")   # errors</code>
简短来说，传递到attr系列方法的symbol只是一个参数，这些方法基于symbol的值创建需要的实例变量和方法。(writer方法
在结尾有一个=，而实例变量名字在前面有一个@。)换句话说，symbol必须与它引用的标识符相对应。

大部分情况下，希望使用symbol的方法也可以使用字符串。相反则不一定正确。

<strong>Converting to/from Symbols</strong>
字符串和symbol可以使用to_s和to_sym方法自由互换:
<code>a = "foobar"
b = :foobar
a == b.to_s   # true
b == a.to_sym   # true</code>
如果你做元编程，如下方法有时候可能很有用。
<code>class Symbol
&nbsp;&nbsp;def +(other)
&nbsp;&nbsp;&nbsp;&nbsp;(self.to_s + other.to_s).to_sym
&nbsp;&nbsp;end
end</code>
上面的方法允许我们连接symbol(或者添加字符串到一个symbol)。下面是一个使用它的例子；这段微小的代码接收一个symbol并
尝试告诉我们它是否是一个accessor(即，读写方法都存在):
<code>class Object
&nbsp;&nbsp;def accessor?(sym)
&nbsp;&nbsp;&nbsp;&nbsp;return (self.respond_to?(sym) and self.respond_to?(sym+"="))
&nbsp;&nbsp;end
end</code>
我这里要提到一个使用symbol的聪明的方式。当我们做map操作时，有时候一个复杂的block可能附加在后面。但是许多情况下，
我们对每个元素简单的调用一个方法:
<code>list = words.map { |x| x.capitalize }</code>
在这里，似乎我们为完成工作做了太多事情。让我们打开Symbol类并定义to_proc方法。这保证任何symbol都可以强制转换成
一个proc对象。但是我们应该返回什么proc?显然应该根据对象context里的symbol本身。换句话说，proc应该将symbol本身作
为一个消息发送给对象。
<code>def to_proc
&nbsp;&nbsp;proc { |obj, *args| obj.send(self, *args) }
end</code>
顺便提一下，这段代码来自Gavin Sinclair的"Ruby Extensions"对象。有了这个方法，我们可以重写上面的代码:
<code>list = words.map(&:capitalize)</code>
值得花费一分钟来理解它怎样工作。map方法使用一个block作为参数。&符号允许我们传递一个proc而不是一个显式附加的
block。由于我们在一个非proc对象上使用&符号，解释器会尝试调用该对象的to_proc方法。返回的proc替代了显式的block，
map将会对每个元素调用它。为什么self作为一个消息传递给array元素有意义呢?这是因为proc是一个闭包，所以它会记住
它被创建在哪个context里。当它被创建时，self表示调用to_proc的symbol。 

<em><strong>转载自 javaeye 作者 hideto</strong></em>
