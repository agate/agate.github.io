---
title: "Douban -> \"I say\" API"
date: 2008-09-01
tags:
---

today i saw a Jason Torres said on http://www.mashupgarage.com/ that he write a <a href="http://pastie.org/262494">Plurk Post API</a>. it use the Mechanize on ruby! it's great! and thanks for the idea, i code a douban "i say" api by myself!

{% codeblock lang:ruby %}
##
# Douban API Power by Mechanize
# http://agatezone.cn
# by agate.
#

require 'rubygems'
require 'mechanize'

class Douban

  @username = ''
  @password = ''

  @agent = nil


  def initialize(username, password)
	@username = username
	@password = password

	@agent = WWW::Mechanize.new { |a|
	  a.user_agent_alias = 'Mac Safari' 
	}
  end

  def send_message(message)

	@agent.get('http://www.douban.com') do |douban|

	  my_page = douban.form_with(:action => '/login') do |form|
		form.form_email = @username
		form.form_password = @password
	  end.submit

	  post_params = { :mb_text => message }
	  @agent.post('http://www.douban.com/mine/miniblogs', post_params)

	end

  end

end

DOUBAN_USERNAME = 'your-email'
DOUBAN_PASSWORD = 'your-password'

# Usage
douban = Douban.new(DOUBAN_USERNAME, DOUBAN_PASSWORD)
douban.send_message('test')
{% endcodeblock %}
