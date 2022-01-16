---
title: How to detect browser support for File Api and drag and drop with javascript
author: matt
type: post
date: 2011-04-17T11:55:12+00:00
url: /blog/2011/04/17/how-to-detect-browser-support-for-file-api-and-drag-and-drop-with-javascript/
categories:
  - Uncategorized
tags:
  - html5
  - javscript

---
Here’s a bit of info for you crazy HTML5 kids. You’ll need to include the handy [Modernizr][1] script for it to work.

```
var browserIsSupported = !!window.FileReader && Modernizr.draganddrop;
```

<address>
  If you want see it in action, just visit [stolencamerafinder](https://www.stolencamerafinder.com/) 😉
</address>

<address>
  I’ve tested this in Firefox 3.6, Chrome 10, IE8, Safari 5 and Opera 11. The only browsers from that list to support FileReader from the File API and the drag and drop events are FF and Chrome.
</address>

<address>
  Let’s hope the other catch up soon…
</address>

 [1]: http://www.modernizr.com/