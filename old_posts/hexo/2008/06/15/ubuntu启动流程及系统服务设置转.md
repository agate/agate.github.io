---
title: "Ubuntu启动流程及系统服务设置[转]"
date: 2008-06-15
tags:
---

======== <strong>启动流程</strong> ========
Linux系统主要通过以下步骤启动： 
1、读取MBR的信息，启动Boot Manager Windows使用NTLDR作为Boot Manager，如果您的系统中安装多个版本的Windows，您就需要在NTLDR中选择您要进入的系统。 Linux通常使用功能强大，配置灵活的GRUB作为Boot Manager，我们将在启动管理章节中向您介绍它的使用方式。
2、加载系统内核，启动init进程 init进程是Linux的根进程，所有的系统进程都是它的子进程。
3、init进程读取"/etc/inittab"文件中的信息，并进入预设的运行级别，按顺序运行该运行级别对应文件夹下的脚本。脚本通常以"start"参数启动，并指向一个系统中的程序。 通常情况下，"/etc/rcS.d/"目录下的启动脚本首先被执行，然后是"/etc/rcN.d/"目录。例如您设定的运行级别为3,那么它对应的启动目录为"/etc/rc3.d/"。
4、根据"/etc/rcS.d/"文件夹中对应的脚本启动Xwindow服务器"xorg" Xwindow为Linux下的图形用户界面系统。
5、启动登录管理器，等待用户登录 Ubuntu系统默认使用GDM作为登录管理器，您在登录管理器界面中输入用户名和密码后，便可以登录系统。（您可以在"/etc/rc3.d/"文件夹中找到一个名为"S13gdm"的链接）

======== <strong>更改运行级别</strong> ========
在"/etc/inittab"文件中找到如下内容： # The default runlevel. id:2:initdefault: 这一行中的数字2,为系统的运行级别，默认的运行级别涵义如下： 0 关机 1 单用户维护模式 2~5 多用户模式 6 重启
<!--more-->
======== <strong>服务管理</strong> ========
======== <strong>更改启动服务</strong> ========
在运行级别对应的文件夹中，您可以看到许多文件名以"S##"和"K##"起始的启动脚本链接。例如： /etc/rcS.d/S35mountall.sh 挂载文件系统 /etc/rcS.d/S40networking 启用网络支持 /etc/rc2.d/S13gdm 启动登录管理器 /etc/rc2.d/S20makedev 创建设备文件 /etc/rc2.d/S23xinetd 启动超级进程 init进程将以"start"为参数，按文件名顺序执行所有以"S##"起始的脚本。脚本名称中的数字越小，它将被越早执行。例如在"/etc /rc2.d/"文件夹中，"S13gdm"文件名中的数字小于"S23xinetd","S13gdm"将比"S23xinetd"先执行。如果一个脚本链接，以"K##"起始，表示它将以"stop"参数被执行。如果相应服务没有启动，则不执行该脚本。例如： /etc/rc2.d/K20powernowd 针对某种硬件的电源管理支持如果您想禁止某一服务在启动时自动运行，您可以将相应运行级别中的脚本由"S##xxx"重命名为"K##xxx"。

======== <strong>手动控制服务</strong> ========
您也可以手动运行带有以下参数的启动脚本，来控制系统服务。 start 启动 stop 停止 restart 重启例如： /etc/rc2.d/K20powernowd start 有时您并不清楚当前运行级别，该运行级别下未必有相应脚本；而且此类脚本的前三位字符并不固定，不便于记忆。这时，您可以直接使用"/etc /init.d/"文件夹中的启动脚本（"/etc/rcX.d/"中的启动脚本链接到"/etc/init.d/"文件夹下相应脚本），这也是我们向您推荐的方式。例如： /etc/init.d/powernowd start Tips：以上命令的位置并没有包含在环境变量的搜索路径中，所以要输入完整路径。

