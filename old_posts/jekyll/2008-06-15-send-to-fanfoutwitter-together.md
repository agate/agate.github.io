--- 
layout: post
title: "send to fanfou&twitter together"
wordpress_id: 67
wordpress_url: http://www.agatezone.cn/code/?p=67
---
power by ruby language:

{% highlight ruby %}
require "net/http"

module SmallBlogSender
  def SmallBlogSender.send(username, password, web_server, message, param_name="status")
    url = URI.parse(web_server)
    req = Net::HTTP::Post.new(url.path)
    req.basic_auth username, password
    req.set_form_data({param_name => message}, ';')
    res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
    case res
    when Net::HTTPSuccess, Net::HTTPRedirection
      # OK
    else
      res.error!
    end
    return res
  end
  UPDATESERVERS = {
    "fanfou" => "http://api.fanfou.com/statuses/update.xml",
    "twitter" => "http://twitter.com/statuses/update.xml"
  }
end

puts "message:(less than 140 characters)"
message=gets
print "username: "
username=gets.delete("\n")
print "password: "
password=gets.delete("\n")
print "==== Now sending to Fanfou ===>"
response = SmallBlogSender.send(username, password, SmallBlogSender::UPDATESERVERS["fanfou"], message)
puts " OK." if response==Net::HTTPSuccess or Net::HTTPRedirection
print "==== Now sending to Twitter ===>"
response = SmallBlogSender.send(username, password, SmallBlogSender::UPDATESERVERS["twitter"], message)
puts " OK." if response==Net::HTTPSuccess or Net::HTTPRedirection
{% endhighlight %}

suggest to run on linux(unix or mac) bash!
