---
title: "Fitx: Linux 下优秀的输入法"
date: 2009-08-17
tags:
---

Fitx 这个开源的优秀输入法让我在 linux 下体会到如同 windows 下搜狗输入法那样的舒服. 良好的速度, 流畅的输入体验, 完整的用户词库导出导入功能. 我觉得在 linux 下, 没有什么输入法能让我如此着迷的了.

Fitx 是 <a href="http://fit.coollittlethings.com/">http://fit.coollittlethings.com/</a> 出品的. 同样地, 也有 mac 版本. 同样是好用得不得了. 但是可惜的是目前免费的 MAC 版本官方已经不再更新了. 我想估计是资金问题吧. 不过如果好用的话, 我会考虑购买一个的.

不过说回来, 我还是喜欢免费的午餐. 特别是 linux 下. 我们可以通过 svn 导出 <a href="http://code.google.com/p/fitx/">http://code.google.com/p/fitx/</a> 里头的源文件. 然后自行编译安装.

具体步骤如下.
1. $ svn co http://fitx.googlecode.com/svn/branches/fitx-autotool fitx-autotool
2. $ cd fitx-autotool
3. $ ./autogen.sh
4. $ make deb && sudo dpkg -i ../fitx_*.deb

其中遇到任何错误基本是没有安装完整的编译工具导致. 请查看 log 并安装对应的编译帮助工具即可.
最后执行那个生成的 deb 安装包就 ok 咯!
