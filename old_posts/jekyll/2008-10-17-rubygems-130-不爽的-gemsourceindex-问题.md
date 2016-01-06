--- 
layout: post
title: "rubygems 1.3.0 不爽的 Gem::SourceIndex 问题"
wordpress_id: 255
wordpress_url: http://www.agatezone.cn/code/?p=255
---
我原先的环境:
<blockquote>RUBYGEMS VERSION: 1.2.0
RAILS VERSION: 2.1.1</blockquote>
但是当我升级到 RUBYGEMS 1.3.0 的时候, 每当用命令行生成一些 rails 文件的时候就会报:
<blockquote>Gem::SourceIndex#search support for Regexp patterns is deprecated 2.1.1</blockquote>
十分不爽! 于是寻寻觅觅问题所在, 在鸟语网站上查了很多都是说是 RUBYGEMS 1.3.0 的问题, 只是一个提醒罢了, 无关痛痒的! 但是我看着就是十分不爽呀! 就想能不能降级到 RUBYGEMS 1.2.0 呢? 在 google 上找到了一个方法!
<code>$sudo gem install rubygems-update -v 1.2.0</code>
问题是我原来是从 RUBYGEMS 1.2.0 升级上来的, 于是我的系统里存在 RUBYGEMS 1.2.0 和 1.3.0 两个升级文件, 默认情况下执行 update_rubygems 会升级到最新版本(这不是我们期望的). 于是必须使用 gem uninstall 来卸最新的 1.3.0 rubygems.
<code>$sudo gem uninstall rubygems-update
会列出一个列表选择需要卸载的序号后回车即可!</code>
这样卸载之后再次执行:
<code>$sudo update_rubygems</code>
就可以降级回到原先的 RUBYGEMS 1.2.0 咯! 等到 rails 或者 rubygems 自己解决这个不爽的提示之后我们在升级吧!
<blockquote>Tips:
gem env
gem list</blockquote>
