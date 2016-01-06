---
title: "再说 ruby 天气插件 --- weatherman"
date: 2008-10-09
tags:
---
 weatherman"
wordpress_id: 241
wordpress_url: http://www.agatezone.cn/code/?p=241
---
之前说了一个十分好用的 ruby 天气插件 rweather. "<a href="http://www.agatezone.cn/code/archives/234">r_weather! ruby 中获取天气的 API</a>".

但是这个 rweather 插件有一个缺点, 就是它太简陋了! 只能获取当前天气状态, 而恰恰在这仅有的当前状态中却没有最高温度和最低温度, 只有当前温度以及外国人常用的感觉温度. 这个只能是小用用, 真正做个天气功能模块还是比较不足的!

又去 github 上面转了转, 看了很多 weather 的插件. 其中有两款让我十分喜爱, 一个是小日本写的 <a href="http://github.com/keita/ruby-weatherhacks/tree/master">ruby-weatherhacks</a> 和一个叫做 <a href="http://github.com/jdpace/weatherman/tree/master">weatherman</a> 的天气插件. 两者都有十分详细的信息获取. 当然小日本那个是日语的服务器, so... 我们还是用 weatherman 吧!

weatherman 这个插件使用方式几乎和 rweather 一样!(都是通过 weather.com 请求信息). 更重要的是, weatherman 可以获取 '当前', '当日', '3天', '周五' 等多种多样的信息格式! 具体的查看 README 文件就十分明白了!
