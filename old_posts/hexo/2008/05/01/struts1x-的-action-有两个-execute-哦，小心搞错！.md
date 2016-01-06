---
title: "Struts1.x 的 Action 有两个 execute 哦，小心搞错！"
date: 2008-05-01
tags:
---

不知道各位使用 Struts1.x 的朋友们晓得不晓得，Struts1.x 的 org.apache.struts.action.Action 中有两个 execute 方法，在我们使用 eclipse 的自动完成 override 功能的时候要是不小心给弄错了你就等着迎接一个不报错的空白页面吧！让我们看看代码：
[source language="java"]
// one execute
public ActionForward execute(ActionMapping mapping, ActionForm form,
	HttpServletRequest request, HttpServletResponse response) {
	//code...
}
// another execute
public ActionForward execute(ActionMapping mapping, ActionForm form,
	ServletRequest request, ServletResponse response) {
	//code...
}
[/source]
好，公布结果！只有 override 上面这个 execute 才能起作用。如果你 override 的是下面这个 execute 的话，很不幸，您调用这个 action 的时候响应给你的是一个空白的页面，你也别想得到任何 exception 的提示！

在 eclipse 中我导入了 struts1.x 的 src 路径，并通过 Open Call Hierarchy 查找调用上面第二个 execute 的类时发现竟然没有调用者！换句话说当我们实现第二个 execute 的时候(没有实现第一个 execute )，是根本没用的！程序根本不会调用到我们 override 的那个 execute 只会傻傻地调用第一个 execute 的默认实现，返回一个 null

那第二个 execute 有什么用呢？我觉得他不是用来给我们重写的，看看它的内容：
[source language="java"]
public ActionForward execute(ActionMapping mapping, ActionForm form,
	ServletRequest request, ServletResponse response)
	throws Exception {
	try {
		return execute(mapping, form,
			(HttpServletRequest) request,
			(HttpServletResponse) response);
	} catch (ClassCastException e) {
		return null;
	}
}
[/source]
在我看来，其实它是为了当一个请求是一个非 http 请求的时候，作为一个前端转换器，重新包装请求和响应，然后才交给真正的，也就是我们的第一个 execute 方法来实现。这个从 src 的注释中我们也可以比较清晰的了解：<blockquote>Process the specified non-HTTP request, and create the corresponding non-HTTP response (or forward to another web component that will create it), with provision for handling exceptions thrown by the business logic. Return an ActionForward instance describing where and how control should be forwarded, or <span style="color: #ff0000;">null</span> if the response has already been completed.</blockquote>
所以……当你重写这个 action 的 execute 方法时，注意咯！是重写那个参数是 http-request/response 的 execute哦！！！

这里严重鄙视一下 struts1.x 的编码态度！
