--- 
layout: post
title: "Screenflow fatal initialization error 解决方案"
wordpress_id: 482
wordpress_url: http://www.agatezone.cn/code/?p=482
---
昨日使用 Screenflow, 在启动的时候遇到了 Screenflow fatal initialization error 这个错误窗口. 在 google 上找了半天才发现解决方案.

1. 删除 /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
2. 运行 OSX86Tools
    * 勾选 "Set Extensions permissions", "Clear Extensions Cache", "Touch Extensions Folder" 并且点击 "Run Selected Tasks" 按钮
    * 点击 "Add EFI String/Boot Flag" 按钮, 点击 "Ethernet Strings", 点击 "Import String to Boot Editor", 点击 "Apply changes to com.apple.Boot.plist"
    * 别点重启, 再次勾选 "Set Extensions permissions", "Clear Extensions Cache", "Touch Extensions Folder" 并且点击 "Run Selected Tasks" 按钮
3. 重启, 并在启动时候使用 "-f @ darwin" 参数

这样便会解决问题. 听说是因为网卡的驱动问题导致的. 这时候启动你会发现上不了网了, 但是不用急, 重启打开设置面板中的网络, 会发现一个新的网络连接. 选那个即可.

参考链接 [<a href="http://www.insanelymac.com/forum/index.php?showtopic=150671">link</a>]
