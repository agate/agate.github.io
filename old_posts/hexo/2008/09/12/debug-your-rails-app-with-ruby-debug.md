---
title: "Debug Your Rails App With ruby-debug"
date: 2008-09-12
tags:
---

<strong>first</strong>, install the ruby-debug
<code>$ sudo gem install ruby-debug -y</code>
<strong>second</strong>, add require into your *.rb files and run it
<code>require "ruby-debug"</code>
<blockquote>when rails web server running. the runtime control file is "config/environments/{env-name}.rb". {env-name} is what depend on the server run's condition. generally we use development env in our develop. so add the "require" into the development.rb</blockquote>
<strong>third</strong>, add the keyword: "debugger" to make a break-point.

info: <a href="http://www.sitepoint.com/article/debug-rails-app-ruby-debug">link</a>
