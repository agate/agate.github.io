--- 
layout: post
title: "rails 中 validates 显示自定义消息"
wordpress_id: 346
wordpress_url: http://www.agatezone.cn/code/?p=346
---
默认情况下我们使用 rails 默认的 validates 来进行模型数据验证工作的时候常常会加上 message 参数来自定义我们的错误提示.

{% highlight ruby %}
validates_presence_of :name, :message => 'is blank...'
{% endhighlight %}

出错的时候会提示
<blockquote>Name is blank...</blockquote>
但是要是我想显示
<blockquote>The name field is blank!</blockquote>
单靠改 message 的内容看来是不行的. 在 google 一番之后发现 ActiveRecord::Errors 这个类中有一个叫做 full_messages 的 helper function. 就是完成把出错的 field 的名字添加到 message 内容的前面的工作. 所以可以 override 一番. 就可以实现我们的功能了. 但是也许不小心会破坏过去的代码. 所以这里推荐一个插件( 由 rails 核心成员写的. )
<a href="http://wiki.rubyonrails.org/rails/pages/Custom+Error+Message">Custom Error Message</a>
其实十分简单, 它也是 override 了那个 helper function. 如果你不喜欢加插件的话自己在 lib 下面建立一个 ruby 文件就好了, 这里也顺便贴一下代码.

{% highlight ruby %}
def full_messages
  full_messages = []

  @errors.each_key do |attr|
    @errors[attr].each do |msg|
    next if msg.nil?

      if attr == "base"
        full_messages << msg
      elsif msg =~ /^\^/
        full_messages << msg[1..-1]
      elsif msg.is_a? Proc
        full_messages << msg.call(@base)
      else
        full_messages << @base.class.human_attribute_name(attr) + " " + msg
      end
    end
  end

  return full_messages
end
{% endhighlight %}

<strong>使用方式:</strong>
在你需要自定义消息的前面加上 '^' 这个符号.(说白了就是很想正则告诉代码这是开始)

{% highlight ruby %}
validates_presence_of :name, :message => '^The name field is blank!'
{% endhighlight %}

这样出错后就会显示:
<blockquote>The name field is blank!</blockquote>
