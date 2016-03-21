require 'fileutils'

DIR = File.expand_path('../..', __FILE__)
OLD_DIR = "#{DIR}/old_posts/jekyll"

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

  puts title.inspect
end
