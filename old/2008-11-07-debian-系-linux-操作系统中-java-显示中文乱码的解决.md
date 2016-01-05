--- 
layout: post
title: "debian 系 Linux 操作系统中 Java 显示中文乱码的解决"
wordpress_id: 280
wordpress_url: http://www.agatezone.cn/code/?p=280
---
奇怪... Ubuntu8.04 下我都没碰到这类问题, 倒是升级到 Ubuntu8.10 的时候 java 就出现乱码了~ 不说为什么, 因为我也不知道. 这里记录一下简单的解决方案:
1. 
在 ${JRE_HOME}/lib/fonts/ 下建立个目录 fallback
比如我这儿就是
<code>$cd /usr/lib/jvm/java-6-sun/jre/lib/fonts/
$mkdir fallback</code>

2.
在 fallback 里弄个中文字体(拷贝或链接都可以)
比如我这就是
<code>$ln -s /usr/share/fonts/truetype/arphic/uming.ttf /usr/lib/jvm/java-6-sun/jre/lib/fonts/fallback/</code>


3.
进入 ${JRE_HOME}/lib/fonts/fallback/ 执行 mkfontscale, 再把 jre/lib/fonts/fallback/fonts.scale 的内容加到 ${JRE_HOME}/lib/fonts/fonts.dir
我这儿就是
<code>$cd /usr/lib/jvm/java-6-sun/jre/lib/fonts/fallback/
$mkfontscale
$cd ..
$cat fallback/fonts.scale >> fonts.dir</code>

DONE!
