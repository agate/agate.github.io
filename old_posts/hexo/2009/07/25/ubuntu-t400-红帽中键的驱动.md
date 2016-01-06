---
title: "Ubuntu: T400 红帽+中键的驱动"
date: 2009-07-25
tags:
---

编辑 /etc/hal/fdi/policy/mouse-wheel.fdi (大概默认没有, 自己建立一个)
填入如下内容:
{% codeblock lang:xml %}
<match key="info.product" string="TPPS/2 IBM TrackPoint">                       
  <merge key="input.x11_options.EmulateWheel" type="string">true</merge>
  <merge key="input.x11_options.EmulateWheelButton" type="string">2</merge>
  <merge key="input.x11_options.YAxisMapping" type="string">4 5</merge>
  <merge key="input.x11_options.XAxisMapping" type="string">6 7</merge>
  <merge key="input.x11_options.Emulate3Buttons" type="string">true</merge>
  <merge key="input.x11_options.EmulateWheelTimeout" type="string">200</merge>
</match>
{% endcodeblock %}
重启机器就 ok 了.
