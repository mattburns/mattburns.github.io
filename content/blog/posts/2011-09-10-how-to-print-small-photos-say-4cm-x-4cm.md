---
title: How to print small photos (say, 4cm x 4cm)
author: matt
type: post
date: 2011-09-10T12:36:49+00:00
url: /blog/2011/09/10/how-to-print-small-photos-say-4cm-x-4cm/
categories:
  - Uncategorized

---
If you have a photo you want to put into a small frame, you may struggle finding a print company that print photos smaller than 15cm x 10cm (6"x4").

The simple answer is to create add a white border to your jpeg and print that. Then you can just trim the edges off the print. I just tried this and it was harder than I would have liked. If you open your photo in some software and expand the canvas, you’ll find it will start eating lots of memory. On my little laptop it became impossible to use.

**Update: Much easier way with new free website:**

[www.oddprints.com][1]

You can use that site for any size frame like 2"x2" or whatever. Simple!

If you like pain, here’s the old command-line way:

  1. Install [imagemagick](http://www.imagemagick.org/script/index.php). It’s free and very powerful.
  2. Open a command prompt (on windows: Start > Run > “cmd”)
  3. Type the following command (replace the path to convert.exe and input.jpg filename as necessary):

`“C:\Program Files\ImageMagick-6.6.0-Q16\convert.exe” input.jpg -border 137.5%x75%  output.jpg`

This example only work with square input photos. Here’s a table to help you work out how to print other sizes. If you have a size you want me to add, just drop a comment.

| input ratio | desired print size | border to add | print size to order |
| ----------- | ------------------ | ------------- | ------------------- |
| 1:1         | 4cm x 4cm          | 137.5%x75%    | 15cm x 10cm         |
| 3:2         | 6cm x 4cm          | 75%x75%       | 15cm x 10cm         |

 [1]: http://www.oddprints.com "OddPrints"