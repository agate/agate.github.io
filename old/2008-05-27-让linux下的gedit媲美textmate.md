--- 
layout: post
title: "让linux下的gedit媲美textmate"
wordpress_id: 62
wordpress_url: http://www.agatezone.cn/code/?p=62
---
好好学习,天天ruby!最近决定好好学习一下动态语言!看着那视频里头的高手用着mac os,在textmate上有如魔法般打出成堆的代码!我就暗下决心要用mac,要用textmate.但是事实上我没钱买mac,一时半会也弄不到mac for x86的dvd.linux又刚刚装好,今天就发现原来gedit也可以这么牛B的!试用了一下,发现和我朋友机器上的textmate差不多阿!

gedit是使用插件扩展自身的,所以一定程度上对textmate有优势.
大部分的plugin可以在 <a href="http://live.gnome.org/Gedit/Plugins">连接</a> 下载到.
在这里我列出我使用的插件列表:
<blockquote>Class Browser  ：显示类的大纲
Code Formatter ：自动格式化，作者特为ruby文件做了优化
Find In File ：在文件中查找
Full Screen ：全屏
Gemini ：自动匹配括号引号和％（&lt;%%&gt;）
Rails Hot Commands ：按下ctrl + alt + c 可以选择执行rails常用命令 (也可以输入所有的linux终端命令，将在项目根目录下执行)
Rails Hotkeys ：按下ctrl+ shift + R 后再按键在相关文件中跳转, 如A打开application.rb M打开model，C打开controller等等，查看帮助按F1。
Snap Open ：按下ctrl + shift + O 可以输入文件名（支持正则）打开文件 (<span style="color: #ff0000;">新版修正为 ctrl + alt + o</span>)
Word Completion ：伪代码提示，只是把当前打开文件中的单词进行提示，但是对于录入速度帮助很大。
缩进行 ：多行的缩进与反缩进
外部工具 ：运行外部工具，如shell命令等。可根据自己需要设置。
文件浏览面板 ：浏览、打开文件</blockquote>
gedit的插件都是用python写的，可以很方便的根据自己偏好修改完善。还有很多插件，根据自己需要酌情添加。
把这些plugin都放在~/.gnome2/gedit/plugins目录下(没有这个目录自己建立一个)

喜欢textmate那个暗调的配色主题,可以到把http://grigio.org/files/darkmate.xml下载下来放入~/.gnome2/gedit/styles目录下方可.要是有其他需求可以到http://live.gnome.org/GtkSourceView/StyleSchemes去看看!

后续有很多细节,比如S的扩展阿,rhtml的支持阿等等,这里记录一些参考资料有待查阅:
http://grigio.org/pimp_my_gedit_was_textmate_linux
