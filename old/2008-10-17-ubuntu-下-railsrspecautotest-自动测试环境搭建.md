--- 
layout: post
title: "ubuntu 下 rails/rspec/autotest 自动测试环境搭建"
wordpress_id: 257
wordpress_url: http://www.agatezone.cn/code/?p=257
---
羡不羡慕那些 rails 视频在 MAC OS X 下面帅气的自动跳出绿色和红色的自动测试提示呢? 当然如果你是 MAC 用户就不用羡慕了哈!(比如我就不羡慕嘿嘿) 但是大部分朋友都是 PC 呀! 没有 MAC 下的 Growl 作为 UI 提示工具怎么办呢? 没事啦! 这些我们都好解决, Ubuntu 下面我们可以用 rnotify 这个 ruby gnome 的消息提示工具. Windows 下我们可以用 ruby-snarl 这个消息提示工具啦! 当然还有 AutoIt 这类辅助工具! 这里我们先说 Ubuntu 这样的 GNOME 环境中的解决方案.

首先是安装 autotest, rspec, rspec_rails 三个插件
<code>$sudo gem install autotest
$rails hello
$cd hello
$./script/plugin install http://rspec.rubyforge.org/svn/tags/CURRENT/rspec
$./script/plugin install http://rspec.rubyforge.org/svn/tags/CURRENT/rspec_on_rails
$./script/generate rspec
</code>
这样便安装好最基础的 BDD 环境了. 手动在你的 rails 目录下键入
<code>$./script/autospec
<span style="color: #339966;">这是这个自动测试不是在后台运行的, 因为他要显示信息嘛!
所以最小化这个终端窗口吧, 或者新开一个 Tab 来继续操纵你的 rails 应用.</span></code>
就可以启动针对此 rails 应用的持续测试功能了. 让我们来试试看! 如何工作, 在终端中你的 rails 目录下键入:
<code>$./script/generate rspec_scaffold post title:string
$rake db:migrate
$rake db:test:clone</code>
看看你的那个自动测试窗口吧! (如果你的小机器不太快, 这个测试窗口还和原来一样, 那么稍等一会会, 他马上就运行咯!) 你大概会看到类似的结尾结果:
<img src="/images/archive/2008/10/ubuntu-autotest-terminal.png" alt="" />
哈! 是不是很有成就感? (当时我满有的...) 呵呵, 但是这个只是在终端中看到的, 难不成要我们每次保存了新的东西都要光顾我们的终端信息么? Mac 下有 Growl 来做桌面 UI 气泡提示. 在 Ubuntu 这样的 GNOME 下我们可以使用 ruby-notify 来实现. 首先必须安装 ruby-gnome2 / libnotify-dev 和 ruby-libnotify 这些组件依赖. (<span style="color: #ff0000;">其中 ruby-libnotify 需要手动安装</span>)
<code>$sudo apt-get install ruby-gnome2 libnotify-dev</code>
以上安装好了 ruby-gnome2 和 libnotify-dev , 至于 ruby-libnotify 可以到其<a href="http://ruby-libnotify.rubyforge.org">官方网站</a>下载手动其<span style="color: #ff0000;">源代码</span>编译安装, 当前最新版本为 <a href="http://rubyforge.org/frs/?group_id=1911">0.3.3</a>, 在其下载页面我下好了 ruby-libnotify-0.3.3.tar.bz2 文件, 将其解压开好. 使用终端进入其目录中执行:
<code>$ruby extconf.rb
$sudo make
$sudo make install</code>
这样就安装好 ruby-libnotify 了! 其实就是用它来代替 Mac 下的 Growl 啦! 接着建立 ~/.autotest 文件并填入如下代码.
{% highlight ruby %}
require 'rnotify'
require 'gtk2'

