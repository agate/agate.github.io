---
title: "rails 多对多表名特点"
date: 2008-09-12
tags:
---

根据英文字母的顺序, 从 a 到 z 的方式. 如果有两个表叫做 posts 和 categories. 那么写这两个表的中间表的时候必须这么命名: "categories_posts". c 在 p 之前! 所以放在前边~ 如果不根据这个规矩命名就会发生找不到中间表的错误!
