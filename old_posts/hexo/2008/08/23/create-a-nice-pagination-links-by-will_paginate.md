---
title: "Create a nice pagination links by will_paginate"
date: 2008-08-23
tags:
---

"will_paginate" is a rails plugin for helping developer to create the pagination links. use it, you can very easily to make a nice pagination links.

<strong>usage:</strong>
<span style="color: #339966;">It’s very easy to do pagination on ActiveRecord models:</span>
<code>cattr_reader :per_page
@@per_page = 5  <span style="color: #339966;">#modify this</span></code>
<span style="color: #339966;">It’s also very easy to make a on Controller:</span>
<code>@posts = Post.paginate :page =&gt; params[:page], :order =&gt; &#39;created_at DESC&#39;</code>
<span style="color: #339966;">In the view, page links can be rendered with a single view helper:</span>
<code>&lt;%= will_paginate @posts %&gt;</code>

Homepage: <a href="http://github.com/mislav/will_paginate/wikis">http://github.com/mislav/will_paginate/wikis</a>
Clone URL: <a href="git://github.com/mislav/will_paginate.git">git://github.com/mislav/will_paginate.git</a>
Doc URL: <a href="http://mislav.caboo.se/static/will_paginate/doc/">http://mislav.caboo.se/static/will_paginate/doc/</a>
