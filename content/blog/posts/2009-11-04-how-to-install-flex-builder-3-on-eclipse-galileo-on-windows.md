---
title: How to install Flex Builder 3 on Eclipse Galileo on Windows
author: matt
type: post
date: 2009-11-03T23:00:04+00:00
url: /blog/2009/11/04/how-to-install-flex-builder-3-on-eclipse-galileo-on-windows/
categories:
  - software
tags:
  - eclipse
  - flex

---
#### Do you get an error when you try to install Flex Builder?
![](/wp-content/uploads/2009/11/flex-error.png)

Ignore it and carry on anyway.

Edit the file:

`[eclipse]\links\com.adobe.flexbuilder.feature.core.link`

and just stick “path=” at the start so it looks something like this:

`path=C:/Program Files/Adobe/Flex Builder 3 Plug-in`

Thanks to [greylurk](http://greylurk.com/index.php/2009/06/getting-flex-builder-3-plugin-to-survive-a-new-eclipse-version/) for the original tip.
