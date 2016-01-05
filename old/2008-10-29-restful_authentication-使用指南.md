--- 
layout: post
title: "restful_authentication 使用指南"
wordpress_id: 273
wordpress_url: http://www.agatezone.cn/code/?p=273
---
很早就在 "Web 开发大全 -- Ruby on Rails 版" 书中看到过 restful_authentication 这个鉴定插件了~ 但是一直都没使用过. 今天看到一个中文的 ROR 视频网站 -- rubycnrails.cn 上面用视频介绍了 restful_authentication 这个插件的使用(但是这位仁兄老是出错... 看着我好着急阿!) 呵呵! 于是我也试着使用了一番, 发现真的满好用的. 这里就记录一下, 顺便说一下需要注意的地方.

github 地址 <a href="http://github.com/technoweenie/restful-authentication/tree/master">http://github.com/technoweenie/restful-authentication/tree/master</a>
(rubycnrails.cn 上面那个视频似乎是使用旧的版本... 大概不知道这个插件已经迁移到 github 上面了吧.)

<strong>安装:</strong>
<code>$cd [your-rails-app]
$./script/plugin install git://github.com/technoweenie/restful-authentication.git</code>

<strong>使用:</strong>
<code>$./script/generate authenticated <strong>Model-Name</strong> <em>[Controller-Name]</em></code>
别忘了 rake 一下, 来建立你的数据库!

<strong>结果:</strong>
生成对应的 controller / model / view. 添加了对应的 routes: signup / login / logout. 当然, 还添加了
<blockquote>lib/authenticated_system.rb
lib/authenticated_test_helper.rb</blockquote>
这两个才是重要的插件功能! 其中 AuthenticatedSystem 中包含了诸如: logged_in?, current_kid 等重要方法! 到时候我们只需要在需要调用的 controller 中 include AuthenticatedSystem 就好了.

<strong>注意:</strong>
不要傻乎乎地学 README 中键入: ./script/generate authenticated user session<strong>s</strong> 这个 s 最好不要!(不要说我违反了 RESTful 的理念, 我说的是最好不要!) 对于初学者来说先别加这个 s, 因为这个会带来很多配置上的模糊: 比如 routes.rb 中 resource 是定义为 'session', 但是设置具体命名路由的时候使用 controller 参数时又要设置为 'sessions'. 所以, 如果你对这里头的细节不是很清楚的话, 建议你改用单数作为这里控制器的名称:
<code>$./script/generate authenticated user session 我建议这么写</code>
当然! 你清除的话, 或者你不关心这个的话, 那还是写上那个 s 吧! 这样才够 RESTful!
其他很细致的内容还是看看源代码或者看看 Plugin 的 README 吧! 写得很不错!
