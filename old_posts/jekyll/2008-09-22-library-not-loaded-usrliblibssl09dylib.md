--- 
layout: post
title: "\"Library not loaded: /usr/lib/libssl.0.9.dylib\" easy solution for Leopard"
wordpress_id: 204
wordpress_url: http://www.agatezone.cn/code/?p=204
---
when you execute some app, you will get this error info like:
<blockquote>Dyld Error Message:
Library not loaded: /usr/lib/libssl.0.9.dylib
Referenced from: /Library/Frameworks/xxxxx
Reason: no suitable image found. Did find:
/usr/lib/libssl.0.9.dylib: mach-o, but wrong architecture
/usr/lib/libssl.0.9.dylib: mach-o, but wrong architecture</blockquote>
The easy solution to this is to backup you libcrypto.0.9.dylib, libssl0.9.dylib and copy over the libcrypto.0.9.7.dylib and libcrypto.0.9.7.dylib.

You can use Terminal.app to make these changes. It is in your Applications folder. (Make sure that you are only copying the part after the $)

<code>$ cd /usr/lib
$ sudo cp libcrypto.0.9.dylib libcrypto.0.9.dylib.old
$ sudo cp libssl.0.9.dylib libssl.0.9.dylib.old
$ sudo ln -sf libcrypto.0.9.7.dylib libcrypto.0.9.dylib
$ sudo ln -sf libssl.0.9.7.dylib libssl.0.9.dylib</code>

close your Terminal. done!
