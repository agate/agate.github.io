---
title: "mysql中的一些命令"
date: 2007-09-03
tags:
---

1. 导出整个数据库

    mysqldump -u 用户名 -p 数据库名 > 导出的文件名
    mysqldump -u root -p root > bak_db.sql

2. 导出一个表

    mysqldump -u 用户名 -p 数据库名 表名> 导出的文件名
    mysqldump -u root -p root users> bak_table.sql

3. 导出一个数据库结构

    mysqldump -u root -p -d --add-drop-table root >d:\bak_struts.sql
    # -d 没有数据
    # --add-drop-table 在每个create语句之前增加一个drop table

4. 导入数据库
进入mysql数据库控制台

    mysql>source d:\bak.sql
