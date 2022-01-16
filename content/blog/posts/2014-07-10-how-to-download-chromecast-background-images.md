---
title: How to download Chromecast background images
author: matt
type: post
date: 2014-07-10T11:35:40+00:00
url: /blog/2014/07/10/how-to-download-chromecast-background-images/
cover:
    image: /wp-content/uploads/2014/07/01_MG_3677-672x372.jpg
categories:
  - Uncategorized

---
Google’s friendly little [chromecast][1] has some [great background images][2].

If you want to download all of those images so you can have a nice high quality screen saver on your laptop/mobile etc. just do this:

    git clone -b patch-1 https://github.com/mattburns/chromecast-backgrounds.git
    cd chromecast-backgrounds/
    npm install lodash q request nopt chalk
    node cli.js --download=images --size=1024 --load=backgrounds.json

Change the size from 1024 to whatever maximum size you want to download.

I had to tweak the source from [this project on github][3]. Hopefully my fork will get folded in.

 [1]: www.chromecast.com
 [2]: https://clients3.google.com/cast/chromecast/home/v/c9541b08 "Chromecast background"
 [3]: https://github.com/dconnolly/chromecast-backgrounds