module Autotest::RNotify
  class Notification
    attr_accessor :verbose, :image_root, :tray_icon, :notification,
      :image_pass, :image_pending, :image_fail,
      :image_file_pass, :image_file_pending, :image_file_fail,
      :status_image_pass, :status_image_pending, :status_image_fail

    def initialize(timeout = 5000,
        image_root = "#{ENV['HOME']}/.autotest_images" ,
        verbose = false)
      self.verbose = verbose
      self.image_root = image_root
      self.image_file_pass = "#{image_root}/pass.png"
      self.image_file_pending = "#{image_root}/pending.png"
      self.image_file_fail = "#{image_root}/fail.png"

      raise("#{image_file_pass} not found") unless File.exists?(image_file_pass)
      raise("#{image_file_pending} not found") unless File.exists?(image_file_pending)
      raise("#{image_file_fail} not found") unless File.exists?(image_file_fail)

      puts 'Autotest Hook: loading Notify' if verbose
      Notify.init('Autotest') || raise('Failed to initialize Notify')

      puts 'Autotest Hook: initializing tray icon' if verbose
      self.tray_icon = Gtk::StatusIcon.new
      tray_icon.pixbuf = Gdk::Pixbuf.new(image_file_pending,22,22)
      tray_icon.tooltip = 'RSpec Autotest'

      puts 'Autotest Hook: Creating Notifier' if verbose
      self.notification = Notify::Notification.new('X', nil, nil, tray_icon)

      notification.timeout = timeout

      Thread.new { Gtk.main }
      sleep 1
      tray_icon.embedded? || raise('Failed to set up tray icon')
    end

    def notify(icon, tray, title, message)
      notification.update(title, message, nil)
      notification.pixbuf_icon = icon
      tray_icon.tooltip = "Last Result: #{message}"
      tray_icon.pixbuf = tray
      notification.show
    end

    def passed(title, message)
      self.image_pass ||= Gdk::Pixbuf.new(image_file_pass, 48, 48)
      self.status_image_pass ||= Gdk::Pixbuf.new(image_file_pass, 22, 22)
      notify(image_pass, status_image_pass, title, message)
    end

    def pending(title, message)
      self.image_pending ||= Gdk::Pixbuf.new(image_file_pending, 48, 48)
      self.status_image_pending ||= Gdk::Pixbuf.new(image_file_pending, 22, 22)
      notify(image_pending, status_image_pending, title, message)
    end

    def failed(title, message)
      self.image_fail ||= Gdk::Pixbuf.new(image_file_fail, 48, 48)
      self.status_image_fail ||= Gdk::Pixbuf.new(image_file_fail, 22, 22)
      notify(image_fail, status_image_fail, title, message)
    end

    def quit
      puts 'Autotest Hook: Shutting Down...' if verbose
      #Notify.uninit
      Gtk.main_quit
    end
  end

  Autotest.add_hook :initialize do |at|
    @notify = Notification.new
  end

  Autotest.add_hook :ran_command do |at|
    results = at.results.last

    unless results.nil?
      output = results[/(\d+)\s+examples?,\s*(\d+)\s+failures?(,\s*(\d+)\s+pending)?/]
      if output
        failures = $~[2].to_i
        pending = $~[4].to_i
      end

      if failures > 0
        @notify.failed("Tests Failed", output)
      elsif pending > 0
        @notify.pending("Tests Pending", output)
      else
        unless at.tainted
          @notify.passed("All Tests Passed", output)
        else
          @notify.passed("Tests Passed", output)
        end
      end
    end
  end

  Autotest.add_hook :quit do |at|
    @notify.quit
  end
end
{% endhighlight %}
然后呢, 这里有几个图片, 请你下载下来保存到 ~/.autotest_images 目录下(自己建立这个文件夹).
<img src="/images/archive/2008/10/pending.png" alt="" /> <img src="/images/archive/2008/10/pass.png" alt="" /> <img src="/images/archive/2008/10/fail.png" alt="" />
(注意哦! 文件名不要变哦! 分别为 pending.png pass.png fail.png)

打工告成! 你可以在 rails 工程目录里头执行:
<code>$./script/autospec</code>
不出意外的话你应该会看到如下结果
<img src="/images/archive/2008/10/ubuntu-autotest-notify.png" alt="" />

Tips:
1. ~/.autotest 这个文件可以定制 autotest 的运行.
2. ruby-libnotify 可以用于 GNOME 中作为消息提示.(<span style="color: #ff0000;">注意哦! 用源代码编译安装哦!</span>)
