require 'fileutils'

DIR = File.expand_path('../..', __FILE__)
OLD_DIR = "#{DIR}/old_posts/jekyll"
NEW_DIR = "#{DIR}/old_posts/hexo"

Dir["#{OLD_DIR}/*"].map do |x|
  match = x.match(/#{OLD_DIR}\/(\d+)-(\d+)-(\d+)-(.+)\.md/)
  year = match[1]
  month = match[2]
  day = match[3]
  filename = match[4]
  new_dir = "#{NEW_DIR}/#{year}/#{month}/#{day}"
  new_file = "#{new_dir}/#{filename}.md"
  content = File.read(x)
  title = content.match(/title:\s*(.+)$/)[1]

  # replace highlight -> codeblock
  all = content.scan /\{\%\s*highlight\s+[^\s]+\s*\%\}/
  unless all.empty?
    content.gsub!(/\{\%\s*highlight\s+([^\s]+)\s*\%\}/, '{% codeblock lang:\1 %}')
    content.gsub!(/\{\%\s*endhighlight\s*\%\}/, "{% endcodeblock %}")
  end

  # update title
  content.gsub!(/^\s*---.+?---/m, <<-END)
---
title: #{title}
date: #{year}-#{month}-#{day}
tags:
---
  END

  FileUtils.mkdir_p(new_dir)
  File.write(new_file, content)
end
