--- 
layout: post
title: "Rails, MySQL的utf8中文乱码问题"
wordpress_id: 80
wordpress_url: http://www.agatezone.cn/code/?p=80
---
在 win 下的试验... 似乎 rails 不是使用 utf8 的编码方式才导致了乱码. 解决方案十分简单. 当然, 请保证 mysql 的字符集使用 utf8 并且建立库/表也是 utf8 的编码.

最重要的是在 rails 工程中的 application.rb 中加入如下代码:
{% highlight ruby %}
# application.rb
  before_filter :set_charset
  before_filter :configure_charsets

  def set_charset
    @headers["Content-Type"] = "text/html; charset=utf-8"
  end

  def configure_charsets
    @response.headers["Content-Type"] = "text/html; charset=utf-8"
    suppress(ActiveRecord::StatementInvalid) do
      ActiveRecord::Base.connection.execute 'SET NAMES UTF8'
    end
  end
{% endhighlight %}
看看~是不是搞定了！
