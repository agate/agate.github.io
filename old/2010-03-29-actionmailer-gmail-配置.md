--- 
layout: post
title: "ActionMailer Gmail 配置"
wordpress_id: 604
wordpress_url: http://www.agatezone.cn/code/?p=604
---
预备知识:
<blockquote>
1. Gmail 使用 TLS 协议
2. Gmail 有 Captcha 验证问题, 同样影响到 SMTP 客户端
3. 低于或等于 1.8.6 版本的 Ruby 不支持 TLS
4. 低于 2.2.1 版本的 Rails 不支持 TLS
</blockquote>

<strong>所以呢, 你如果是符合 Ruby >= 1.8.7 并且 Rails >= 2.2.1 那么请 Follow 如下步骤:</strong>

1. 设置 ActionMailer::Base.smtp_settings
{% highlight ruby %}
# 添加一个 rb 文件到 config/initializers/ 目录中, 内容如下:
ActionMailer::Base.smtp_settings = {
  :address              => "smtp.gmail.com",
  :port                 => 587,
  :authentication       => :plain,
  :enable_starttls_auto => true,
  :user_name            => "USERNAME@DOMAIN",
  :password             => "PASSWORD"
}
# 这里的关键在 enable_starttls_auto
{% endhighlight %}

2. 取消 Gmail 帐号的 Captcha
打开连接 www.google.com/a/DOMAIN/UnlockCaptcha
输入用户名密码即可解锁

<strong>如果你是老版本呢~ 可以参考</strong>

1. rails 官方文档 http://guides.rubyonrails.org/action_mailer_basics.html
2. 解决方案插件 http://github.com/openrain/action_mailer_tls
