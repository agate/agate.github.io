--- 
layout: post
title: "virtual attribute 是一个好思路"
wordpress_id: 199
wordpress_url: http://www.agatezone.cn/code/?p=199
---
每日 rails 每日发现圈子里天才多多! 对于天赋我深信不疑! 嘿嘿! 特别喜欢天才! 对天才有特殊的癖好! 比如恋天才癖啊~

废话一大堆, 切入正题! virtual attribute 是 rails 保存 model 中使用的一个技巧! 很实用, 很天才...(又来了) 有时候我们模型的属性设置是一个样, 但是我们表单设计又是另外一个样子.(好拗口) 打个比方: 一个 user 模型, 有 first_name, last_name 等属性; 对应表单只有一个 name 输入框(规矩是根据空格区分 first_name 和 last_name). 这个问题来了, 默认情况下 controller 的 create 或者 update 都是通过 params[:user] 来注入传入表单数据到模型实体的. 问题是 user 模型中并没有 name 属性, 同时 user 的 first_name 和 last_name 也未被赋值. 在这个时候 virtual attribute 就显示他的优势了! 见代码:
<code><span style="color: #808080;">&lt;!-- users/new.rhtml --&gt;</span>
&lt;%= f.text_field :name %&gt;</code><code><span style="color: #808080;"># models/user.rb</span>
def name
&nbsp;&nbsp;[first_name, last_name].join(' ')
end
def name=(name)
&nbsp;&nbsp;split_names = name.split(' ', 2)
&nbsp;&nbsp;self.first_name = split_names.first
&nbsp;&nbsp;self.last_name = split_names.last
end</code>
这样, 在保存或是修改 user 模型的时候就能正常工作了!(不需变动原有控制器哦!) 这就是 'skinny controller, fat model' 的好处. 这种用法十分聪明和实用, 在使用类似 make_resourceful 这种简化 controller 代码的插件的时候这种技巧就更显得重要了!
