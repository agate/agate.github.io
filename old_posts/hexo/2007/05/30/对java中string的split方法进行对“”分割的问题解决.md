---
title: "对JAVA中String的split方法进行对“.”分割的问题解决"
date: 2007-05-30
tags:
---

今天遇到一个对java中字符串分割的问题：

如何进行对 "." 这个符号的分割，使用 split 方法！

我试着使用 [StringName].split("."); 来进行分割，但是要知道在 split 中 "." 是用来匹配 "\n" 之外的任何单字符的，有人建议使用 "\." 但是明摆着这是不行的（语法本身就是错的！）最后在网上找到了正确匹配 "." 的方法：
{% codeblock lang:java %}
public class TestStringSplit {
  public static void main(String args[]) {
    String aaa = "aaa.bbb";
    String[] bbb = aaa.split("[.]");
    System.out.println("aaa=" + aaa);
    System.out.println("bbb.length=" + bbb.length);
    for(int n = 0; n < bbb.length; n++) {
      System.out.println("bbb[" + (n+1) + "]=" + bbb[n]);
    }
  }
}
{% endcodeblock %}
这样问题就解决了~~~