======== <strong>常用系统服务</strong> ========
acpi-support 高级电源管理支持 acpid acpi守护程序.这两个用于电源管理，非常重要 alsa 声音子系统 alsa-utils anacron cron的子系统，将系统关闭期间的计划任务，在下一次系统运行时执行。 apmd acpi的扩展 atd 类似于cron的任务调度系统。建议关闭 binfmt-support 核心支持其他二进制的文件格式。建议开启 bluez-utiles 蓝牙设备支持 bootlogd 启动日志。开启它 cron 任务调度系统，建议开启 cupsys 打印机子系统。 dbus 消息总线系统(message bus system)。非常重要 dns-clean 使用拨号连接时，清除dns信息。 evms 企业卷管理系统（Enterprise Volumn Management system） fetchmail 邮件用户代理，用于收取邮件 gdm gnome登录和桌面管理器。 gdomap gpm 终端中的鼠标支持。 halt 别动它。 hdparm 调整硬盘的脚本，配置文件为"/etc/hdparm.conf"。 hibernate 系统休眠 hotkey-setup 笔记本功能键支持。支持类型包括： HP, Acer, ASUS, Sony, Dell, 和IBM。 hotplug and hotplug-net 即插即用支持，比较复杂，建议不要动它。 hplip HP打印机和图形子系统 ifrename 网络接口重命名脚本。如果您有十块网卡，您应该开启它 inetd 在文件"/etc/inetd.conf"中，注释掉所有你不需要的服务。如果该文件不包含任何服务，那关闭它是很安全的。 klogd 重要。 linux-restricted-modules-common 受限模块支持。"/lib/linux-restricted-modules/"文件夹中的模块为受限模块。例如某些驱动程序，如果您没有使用受限模块，就不需要开启它。 lvm 逻辑卷管理系统支持。 makedev 创建设备文件，非常重要。 mdamd 磁盘阵列 module-init-tools 从/etc/modules加载扩展模块，建议开启。 networking 网络支持。按"/etc/network/interfaces"文件预设激活网络，非常重要。 ntpdate 时间同步服务，建议关闭。 pcmcia pcmcia设备支持。 powernowd 移动CPU节能支持 ppp and ppp-dns 拨号连接 readahead 预加载库文件。 reboot 别动它。 resolvconf 自动配置DNS rmnologin 清除nologin rsync rsync守护程序 sendsigs 在重启和关机期间发送信号 single 激活单用户模式 ssh ssh守护程序。建议开启 stop-bootlogd 在2，3，4，5运行级别中停止bootlogd服务 sudo 检查sudo状态。重要 sysklogd 系统日志 udev &amp; udev-mab 用户空间dev文件系统（userspace dev filesystem）。重要 umountfs 卸载文件系统 urandom 随机数生成器 usplash 开机画面支持 vbesave 显卡BIOS配置工具。保存显卡的状态 xorg-common 设置X服务ICE socket。 adjtimex 调整核心时钟的工具 dirmngr 证书列表管理工具,和gnupg一起工作。 hwtools irqs优化工具 libpam-devperm 系统崩溃之后，用于修理设备文件许可的守护程序。 lm-sensors 板载传感器支持 mdadm-raid 磁盘陈列管理器 screen-cleanup 清除开机屏幕的脚本 xinetd 管理其他守护进程的一个inetd超级守护程序

======== <strong> 重要配置文件</strong> ========
无论任何情况下，在修改配置文件之前，请您先备份它！ 建议您使用这个命令："sudo cp xxx xxx_`date +%y%m%d_%H:%M`"。 当然这很麻烦，您可以新建一个名为"bak"的文件，内容如下： #!/bin/bash sudo cp $1 $1_`date +%y%m%d_%H:%M` 把它放在您能够记住的目录下，比如"/home"，执行命令"sh /home/bak xxx"，就可以将当前文件夹下的文件"xxx"另存为"xxx_yymmdd_HH:MM"的格式了

======== <strong>全局配置文件</strong> ========
系统初始化 /etc/inittab 运行级别、控制台数量 /etc/timezone 时区 /etc/inetd.conf 超级进程 文件系统 /etc/fstab 开机时挂载的文件系统 /etc/mtab 当前挂载的文件系统 用户系统 /etc/passwd 用户信息 /etc/shadow 用户密码 /etc/group 群组信息 /etc/gshadow 群组密码 /etc/sudoers Sudoer列表（请使用"visudo"命令修改此文件，而不要直接编辑） Shell /etc/shell 可用Shell列表 /etc/inputrc ReadLine控件设定 /etc/profile 用户首选项 /etc/bash.bashrc bash配置文件 系统环境 /etc/environment 环境变量 /etc/updatedb.conf 文件检索数据库配置信息 /etc/issue 发行信息 /etc/issue.net /etc/screenrc 屏幕设定 网络 /etc/iftab 网卡MAC地址绑定 /etc/hosts 主机列表 /etc/hostname 主机名 /etc/resolv.conf 域名解析服务器地址 /etc/network/interfaces 网卡配置文件

======== <strong>用户配置文件</strong> ========
"/etc/"目录下的所有文件，只有root用户才有修改权限。应用软件的全局配置文件，普通用户也不能够修改，如果您想配置软件，以适应您的需求，您可以修改它的用户配置文件。用户配置文件通常为全局配置文件的同名隐藏文件，放在您的$HOME目录下，例如： /etc/inputrc /home/user/.inputrc /etc/vim/vimrc /home/user/.vim/vimrc 也有少数例外，通常是系统程序 /etc/bash.bashrc /home/user/.bashrc
