---
title: "send to fanfou&twitter together"
date: 2008-06-15
tags:
---

power by ruby language:

{% codeblock lang:ruby %}
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
{% endcodeblock %}

suggest to run on linux(unix or mac) bash!
