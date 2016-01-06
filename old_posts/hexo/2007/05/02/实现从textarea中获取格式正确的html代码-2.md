---
title: "实现从TextArea中获取格式正确的HTML代码"
date: 2007-05-02
tags:
---

在进行JSP开发的时候经常碰到文本编辑的东西，虽然现在有大量可用的现成网页代码编辑器，但是一些小模块只需要写写文字之类的还是自己写一个 `<textarea></textarea>` 来记录比较妥当。

但是呢~这个传到数据库后调用是直接显示为html时会发现没有了原来的段落格式了，而且很多比如 "`<`" , "`>`" , "`&`" 这类的特殊符号还会导致整个页面变形……

呵呵说起来可怕了些，最近写了一个java转换的代码，就可以实现从textarea中获得格式正确的html代码了！

具体代码如下：
{% codeblock lang:java %}
public class TransHTMLSQL {
  public String replace(String str_source, String str_original, String str_new) {
    if (str_source == null) return null;
    StringBuffer output = new StringBuffer();
    int lengOfsource = str_source.length();
    int lengOfold = str_original.length();
    int posStart = 0;
    int pos;
    while ((pos = str_source.indexOf(str_original,posStart)) >= 0 ) {
      output.append(str_source.substring(posStart,pos));
      output.append(str_new);
      posStart = pos + lengOfold;
    }
    if(posStart < lengOfsource) {
      output.append(str_source.substring(posStart));
    }
    return output.toString();
  }

  public String toHtml(String s) {
    s = replace(s, "<", "&lt;");
    s = replace(s, ">", "&gt;");
    s = replace(s, "&", "&amp;");
    s = replace(s, "\t", " ");
    s = replace(s, "\r\n", "\n");
    s = replace(s, "\n", "<br/>");
    s = replace(s, " ", "&nbsp;");

    return s;
  }

  public String unHtml(String s)  {
    s = replace(s, "&nbsp;", " ");
    s = replace(s, "<br/>", "\n");

    return s;
  }
}
{% endcodeblock %}
