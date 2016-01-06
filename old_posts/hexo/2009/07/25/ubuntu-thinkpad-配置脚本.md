---
title: "Ubuntu: Thinkpad 配置脚本"
date: 2009-07-25
tags:
---

自从上一篇文章说了如何启用 thinkpad 的红帽和中键之后我又无聊地 google 了一番, 找到了一个叫做 thinkwiki 的网站, 里头有很多有用的关于 thinkpad 的资料. 特别是安装 linux 的配置资料.

看到了一个脚本 (for ubuntu 9.04)
用于解决 thinkpad:
1. 红帽/中键
2. FN+F8 开关触摸板
3. fix 了一些电源方面的 bug
4. 映射了 FN 作为 Menu 键

我修改了一点, 添加了激活静音键的功能, 具体修改后代码如下:
{% codeblock lang:ruby %}
#!/bin/sh
# Shell-script for postinstallation work on a T400 or another Thinkpad

# Scrolling with Trackpoint
echo '< ?xml version="1.0" encoding="UTF-8"?>
<match key="info.product" string="TPPS/2 IBM TrackPoint">
  <merge key="input.x11_options.EmulateWheel" type="string">true</merge>
  <merge key="input.x11_options.EmulateWheelButton" type="string">2</merge>
  <merge key="input.x11_options.XAxisMapping" type="string">6 7</merge>
  <merge key="input.x11_options.YAxisMapping" type="string">4 5</merge>
  <merge key="input.x11_options.ZAxsisMapping" type="string">4 5</merge>
  <merge key="input.x11_options.Emulate3Buttons" type="string">true</merge>
</match>' > /etc/hal/fdi/policy/mouse-wheel.fdi

# FN + F8 to switch trackpad on/off
echo '< ?xml version="1.0" encoding="UTF-8"?>
<deviceinfo version="0.2">
  <device>
    <match key="input.x11_driver" string="synaptics">
      <merge key="input.x11_options.SHMConfig" type="string">True</merge>
    </match>
  </device>
</deviceinfo>' > /etc/hal/fdi/policy/shmconfig.fdi

# recommended workaround for hard disk bug
sed -i 's/ENABLE_LAPTOP_MODE=false/ENABLE_LAPTOP_MODE=true/g' /etc/default/acpi-support

sed -i 's/BATT_HD_POWERMGMT=1/BATT_HD_POWERMGMT=200/g' /etc/laptop-mode/laptop-mode.conf

# Menu Key Workaround
sed -i 's|key\ <i151>\ \ \ {\ \ \ \ \ \ \[\ XF86WakeUp|key\ </i151><i151>\ \  {\ \ \ \ \ \ \[\ Menu\ \ \ \ \ \ |g' /usr/share/X11/xkb/symbols/inet

# Mute Key
cp /boot/grub/menu.lst /boot/grub/menu.lst.`date +%F`.bak
sed -i 's|kopt=root=UUID=.\{36\}\ ro$|&\ acpi_osi="Linux"|g' /boot/grub/menu.lst
update-grub

echo '==========================================='
echo 'After an reboot you certainly can use the features! To do so type "reboot"'
{% endcodeblock %}

把这段代码复制到一个文件中 (比如 thinkpad-config), 然后在 terminal 中执行:
$ chmod 775 thinkpad-config
$ sudo ./thinkpad-config

最后重启就 ok 了.
原始脚本地址可以访问: <a href="http://www.thinkwiki.org/wiki/Install_Ubuntu_9.04_(Jaunty_Jackalope)_on_a_ThinkPad_T400">URL</a></i151>
