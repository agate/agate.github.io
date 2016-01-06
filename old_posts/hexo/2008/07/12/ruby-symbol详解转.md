---
title: "ruby symbol详解[转]"
date: 2008-07-12
tags:
---

<p><strong>起因</strong><br />
最近在学习ruby on rails，的确是一个优秀的数据库开发框架。但在过程中，发现在视图文件夹中的rhtml文件里有大量的类似于以下的语句：</p>
<td><%= link_to recipe.title, :action => "show", :id => 1 %></td>
<p>这是一个指向链接，如果没有冒号这句话的意思很好理解：这是一个指向http://127.0.0.1:3000/recipe/show/1的连接，也就是“显示”数据库表recipe中“id”为1的条目的信息，但让人不解的是action和id前面的冒号，它们是干甚么用的？</p>
<p><strong>ruby面向对象特性的一个缺点</strong><br />
ruby中，一切皆是对象。就一个简单的字符串举例：<br />
ruby -e 'puts "hello world".class'<br />
String<br />
这里打印了"hello world"的字符串所属的类，结果显示它是一个String对象的实例。我们还可以显示它的对象号。<br />
ruby -e 'puts "hello world".object_id'<br />
41436168<br />
ruby一向标榜自己是完全的面向对象的原因就在于此，它的确做的很彻底。但是凡事有好就有坏，一个对象占用的内存空间显然会比纯粹的变量大得多，当程序中涉及到大量的字符串时，一个ruby程序会占用过多的内存。举个例子说：<br />
我们用hash列表来存储歌曲的信息<br />
song1 = { 'title' => 'used to love you', 'artist' => 'john legend'}<br />
song2 = { 'title' => 'i still', 'artist' => 'backstreet boys'}<br />
#......<br />
#很多歌，这里只用两首<br />
for i in 1..2<br />
 thesong="song"+i.to_s<br />
 eval <<-PROC<br />
 #{thesong}.each_key { |key| puts key.object_id.to_s }<br />
 PROC<br />
end<br />
结果：<br />
41436144<br />
41436408<br />
41435904<br />
41436000<br />
因为object_id各不相同，在hash表中的各个key都是独立的String对象，即使内容相同（如'title'），ruby还是将其视为不同的对象，这样就无端地占用了不少内存。但事实上，大多数情况下，我们仅将hash中的key视为字段而已，不会涉及到String类的方法，ruby自动将其设置为对象有杀鸡用牛刀之嫌。</p>
<p><strong>symbol是什么</strong><br />
直译来说就是“符号”，在ruby就是形如:action这样的，一个冒号后跟一段字符串。显然，根据“一切都是对象”定律，它也是一个对象。<br />
ruby -e ' puts :action.class '<br />
Symbol<br />
这个对象存在的意义在于，它解决了“同内容字符串，不同对象”带来的过多占用内存的问题。简单的说:action代表了'action'字符串，这里说的是字符串，不是字符串对象。<br />
ruby -e ' puts :action '<br />
action<br />
更确切的讲就是一个symbol对象代表该对象的冒号后的字符串。<br />
ruby -e ' puts :action '<br />
action<br />
ruby -e ' puts :"hello world" '<br />
hello world<br />
所有同内容的字符串只需要一个标记对象就可以代替，这样减少了不必要的对象建立和内存占用。但是，正如我强调的“symbol代表的是字符串，不是对象”，因此不要希望标记可以使用String类的诸如capitalize，center等方法，如果使用的话只会得到提示方法未定义的错误报告：<br />
ruby -e ' puts :action.capitalize '<br />
-e:1: undefined method 'capitalize' for :action:Symbol' (NoMethodError)<br />
幸运的是，symbol提供了转换函数to_s用来生成一个字符串对象，它会提取字符串内容并将其升级为对象。<br />
ruby -e ' puts :action.to_s.capitalize '<br />
Action<br />
另外，很重要的一点是，symbol没有赋值方法，换句话说symbol一旦定义，将不能改变。<br />
ruby -e ' :action="hello" '<br />
syntax error<br />
很遗憾，即使使用了to_s，赋值依然无法顺利进行，因为ruby会认为“to_s=”是一个未定义函数。除非明确地为被转换生成的字符串对象指定一个引用（但事实上在复制之后该连接的指向又发生了变化）：<br />
:action<br />
myaction=:action.to_s<br />
myaction="lala"<br />
puts myaction<br />
结果：<br />
lala</p>
<p><strong>怎么使用symbol</strong><br />
任何可以使用symbol的地方都可以使用与之向对应的字符串对象。在rails中有建立类似javabean的方法：<br />
attr_reader :action<br />
它建立了一个读取实例变量@action的方法，也可以写成这样：<br />
attr_reader "action"<br />
反之，只要<br />
字符串在程序运行过程中不用改变<br />
字符串不必使用String类方法<br />
那么我们可以放心用symbol来代替字符串对象，从而大大减少内存的占用，在rails中尤为明显。因为需要频繁地在各个控制方法和页面之间跳转和传出数据，大量的方法名由symbol来代替，及节约了内存也提高了运行速度。</p>
