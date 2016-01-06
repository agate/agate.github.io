--- 
layout: post
title: "说说 Symbol 和 String 的暧昧关系"
wordpress_id: 78
wordpress_url: http://www.agatezone.cn/code/?p=78
---
从实用角度看，在一些场景下Symbol好过String只有两点：节省内存，表达简洁。
而把两者强制拆开，既有额外好处也带来不便。
好处是充分利用两者的不同进行差异处理，如上面举的异常处理/when的用法。
但不便之处也不少，因为很多情况下需要无区别化对待两者，rails中就大量采用了这种风格，使用者无须担心
attr_accessor :abc 和 attr_accessor 'abc'有什么区别，layout 'main'和layout :main有什么区别（当然，跟layout nil和layout false还是有区别的，一点机智和诡异)。

当用户传过的东东作为Hash的key时，两者的不同让人烦死。
比如，我在每个model里声明一些字段的默认值：
<code>class Person < ActiveRecord::Base
&nbsp;&nbsp;DEFAULTS = {
&nbsp;&nbsp;&nbsp;&nbsp;:age => 30
&nbsp;&nbsp;}
end</code>
在controller里
<code>class PersonController < ActiveController::Base
&nbsp;&nbsp;def create
&nbsp;&nbsp;&nbsp;&nbsp;person = Person.new(Person::DEFAULTS.merge(params[:person]))
&nbsp;&nbsp;&nbsp;&nbsp;person.save!
&nbsp;&nbsp;end
end</code>
请注意controller里的merge,假定页面没有传入params[:person][:age]，则新建的person的age取默认值30.
那么，当页面传了age参数为40呢？按理merge后age应该为40,事实却不总正确。因为params里的key都是以String存储的，而我的DEFAULTS的key是Symbol，则merge后的结果是
<code>{
&nbsp;&nbsp;:age => 30,
&nbsp;&nbsp;"age" => 40
}</code>
最终save!以哪个为准，天知道~

rails实现了名为HashWithIndifferentAccess的类（继承自Hash），就是为了解决这一问题。无论开发者传过来的是 String还是Symbol（作为key），它都会把预先统一转化成String进行存取，以实现无差别化对待。细心的人可能已察觉，既然params 里的内容都是以String作为Key,为啥还可以params[:person]这样访问，奥秘就是用了这个类。它的源码在 gems/activesupport-x.x.x/lib/active_support/core_ext/hash/indifferent_access.rb
所以，我上面的model要改成：
<code>class Person < ActiveRecord::Base
&nbsp;&nbsp;DEFAULTS = HashWithIndifferentAccess.new({
&nbsp;&nbsp;&nbsp;&nbsp;:age => 30
&nbsp;&nbsp;})
end</code>
即使有这个类，也让人呕吐不止。曾想对它简单封装，提供Hash#to_indiff，仍不满意，不过，注意这个差别并有意避免仍是当前能做到的。

ruby1.9已经把Symbol作为String的子类实现了，并去除了Symbol#to_int,虽然没有百分之百确定出现在 ruby2.0里，还好离解放不远，这样从语言角度两者的边界就更清晰了,"Goodbye, HashWithIndifferentAccess."
:symbol.is_a? String
<a href="http://redhanded.hobix.com/inspect/SymbolIs_aString.html">http://redhanded.hobix.com/inspect/SymbolIs_aString.html</a>

让人绝倒的理由之一：
<blockquote>Smalltalk’s symbols are a subclass of string. (He adds that this is his most motivating reason to do it.) </blockquote>
<strong>
<em>said by liusong1111 from javaeye!</em></strong>
