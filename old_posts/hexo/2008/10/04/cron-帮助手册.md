---
title: "cron 帮助手册"
date: 2008-10-04
tags:
---

最近写一个应用在 linux 环境下运行, 需要在用户生日的时候发送组合邮件. 查阅了很多, bbs 上也提问了很多还是没有比较好的解决方案. 只好听从 chinaonrails 大侠们的建议使用 cron 工具定时执行脚本来解决. 这个东西比较陌生(说白了就是微软视窗的计划任务...). 我还是记下来免得忘记.

主要翻译 Linux Help 下的 <a href="http://www.linuxhelp.net/guides/cron/">Cron Help Guide</a>

cron 一词源于希腊单词 chronos , 意为"时间", 这里说到的 cron 是 linux 系统下一个自动执行指定任务的程序. 例如, 你想在每晚睡觉期间创建某些文件或文件夹的备份, 就可以用cron来自动执行.

cron 将他的任务项目存储在 crontab (cron table) 文件里. 一般来说这个文件存放在你的 /etc 目录下. 有可能不同的系统位置不一样, 自己研究咯. 编辑用户的 crontab 任务项目可以通过在终端中键入 <span style="color: #3366ff;">crontab -e</span>. 在执行 'crontab -e' 时的默认编辑器是 VI. 当然你可以通过在终端中键入 <span style="color: #3366ff;">export VISUAL='editor_name'</span> 来改变默认编辑器, 并使用你喜欢的编辑器替代.

在我的 /etc/crontab 文件里有以下两行任务项目. 第一条是让我的爱机在晚间备份我 /etc 目录. 第二条是执行 Analog 程序用于计算我的 <a href="http://www.analog.cx/">web</a> 服务器的状态.

<span style="color: #3366ff;">12 3 * * * root tar czf /usr/local/backups/daily/etc.tar.gz /etc &gt;&gt; /dev/null 2&gt;&amp;1
52 5 * * * root /usr/local/src/analog-5.32-lh/analog &gt;&gt; /dev/null 2&gt;&amp;1</span>

以下是 cron 语句中的字段与字段含义:
<table border="1" cellspacing="0" cellpadding="5" bordercolor="#000000">
<tbody>
<tr>
<th align="center">字段</th>
<th align="center">含义</th>
</tr>
<tr>
<td width="50" align="center">1</td>
<td>分钟 (0-59)</td>
</tr>
<tr>
<td align="center">2</td>
<td>小时 (2-24)</td>
</tr>
<tr>
<td align="center">3</td>
<td>日期 (1-31)</td>
</tr>
<tr>
<td align="center">4</td>
<td>月份 (1-12, Jan, Feb, etc)</td>
</tr>
<tr>
<td align="center">5</td>
<td>星期几 (0-6, 0 = Sunday, 1 = Monday etc or Sun, Mon, etc)</td>
</tr>
<tr>
<td align="center">6</td>
<td>用户名(执行这个任务项目的时候用此用户身份)</td>
</tr>
<tr>
<td align="center">7</td>
<td>要执行的命令</td>
</tr>
</tbody></table>
就拿我那个 crontab 文件的第一行来说吧:

<span style="color: #3366ff;">12 3 * * * root tar czf /usr/local/backups/daily/etc.tar.gz /etc &gt;&gt; /dev/null 2&gt;&amp;1</span>

这个任务项目将在每天 3:12am 的时候执行 "tar czf /usr/local/backups/daily/etc.tar.gz /etc". 而后面跟的那个 "&gt;&gt; /dev/null 2&gt;&amp;1" 表示把所有的标准输出发送到 /dev/null (linux 的回收站), 同时把标准错误输出(2)发送到和标准输出(1)同样的地方(就是那个 /dev/null). 说白了这行任务项目不会产生任何输出!

另外这里有一个难一些的例子:

<span style="color: #3366ff;">30 15 13 6 1 * root tar czf /usr/local/backups/daily/etc.tar.gz /etc &gt;&gt; /dev/null 2&gt;&amp;1</span>

