--- 
layout: post
title: "javascript: window.location"
wordpress_id: 414
wordpress_url: http://www.agatezone.cn/code/?p=414
---
在 javascript 中常需要获取或者修改当前页面的地址
可以使用 window.location 这个对象

{% highlight javascript %}
window.location = {
  // attributes                                                                 
  hash:     //Sets or returns the URL from the hash sign (#)
  host:     //Sets or returns the hostname and port number of the current URL
  hostname: //Sets or returns the hostname of the current URL
  href:     //Sets or returns the entire URL
  pathname: //Sets or returns the path of the current URL
  port:     //Sets or returns the port number of the current URL
  protocol: //Sets or returns the protocol of the current URL
  search:   //Sets or returns the URL from the question mark (?)

  // methods
  assign():  //Loads a new document
  reload():  //Reloads the current document
  replace(): //Replaces the current document with a new one
}
{% endhighlight %}
