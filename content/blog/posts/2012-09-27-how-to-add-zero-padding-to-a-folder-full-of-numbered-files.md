---
title: How to add zero-padding to a folder full of numbered files
author: matt
type: post
date: 2012-09-27T11:13:06+00:00
url: /blog/2012/09/27/how-to-add-zero-padding-to-a-folder-full-of-numbered-files/
categories:
  - Uncategorized

---
Have you got a folder of files that look like this?  

    file_1.png
    file_2.png
    file_3.png
    file_10.png
    file_11.png
    file_12.png
    file_100.png

But what you really want this:  

    file_001.png
    file_002.png
    file_003.png
    file_010.png
    file_011.png
    file_012.png
    file_100.png


Then, my linux-loving friend, run this:  

    rename 's/\d+/sprintf("%03d",$&)/e' *.png