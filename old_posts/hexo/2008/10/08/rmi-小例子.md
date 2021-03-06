---
title: "RMI 小例子"
date: 2008-10-08
tags:
---

今天帮朋友做课程设计, 要用 RMI 远端操控数据库. 于是乎便看了一下 RMI 应用的用法规则. 发现十分简单. 在这里写下一个 HelloWorld 例子, 以便未来参考.
<blockquote>引言: 白痴的我明明知道 RMI 底层是 Socket 实现的, 传递的对象固然要序列化. 但是今天我竟然傻逼地把 Connection 传导客户端操作... 小朋友不要学我变成白痴哦!</blockquote>
<strong>一. 结构(我叫他规则):</strong>
一个接口, 一个实现类. 一个服务器端, 一个客户端. 总共三类一接口.

<strong>二. 代码:</strong>
{% codeblock lang:java %}
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Product extends Remote {
    public String getName() throws RemoteException;
}
{% endcodeblock %}
{% codeblock lang:java %}
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ProductImpl extends UnicastRemoteObject implements Product {
    
    private String name;
    
    public ProductImpl(String name) throws RemoteException {
        this.name = name;
    }

    public String getName() throws RemoteException {
        System.out.println("方法 getName 被调用！");
        return name;
    }
    
}
{% endcodeblock %}
{% codeblock lang:java %}
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {

    public static void main(String[] args) {
        try {
            Registry r = LocateRegistry.createRegistry(1099);
            Product p = new ProductImpl("乐事薯片"); //我的最爱
            r.bind("p", p);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
{% endcodeblock %}
{% codeblock lang:java %}
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
public static void main(String[] args) {
        try {
            String host = ""; //这里替换成你的服务器地址, 空的就代表本机
            Registry r = LocateRegistry.getRegistry(host);
            Product p = (Product)r.lookup("p");
            System.out.println("此产品的名字为：" + p.getName());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
{% endcodeblock %}

<strong>三. 执行:</strong>
<em>1. 放置</em>
将上述 4 个类放置在统一文件夹下.
<em>2. 编译</em>
<code>javac -cp . *.java</code>
<em>3. 启动服务器端</em>
启动一个终端, 进入该文件夹, 执行:
<code>java -cp . Server</code>
<em>4. 启动客户端</em>
启动一个终端, 进入该文件夹, 执行:
<code>java -cp . Client</code>

四. 注意
编码问题一直存在, java 编译也不例外! 在 Linux 这些 UTF-8 的世界里请大家把上面四个文件都保存成 UTF-8 格式. Windows 的世界里, 保存成 ANSI 即可!
