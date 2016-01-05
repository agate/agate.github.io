--- 
layout: post
title: "Get current controller and action name"
wordpress_id: 103
wordpress_url: http://www.agatezone.cn/code/?p=103
---
if you want to get the current controller and action's name, you can use this way:
<code><span style="color: #339966;"># in controller class file, you can use</span>
self.class.controller_path <span style="color: #339966;"># to get the current controller name</span>
<span style="color: #339966;"># and use</span>
self.action_name                      <span style="color: #339966;"># to get the current action name</span></code>
