--- 
layout: post
title: "架设 Git 服务器 -- gitosis 方式"
wordpress_id: 671
wordpress_url: http://www.agatezone.cn/code/?p=671
---
参考: <a href="http://progit.org/book/zh/ch4-0.html">http://progit.org/book/zh/ch4-0.html</a>

1. 安装 git

2. 安装 gitosis
<code>$ git clone git://eagain.net/gitosis.git
$ sudo apt-get install python-setuptools
$ cd gitosis
$ sudo python setup.py install</code>

3. 创建 git 用户
<code>$ sudo adduser \
--system \
--shell /bin/sh \
--gecos 'git version control' \
--group \
--disabled-password \
--home /home/git \
git</code>

4. 初始化 gitosis
使用 ssh-keygen 来建立 ssh 公钥(如果你已经有了就不必了)
<code>$ ssh-keygen</code>
然后
<code>$ sudo cp ~/.ssh/id_rsa.pub /tmp/
$ sudo -H -u git gitosis-init < /tmp/id_rsa.pub
$ sudo chmod 755 /home/git/repositories/gitosis-admin.git/hooks/post-update</code>

5. 配置 gitosis
</code><code>$ cd
$ git clone git@localhost:gitosis-admin.git
$ cd gitosis-admin</code>

5.1. 编辑 gitosis.conf 文件, 格式如下
<blockquote>[group {repository-name}]
writable = {dir-name}
members =  {user1} {user2}</blockquote>

5.2. 添加 user1.pub 和 user2.pub 到 keydir 目录下
5.3. 提交你的修改和添加的 pub 文件
<code>$ git commit -a -m "message"
$ git push</code>
5.4. 这样 user1 和 user2 就可以通过 git 操作那个 {repository-name} 了, 例如:
<code>$ git clone git@your_server_ip:{repository-name}.git</code>

总结:
gitosis 不用让用户把自己的 ssh 公钥贴到 ~/.ssh/authorized_keys 中, 转而交给自己 gitosis-admin 中的 keydir 目录管理, 相当巧妙.
