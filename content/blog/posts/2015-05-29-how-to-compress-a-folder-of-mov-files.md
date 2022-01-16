---
title: How to compress a folder of .mov files
author: matt
type: post
date: 2015-05-29T13:06:16+00:00
url: /blog/2015/05/29/how-to-compress-a-folder-of-mov-files/
categories:
  - Uncategorized

---
Made a bunch of .movs using quicktime’s screen recording but they’re a bit big? ffmpeg’s default settings when converting to mp4 is a quick win

    for i in *.mov; do ffmpeg -i $i $i.mp4; done

Name them alphabetically and you can merge them all together:

    ffmpeg -f concat -i <(printf "file '$PWD/%s'\n" ./*.mp4) -c copy merged.mp4
