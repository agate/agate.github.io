---
title: "使用 VMware + Greasemonkey 在 Windows 下自动测试开发远程 rails 应用"
date: 2008-10-21
tags:
---

怎么说呢~ 我还是比较喜欢视窗系统下的使用开发方式(具体原因是 Linux 和 Mac 对中文字体的渲染实在是不敢恭维). 于是目前我使用开发 web 程序的方式是使用 VMware, 在视窗系统下使用 PuTTY 和视窗共享来操作 Linux 系统, 并进行开发. 效果挺不错的. 本文书写的原因是 autotest 在远程调用时候比较不容易实现<strong>可视化</strong>的自动测试(出错有声音啊, 有红字啊~). 所以经过变通思考我决定采用 Firefox + Greasemonkey 这样的搭配来实现定时访问 autotest 生成的 html 结果, 从而在视窗系统下对远端 Linux 开发机进行自动化测试和提示.

先看看效果图:

<img src="/images/archive/2008/10/rspec_linux_windows_layout.png" />

<img src="/images/archive/2008/10/rspec_linux_windows_result.png" />

你会问, autotest 生成的 html 并不能自动刷新啊, 这里我就想到了 Greasemonkey 这个强大的 Firefox 自定义扩展插件. 可以通过自己手动书写 JS 来扩展页面功能/样式.

于是我便写了一个简单的 JS 脚本, 提供 n 秒自动刷新, 有 failures 就发出报告声. 脚本如下:
{% codeblock lang:javascript %}
// ==UserScript==
// @name           rspec results auto refresh
// @namespace      agatezone
// ==/UserScript==

// modify vars
var time_left = 10;
var path = "file:///E:/my_help_files/GreasemonkeyFiles/rspec_results_auto_refre";

// script begin ---------
// init
init();

// play error sound while has errors.
if (hasError()) {
	var sound = document.createElement('div');
	document.getElementById('reload').appendChild(sound);
	sound.innerHTML = "<embed name=\"pmsound2player\" src=\"" + path + "player.swf\" flashvars=\"sFile=" + path + "failure.mp3\" menu=\"false\" allowscriptaccess=\"sameDomain\" swliveconnect=\"true\" type=\"application/x-shockwave-flash\" width=\"0\" height=\"0\">";
}

// start timer
reloadTimer();

/////////////////////////////

// functions start ++++++++++++++++
function init() {
	var summary = document.getElementById('summary');
	var p = document.createElement('p');
	var t = document.createTextNode('');
	p.setAttribute('id', 'reload');
	p.appendChild(t);
	summary.appendChild(p);
}

function setTitle(x) {
	document.title = x;
	document.getElementById('reload').firstChild.nodeValue = x + "...";
}

function reloadTimer() {
	if (time_left <= 0) {
		setTitle('Reloading...');
		window.location.reload();
	} else {
		setTitle ('Reload in ' + time_left + ' second' + (time_left == 1 ? '' : 's'));
		setTimeout (reloadTimer, 1000);
		time_left --;
	}
}

function hasError() {
	var result_text = document.getElementById('totals').firstChild.nodeValue;
	var re = /(\d+)\s+examples?,\s*(\d+)\s+failures?(,\s*(\d+)\s+pending)?/;
	var results = re.exec(result_text);
	if (results[2] != 0) {
		return true;
	} else {
		return false;
	}
}
// functions end ++++++++++++++++
// script end ---------
{% endcodeblock %}
这里有两个文件 <a href="http://www.box.net/shared/b828gsipa2">DOWNLOAD</a> 主要作为错误提示音使用, 请解压开后放置到一个位置, 并且把这段代码里头的 path 修改为这两个文件存放的位置. 就比如我把这两个提示音文件放在:
<code>c:\autotest_rspec\</code>
下面, 那么 path 就改成:
<code>file:///C:/autotest_rspec/</code>
这样的网页地址形式.

这样便可以简单地在微软视窗操作系统下实现自动化测试远端开发机并给出结果提示.

灵感: Greasemonkey 太强大了! JavaScript 同样! Dom 模型更是了不起!
