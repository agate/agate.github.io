---
title: "rails 5 行应用的启示"
date: 2008-09-06
tags:
---

这两天脑袋瓜有爆炸了~ 好久没有体会到刚刚学 J2EE 时候的那种兴奋和冲进了! 是 rails 给了我重生一样的感觉! 不可否认, 我是一个喜新的人! 我对新技术的饥渴是我周围朋友深知的! 先是 rSpec 指引着的 BDD 然后是熟悉又陌生的 RESTFul, 这么大量的知识点让我既兴奋又喘不过气! 毕竟学 rails 开发是为了下一个项目的应用方向做准备的! 但是如此大量的知识我是否来得及学习和掌握, 最总要的是我能否将其用在未来这个项目上面是我最担心的~

今天在 China on rails 上面习惯性闲逛的时候特地搜了一下 RESTFul 的资源, 看到了一个五步建立一个基于 rails 的 TODO List 应用, 并不因为这个应用有多么强大, 主要的是从这个应用我看到了第一个完整的 rails RESTFul 应用例子!
<code>1. rails todo
2. cd todo
3. rake db:create:all
4. script/generate scaffold Todo title:string body:text done:boolean due:datetime
5. rake db:migrate
</code>
然后启动你的 rails 应用并访问 http://localhost:3000/todos 看看一个 RESTFul 的 rails 应用吧!

简简单单的5行命令构建的应用如此深刻地反应了 rails 在其开发中不变的 "灵活", "简单" 的宗旨, 更加坚定了俺 good good study, day day up! 的信心, 好! 下个项目必定 rails!
