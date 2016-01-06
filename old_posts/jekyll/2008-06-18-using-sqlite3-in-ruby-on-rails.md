--- 
layout: post
title: "Using SQLite(3) in Ruby on Rails"
wordpress_id: 71
wordpress_url: http://www.agatezone.cn/code/?p=71
---
if you are using rails 2.0+. congratulations! your rails default db engine is sqlite3 and you don't need to do any other work. just type the command:
<code>$rails {your app name}</code>
if you are using rails 1.2.6 or older version. the sqlite3 is not the default db engine for the project. but you can use one command to create the sqlite3 base app.
<code>$rails {your app name} -d sqlite3</code>

ps. if you get the error when you runing the server. it maybe cause by the db engine. make sure you have install the sqlite3-ruby gem. 
<code>$sudo gem install sqlite3-ruby</code>