这个任务项目将在6月13日星期一的 3:30pm 执行 "tar czf /usr/local/backups/daily/etc.tar.gz /etc". 你也可以通过下面这条任务项目达到同样效果

<span style="color: #3366ff;">30 15 13 Jun Mon * root tar czf /usr/local/backups/daily/etc.tar.gz /etc &gt;&gt; /dev/null 2&gt;&amp;1</span>

如果你以 joey 的身份在没个小时的第 15 分钟的时候执行一条命令时你可以使用类似下面的这条任务项目:

<span style="color: #3366ff;">15 * * * * joey /usr/bin/somecommand &gt;&gt; /dev/null 2&gt;&amp;1</span>

上面这些例子里的 '*' 号表示 cron 在这个字段会不理会这些东西.

如果你想让一条命令每两小时执行一次, 你可以把任务项目的 '小时' 字段设置为 '<span style="color: #3366ff;">*/2</span>' 这个值. 这将让命令在 2am, 4am, 6am... 2pm, 4pm... 的时候执行. 例子如下:

<span style="color: #3366ff;">* */2 * * * joey /usr/bin/somecommand &gt;&gt; /dev/null 2&gt;&amp;1</span>

在 cron 中使用逗号 ',' 来在一个字段中指定多个时间. 如果你想让一个命令在每小时的第 15 分钟和第 30 分钟执行, 你可以在分钟字段中输入 '<span style="color: #3366ff;">15,30</span>'. 例子如下:

<span style="color: #3366ff;">15,30 * * * * joey /usr/bin/somecommand &gt;&gt; /dev/null 2&gt;&amp;1</span>

如果你先在每个月的第一周执行一个任务项目的话你可以在 '日期' 字段中填入 <span style="color: #3366ff;">1-7</span> (即表示第一天到第七天). 例子如下:

<span style="color: #3366ff;">15,30 */2 1-7 * * joey /usr/bin/somecommand &gt;&gt; /dev/null 2&gt;&amp;1</span>

这样在每个月的前七天(第一周)的每一天的偶数小时的一刻钟和半点的时候 (2:15, 2:30, 4:15, 4:30 etc) 执行somecommand 这个命令.

如果你想要 cron 在每天的 4:18pm 执行一个脚本集合, 那么你可以把所有这些脚本放在同一个文件夹(比如, /home/username/cron) 并且把写列这行加入你的 crontab 中:

<span style="color: #3366ff;">18 16 * * * root run-parts /home/username/cron &gt;&gt; /dev/null 2&gt;&amp;1
</span>

如果你希望保存下一个命令产生的命令行输出你可以将原来任务项目中的 <span style="color: #3366ff;">&gt;&gt; /dev/null 2&gt;&amp;1</span> 替换成 <span style="color: #3366ff;">&gt;&gt; /home/user/somecommand.log 2&gt;&amp;1</span>

当你添加完你需要的所有任务项目之后, 你可以通过 <span style="color: #3366ff;">crontab -l</span> 这个命令来列出它们.

如果你想要删除你的 crontab 文件, 你可以调用命令 <span style="color: #3366ff;">crontab -r</span> 来删除它.

你可以使用 root 用户身份来编辑某个特定的 crontab 文件, 只许运行 <span style="color: #3366ff;">crontab -e -u username</span>

你看! cron 是一个用起来十分舒适又十分强大的一个工具, 为每一个系统管理员提供优秀的自动化任务功能!

<hr />
<blockquote>最后我这里总结一下
&nbsp;1. 查看当前用户的cron配置，使用 crontab -l
&nbsp;2. 编辑当前用户的cron配置，使用 crontab -e
&nbsp;3. 删除当前用户的cron配置，使用 crontab -r
&nbsp;4. 以root身份查看/编辑/删除某用户的cron配置，在命令后加上 -u username
&nbsp;5. 配置系统级的任务，编辑 /etc/crontab 文件</blockquote>
