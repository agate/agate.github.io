--- 
layout: post
title: "swap your Escape and CapsLock keys for VIM"
wordpress_id: 313
wordpress_url: http://www.agatezone.cn/code/?p=313
---
i feel uncomfortable while i using vim and having to move way up to reach Escape key. so i swaped the Escape and CapsLock keys by under steps:

first, open your terminal. and type:
<code>$vim ~/.xmodmap</code>

second, add under statements into ./xmodmap file.
<code>remove Lock = Caps_Lock
keysym Caps_Lock = Escape
keysym Escape = Caps_Lock
add Lock = Caps_Lock</code>

last, restart your X env.
(maybe you can use CTRL + ALT + BackSpace)

after these configurations, i found it's easier than move way up to reach Esc while using vim.

ps. thanks forrest, thanks leon! i found i fell in love with vim!!! it's really powerful!
