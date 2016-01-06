--- 
layout: post
title: "Law of Demeter"
wordpress_id: 501
wordpress_url: http://www.agatezone.cn/code/?p=501
---
一直被 Jeff 提醒需要遵循 Law of Demeter. 也一直只是一个大概的概念. 似乎就是不要访问过深的方法链.

今天看 wujiang 借我的 < 程序员修炼之道>. 发现里头有一节说 "德墨忒耳法则" 顺便 google 了一下发现原来就是 Law of Demeter. 这里记录一下:

{% highlight ruby %}
# 函数的德墨忒耳法则规定, 某个对象的任何方法都应该只调用属于以下情形的方法:
class Demeter
  def initialize(args)
    @array = [1,2,3]
  end
  
  def funA
    #TODO
  end
  
  def example (obj)
    result = funA()          # 它自身
    obj.do()                 # 传入该方法的任何参数
    hash   = Hash.new        # 它创建的任何对象
    puts @array.join(' ,')   # 任何直接持有的组件对象
  end
end
{% endhighlight %}

更多参考: <a href="http://en.wikipedia.org/wiki/Law_of_Demeter">http://en.wikipedia.org/wiki/Law_of_Demeter</a>
