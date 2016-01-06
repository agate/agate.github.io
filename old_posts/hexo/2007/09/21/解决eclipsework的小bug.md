---
title: "解决eclipsework的小bug"
date: 2007-09-21
tags:
---

最近由于学习struts2.0和webwork的需要我尝试了eclipsework的eclipse插件的使用。可能是因为财力问题，或者是作者无力再维护的缘故，eclipsework的wiki以及FAQ十分少，甚至连基本的文档都没有，只留下sourceforge的一些看不懂的视频……

管他的！但是用的时候发现其webwork的action.xml向导文件再进行动态更新xwork.xml的工作中始终无法找到xwork.xml让我十分头疼，甚至连google和baidu都无法受到解答（尽是一些同样问题的提问……）。

没办法咯，只好自己开始翻看他的src发现似乎是在解析xml-update的时候出现了问题，仔细翻看action.xml文件发现
<code>&lt;xml-update <span style="color: rgb(255, 0, 0);">file="xwork.xml"</span>&gt;
　　&lt;package name="${xwork_package_name}" extends="${xwork_package_extends}"
　　　namespace="$!xwork_package_namespace" check-before-create="true"&gt;
　　　　&lt;action name="${xwork_action_name}" class="${action}"
　　　　　method="$!methodName"&gt;
　　　　　　&lt;result name="success" type="${radio}"&gt;${resultName}&lt;/result&gt;
　　　　&lt;/action&gt;
　　&lt;/package&gt;
&lt;/xml-update&gt;</code>
这个file到底是什么，如果只是xwork.xml应该不会出现这个问题的……

进一步查看官方网站的资料发现：file是一个标签，可以指定到一个文件
哈哈终于真相大白，原来这个template包是有小小的bug的，只要在签名适当的地方加入
<code>&lt;file name="xwork.xml" label="xwork.xml" type="folder" extensions="xml"/&gt;</code>
就行了！

这样变解决了eclipsework中的webwork自动生成的问题！再次感谢eclipsework的作者！一个让我感动的插件！
