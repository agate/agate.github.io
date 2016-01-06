---
title: "p6spy和sqlProfiler的配合使用让你的hibernate的show_sql更好用"
date: 2008-03-27
tags:
---

使用hibernate开发的朋友都知道，想在使用hibernate进行持久层操作的时候显示对应的sql语句，可以设置hibernate配置文件中的show_sql属性为true来实现这个需求。可是这个功能比较让人失望……他的语句是没错，但是参数值全是?这个带传入的参数符号，每个调试带来什么方便。

在这里，我介绍两个工具包来解决这个问题：[p6spy]和[sql_profiler]，具体主页地址在下列给出
p6spy: http://www.p6spy.com
SQL Profile: http://www.jahia.net/jahia/page597.html

我们先来说说p6spy这个工具。在我理解上，他其实就是一个中间驱动，在数据库调用端和实际数据库驱动间做一个代理人的角色，进而加入了一些特有的辅助功能。在这里我们使用的调用端就是hibernate这个数据持久层框架，而数据库驱动我们用的是mysql的默认驱动(一般就是com.mysql.jdbc.Driver)。好，解释完理论开始实际试验：
* 将p6syp.zip(可能是tar文件包)下载好
* 将包中的p6syp.jar包放入你工程的classpath下(web项目就丢到WEB-INF/lib中)
* 将包中的spy.properties放入src目录中
* 修改hibernate配置文件中的数据库驱动为com.p6spy.engine.spy.P6SpyDriver这个中间驱动
* 修改刚才拷贝进src中的spy.properties文件，将realdriver的值设置成原来hibernate中的真正驱动(这里我是com.mysql.jdbc.Driver)

<img src="http://pic.yupoo.com/skyforce/6045754ef71b/1dwgk2wv/1dwgk2wv.jpg" />

OK搞定！重新编译项目，以保证p6syp.jar和spy.properties编译进入目标地址。

接着就运行你的程序吧，看看控制台……(不要打我啊，我又没说控制台会有变化=.=)。但是看看你的工程根目录下是不是出现了spy.log，这里面就是你要的数据库操作历史，包括了真正传入的参数的具体值。

如果需要改变spy.log日志的生成地址，可以对应设置spy.properties文件的logfile属性给出绝对地址。(logfile默认是spy.log可以加上路径比如logfile = c:\xxx\xxx.log)

好了，似乎hibernate的?参数问题解决了，但是我的好多朋友都抱怨：“怎么这个log格式这么难懂啊！看着好不爽啊！”的确！p6syp的日志格式让人确实分外头大，于是乎介绍个SQL Profile来帮帮痛苦的大众。

照惯例，介绍介绍理论知识。SQL Profiler是一个基于p6syp的一个辅助包，可以实现很多功能，比如根据你的query来帮你生成合适的索引功能。在这里我们使用它的GUI控制介面，说白了就是一个监听器，在你通过p6spy进行数据库操作时，他就会很清晰地跟踪并列出你的操作，比单单查看那个恶心的spy.log来得舒服！既然基于p6syp当然也要用到p6syp.jar这个包咯，只是必须使用我们下载到的sqlprofiler.zip中的spy.properties来替换原来的项目中的那个文件，因为这个文件是定制过的，所谓的监听器也是靠这个文件才起作用的。好，废话说多了毕竟会烦，来说说具体步骤：
* 将下载好的sqlprofiler.zip包中的 sqlprofiler.jar 和spy.properties两个文件解压出来
* 使用新的spy.properties文件替换工程中原来的那个文件
* 根据刚才添加p6syp的过程，修改 spy.properties 文件的参数
* 使用 java -jar sqlprofiler.jar 命令启动sqlprofiler的GUI介面
* 再次启动你的应用吧，看看是不是在进行数据持久层操作的时候sqlprofiler的GUI介面中便出现了对应的操作记录，很清晰的列了出来：

<img src="http://pic.yupoo.com/skyforce/4306555a5aa3/ng2xhhvh.jpg" />
