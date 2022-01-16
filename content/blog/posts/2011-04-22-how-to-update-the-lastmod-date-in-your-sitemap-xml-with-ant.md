---
title: How to update the lastmod date in your sitemap xml with Ant
author: matt
type: post
date: 2011-04-22T03:39:34+00:00
url: /blog/2011/04/22/how-to-update-the-lastmod-date-in-your-sitemap-xml-with-ant/
categories:
  - Uncategorized

---
Hmm, you want to add the “lastmod” node, but you’re too lazy to ever keep that up to date so you decide to update it with your Ant script whenever you deploy. Easy.

So you’ve just written a [valid][1] sitemap.xml file for your website because [Google said it was a good idea][2]. Great.

```
&lt;?xml version="1.0" encoding="UTF-8" standalone="no"?&gt;
&lt;urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"&gt;
   &lt;url&gt;
      &lt;loc&gt;http://www.stolencamerafinder.com/&lt;/loc&gt;
      &lt;lastmod&gt;2011-04-21&lt;/lastmod&gt;
      &lt;changefreq&gt;weekly&lt;/changefreq&gt;
   &lt;/url&gt;
&lt;/urlset&gt;
```

First, you’ll need the jar for a third-party Ant task called [XMLTask][3]. Once you have that, the ant target you’ll need is simply:

```
&lt;taskdef name="xmltask" classname="com.oopsconsultancy.xmltask.ant.XmlTask" classpath="test-lib/xmltask.jar"/&gt;
&lt;target name="update-sitemap" description="update the update date"&gt;
	&lt;tstamp&gt;
	    &lt;format property="today" pattern="yyyy-MM-dd" locale="en,UK"/&gt;
	&lt;/tstamp&gt;
    &lt;xmltask source="war/sitemap.xml" dest="war/sitemap.xml" standalone="yes" report="true"&gt;
        &lt;replace path="/:urlset/:url/:lastmod/text()" withText="${today}"/&gt;
    &lt;/xmltask&gt;
&lt;/target&gt;
```

Yeah yeah, this is kid’s stuff, why blog about it? Well, embarrassingly, it took me 3 hours of [messing around][4] to get it working. If I don’t write it down somewhere, I’ll only forget the next time I need to do this. Sigh.

 [1]: http://www.sitemaps.org/protocol.php
 [2]: https://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=156184
 [3]: http://www.oopsconsultancy.com/software/xmltask/
 [4]: http://stackoverflow.com/questions/5739210/how-to-update-an-xml-document-with-ant