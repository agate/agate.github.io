# require 'fileutils'

# DIR = File.dirname(__FILE__)

# Dir['old/*'].map do |x|
  # x.sub('old/', '')
# end.each do |name|
  # match = name.match(/(\d+)-(\d+)-(\d+)-(.+)/)
  # year = match[1]
  # month = match[2]
  # day = match[3]
  # file = match[4]

  # FileUtils.mkdir_p("#{DIR}/source/_posts/#{year}")
# end

# Dir['source/_posts/*'].each do |x|
  # content = File.read(x)
  # all = content.scan /\{\%\s*highlight\s+[^\s]+\s*\%\}/
  # unless all.empty?
    # content.gsub!(/\{\%\s*highlight\s+([^\s]+)\s*\%\}/, '{% codeblock lang:\1 %}')
    # content.gsub!(/\{\%\s*endhighlight\s*\%\}/, "{% endcodeblock %}")
    # File.write(x, content)
    # puts "updated: #{x}"
  # end
# end
