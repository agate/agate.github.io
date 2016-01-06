---
title: "rails 两个帮助方法 xxx_path 和 xxx_url 区别"
date: 2008-10-06
tags:
---

其实这两个形成的地址没啥区别, 只不过使用 xxx_url 这个帮助方法会在地址的最后加上 "/". 
<blockquote>比如:
xxx_path 生成 http://www.agatezone.cn
xxx_url 生成 http://www.agatezone.cn/</blockquote>
其实有一个这类帮助方法书写的格式:
<img src="/images/archive/2008/10/rest_helper_method.png" />
如果使用一对多的模型建立控制器, 这种的 rest 控制器的帮助方法就类似如下格式:
<img src="/images/archive/2008/10/rest_helper_method_ext.png" />
解释一下:
namespace 就是命名空间(说白了就是放在那个目录下);
parent resource 是指如果有父模型就填入, 同理那个 p 就是父模型的对象实体.
