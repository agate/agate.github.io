---
title: "Google Chart Tools"
date: 2010-02-13
tags:
---

今天看到 google 出了一组很酷的图形 API

<img src="http://chart.apis.google.com/chart?cht=bhs&chs=75x50&chd=t:10,50,60,80,40|50,60,100,40,20&chco=4d89f9,c6d9fd&chbh=20&chds=0,160&chbh=a" title="Bar Charts" /><img src="http://chart.apis.google.com/chart?chs=75x75&cht=ls&chd=t0:0,17,7,6|0,30,27,54|0,45,47,46|0,63,59,60|-1,40,35,-1|-1,5,70,-1|-1,-1,80,-1&chm=F,0000FF,0,1:2,10|H,0000FF,0,1:2,1:10|H,0000FF,3,1:2,1:10|H,0000FF,4,1:2,1:10|o,FF0000,5,,5|o,FF0000,6,,5" title="Box Charts" /><img src="http://chart.apis.google.com/chart?chs=75x50&cht=lc&chd=t0:-1,5,10,7,12,-1|-1,25,45,47,24,-1|-1,40,30,27,39,-1|-1,55,63,59,80,-1&chm=F,0000FF,0,,10" title="Candlestick Charts" /><img src="http://chart.apis.google.com/chart?cht=bvs&chbh=5,2&chm=D,0033FF,2,0,5,1&chbh=20&chs=75x50&chd=s2:1XQbnf4,EWoQMUB,9halxp9&chco=4D89F9,C6D9FD&chbh=a" title="Compound Charts" /><img src="http://chart.apis.google.com/chart?chst=d_bubble_icon_text_small&chld=ski|bb|Wheeee!|FFFFFF|000000" title="Dynamic Icons" /><img src="http://chart.apis.google.com/chart?cht=tx&chl=x%20=%20%5Cfrac%7B-b%20%5Cpm%20%5Csqrt%20%7Bb%5E2-4ac%7D%7D%7B2a%7D" title="Formulas" /><img src="http://chart.apis.google.com/chart?chs=75x50&cht=gom&chd=t:70&chco=FF0000,FF8040,FFFF00,00FF00,00FFFF,0000FF,800080" title="Google-O-Meter Charts" /><img src="http://chart.apis.google.com/chart?cht=lxy&chs=75x50&chd=t:10,20,40,80,90,95,99|20,30,40,50,60,70,80|-1|5,10,22,35,85&chco=3072F3,ff0000,00aaaa&chm=s,FF0000,0,-1,2|s,0000ff,1,-1,2|s,00aa00,2,-1,2" title="Line Charts" /><img src="http://chart.apis.google.com/chart?cht=t&chs=150x75&chd=t:0,100,50,32,60,40,43,12,14,54,98,17,70,76,18,29&chco=FFFFFF,FF0000,FFFF00,00FF00&chld=DZEGMGAOBWNGCFKECGCVSNDJTZGHMZZM&chtm=africa&chf=bg,s,EAF7FE" title="Map Charts" /><img src="http://chart.apis.google.com/chart?cht=p3&chd=s:Uf9a&chs=75x50" title="Pie Charts" /><img src="http://chart.apis.google.com/chart?chs=50x50&cht=qr&chl=Hello+world&chld=L|1&choe=UTF-8" title="QR Codes" /><img src="http://chart.apis.google.com/chart?cht=rs&chs=75x75&chd=t:77,66,15,0,31,48,100,77|20,36,100,2,0,100&chco=FF0000,FF9900&chls=2.0,4.0,0.0|2.0,4.0,0.0&chxt=x&chxl=0:|0|45|90|135|180|225|270|315&chxr=0,0.0,360.0&chg=25.0,25.0,2.0,2.0&chm=B,FF000080,0,1.0,5.0|B,FF990080,1,1.0,5.0&chxs=0,000000,4,0" title="Radar Charts" /><img src="http://chart.apis.google.com/chart?cht=s&chd=t:12,87,75,41,23,96,68,71,34,9|98,60,27,34,56,79,58,74,18,76|42,11,33,40,22,45,30,45,32,27&chs=75x50&chco=FF0000" title="Scatter Charts" /><img src="http://chart.apis.google.com/chart?cht=v&chs=75x50&chd=t:100,100,0,50" title="Venn Charts" />

地址: http://code.google.com/apis/charttools/

目前提供:
1. Image charts - using a simple URL request to a Google chart server
2. Interactive charts - using a Google developed JavaScript library
具体的就是:
1 -- [图片型图标] 只是一个图片而已
2 -- [可视化图标] 是一个 javascript 实现的可视化图形组件, 提供动态显示和鼠标事件

具体可以到: http://code.google.com/apis/charttools/docs/choosing.html 看看二者的区别
