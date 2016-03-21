title: Gem Install SSL Errors
date: 2016-03-21 13:16:28
tags:
---
这几天老是发现 gem / bundle install 的时候出现这样的错误:

`ssl_connect returned=1 errno=0 state=sslv3 read server certificate b: certificate verify failed`

也不知道为什么. 试图使用不同的源也不顶用. 只能无奈地在 `.gemrc` 文件里加入 `:ssl_verify_mode: 0`. 但是这样总是心里不舒服. 于是就遍地找解决方法. 于是就发现了:

[OpenSSL Errors and Rails – Certificate Verify Failed @ RailsApps Project](http://railsapps.github.io/openssl-certificate-verify-failed.html)

原来发生这个问题的原因是因为系统里的 certificate files 过期了. 其实只需要更新你的 openssl 证书既可.
在 Mac OS X 下 rvm 还提供了很方便的更新脚本: `rvm osx-ssl-certs update all` 以及 `rvm osx-ssl-certs cron install` 来创建一个 cronjob, 让其自动帮你定期更新证书.

这篇文章里也在最后简单地介绍了 windows / linux 下如何解决这个问题的方法.
