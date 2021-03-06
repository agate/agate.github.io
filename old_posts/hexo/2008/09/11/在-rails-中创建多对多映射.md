---
title: "在 Rails 中创建多对多映射"
date: 2008-09-11
tags:
---

<blockquote>这里使用 rails 2.0 以上版本, 并使用 sqlite3 数据库. 本文提供两种常用建立多对多映射的方法.</blockquote>
<strong>第一种</strong>
首先, 创建一个 rails 工程并进入工程目录中!
<code>$rails demo
$cd demo</code>
接着让我们用 scaffold 建立两个资源 book 和 author. 在此我们可以这么理解: 一个作者可以写很多书, 一本书当然也可以有很多作者!
<code>$./script/generate scaffold book name:string
$./script/generate scaffold author name:string</code>
以上两句命令已经帮我们把 controller | model | view | migrate 建好了! 一般来说, 要实现多对多关系必须提供数据库中的一个中间表来实现. 在这里可以执行
<code>$./script/generate migration create_authors_books</code>
生成数据迁移文件, 并编辑db/migrate/xxx*_create_authors_books.rb:
<code>class CreateAuthorsBooks &lt; ActiveRecord::Migration
&nbsp;&nbsp;def self.up
&nbsp;&nbsp;&nbsp;&nbsp;create_table :authors_books, :id =&gt; false do |t|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.references :book
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.references :author
<span style="color: #339966;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 当然你可以使用原来的 integer 类型来引用 xxx_id
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# t.TYPE 这种是新的建表方式, 过去使用的是 t.column :column_name :type
</span>&nbsp;&nbsp;&nbsp;&nbsp;end
&nbsp;&nbsp;end
&nbsp;&nbsp;def self.down
&nbsp;&nbsp;&nbsp;&nbsp;drop_table :authors_books
&nbsp;&nbsp;end
end</code>
接下来我们只需要运行
<code>$rake db:migrate</code>
便可以把数据库(表: book|author|authors_books)也同时建好. 下面就是在 model 的代码中加入关系声明的代码咯! 对于多对多我们使用 has_and_belongs_to_many 方法!
<code><span style="color: #339966;"># app/models/book.rb</span>
class Book &lt; ActiveRecord::Base
&nbsp;&nbsp;has_and_belongs_to_many :authors
end</code>
<code><span style="color: #339966;"># app/models/author.rb</span>
class Author &lt; ActiveRecord::Base
&nbsp;&nbsp;has_and_belongs_to_many :books
end</code>
done! 这样就建立好二者的多对多关系了!
如何取呢? 其实就是对应地取其复数形式, 如一本书的多个作者就可以这么取 @post.authors 而一个作者的多本书同理 @author.books
问题是现在在我们的数据库里还没有数据, 为了方便起见可以自己使用 GUI 工具填入数据(记住包括 authors_books 表的数据哦! 这个是关联关系的关键!) 文章这里就不详细描述"如何填数据"咯!
现在由于我们使用 scaffold 来自动化地建立了 view 部分, 所以现在单单运行服务器并浏览页面是看不到实际效果的! 为讲述方便, 这里只对 book 的 index 视图进行修改, 在对应的地方根据下列格式进行修改:
<code> &lt;%=h("&lt;&lt;" + book.name + "&gt;&gt;") %&gt; ---
(
&lt;% book.authors.each do |author| %&gt;
&nbsp;&nbsp;&lt;%= author.name %&gt;
&lt;% end %&gt;
) </code>
这样所有工作就做完了! 在数据库数据已经建好的前提下, 浏览 <a href="http://localhost:3000/books" target="_blank">http://localhost:3000/books</a> 应该就可以看到类似的结果
<img src="/images/archive/2008/09/rails-many-to-many.png" alt="" />

<strong>第二种</strong>
相信第一种应该是大部分人使用的方法! 第二种只是另外一种实现(有的人觉得比较好理解).
就是使用 has_many :through
<code><span style="color: #339966;"># app/models/book.rb</span>
class Book &lt; ActiveRecord::Base
&nbsp;&nbsp;has_many :xxx_relationship
&nbsp;&nbsp;has_many :authors, :through => :xxx_relationship
end</code>
<code><span style="color: #339966;"># app/models/author.rb</span>
class Author &lt; ActiveRecord::Base
&nbsp;&nbsp;has_many :xxx_relationship
&nbsp;&nbsp;has_many :books, :through => :xxx_relationship
end</code>
<code><span style="color: #339966;"># app/models/xxx_relationship.rb</span>
class XxxRelationship &lt; ActiveRecord::Base
&nbsp;&nbsp;belongs_to :books
&nbsp;&nbsp;belongs_to :authors
end
<span style="color: #339966;"># 这种方法的特点就是需要在关系表中加入 belongs_to 的声明</span></code>
也许这个的好处就是在看起来更加细致, 控制得细致入微, 而且抛弃了"约定", 使得关系表随便命名即可. 有的人觉得这样好, 但是我更喜欢约定俗成的 Rails
