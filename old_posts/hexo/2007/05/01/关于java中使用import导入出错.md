---
title: "关于JAVA中使用import导入.*出错"
date: 2007-05-01
tags:
---

学java的时候一直有一个十分不解的疑问：

为什么自己建立的包不可以导入所有包中类(import 包名.*;)

{% codeblock lang:java %}
//用.*来导入全部class，这么导入多个class是可以的！
import java.io.*;
import java.util.*;
public class Example {
}
{% endcodeblock %}
上面这么写是可以的，但是但我自己用自己写的包时就不可以了，会报错：

{% codeblock lang:java %}
//这里是TestPackageOne类的代码
package cn.letiteasy.testPackage;

public class TestPackageOne {
  public void show() {
    System.out.println("HelloWorld!");
  }
}
{% endcodeblock %}

{% codeblock lang:java %}
//这里是TestPackageFour类的代码
import cn.letiteasy.testPackage.*;

public class TestPackageFour {
  public static void main (String args[]) {
    TestPackageOne a = new TestPackageOne();
    a.show();
  }
}
{% endcodeblock %}

我先把TestPackageOne.class放到了对应的目录下了
现在我的文件结构是:

    root\
    root\TestPackageOne.java
    root\TestPackageFour.java
    root\cn\letiteasy\testPackage\TestPackageOne.class

但是我编译TestPackageFour.java的时候出现如下错误：
---
title: "关于JAVA中使用import导入.*出错"
date: 2007-05-01
tags:
---
---------------------------------------------
      错误的类文件： d:\java\class\TestPackageOne.java
      文件不包含类 TestPackageOne
      请删除该文件或确保该文件位于正确的类路径子目录中。
      TestPackageOne a = new TestPackageOne();
      ^
      1 错误
---
title: "关于JAVA中使用import导入.*出错"
date: 2007-05-01
tags:
---
---------------------------------------------

但是要是我把 TestPackageFour.java 中的

    import cn.letiteasy.testPackage.*;

改成

    import cn.letiteasy.testPackage.TestPackageOne;

就可以通过了

一开始我一直不知道是为什么，明明书上是这么说的，于是也就大概觉得书上指的是原包中的那些 class 吧。但是最近在问一位朋友的时候才知道了"内幕"

原来啊，这个是java虚拟机的缘故：
> 因为在编译的时候会优先找到这个 java 文件, 编译后因为这个没有包结构所以把 root\TestPackageOne.java 这个 java 文件放到别的目录下就可以了  
> import cn.letiteasy.testPackage.TestPackageOne; 指明了是包里面的类, 所以不会编译这个 java 文件
啊~~这才真相大白^^
