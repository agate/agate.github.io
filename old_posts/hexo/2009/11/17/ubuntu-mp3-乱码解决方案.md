---
title: "ubuntu mp3 乱码解决方案"
date: 2009-11-17
tags:
---

<code>$ sudo apt-get install python-mutagen
$ cd your-mp3-dir
$ find . -iname "*.mp3" -execdir mid3iconv -e GBK {} \;</code>
