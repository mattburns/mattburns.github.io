---
title: Running the 4K AOC U2868PQU and Intel HD4000 graphics…
author: matt
type: post
date: 2014-09-30T11:39:13+00:00
url: /blog/2014/09/30/running-the-4k-aoc-u2868pqu-and-intel-hd4000-graphics/
cover:
    image: /wp-content/uploads/2014/09/aoc-u2868pqu-672x372.jpg
categories:
  - Uncategorized

---
Ok, I just bought a 4K display, whoop!

I knew when I bought it that neither my [late-2012 Retina Macbook Pro][1], or my Ubuntu desktop machine would actually drive the monitor at 4K because they both rely on Intel’s HD4000 graphics which is built into their Ivy bridge CPUs. I did however expect to get at least 2560×1440 (if only at 30Hz) which is fine by me, and then I’m ready when I next upgrade…

## OSX

Unfortunately, I initially couldn’t get the Macbook to run at anything above 1080p (which looks horrible) (as you can see from [my stackexchange question][2]).

I then managed to get full 3840×2160 @30Hz using mini-displayport and an app called SwitchResX. Here are my custom settings, you need to reboot the machine to apply them:

![](/wp-content/uploads/2014/09/Screen-Shot-2014-09-30-at-16.42.52.png) 

As a word of warning, this does make things eye-bleedingly small. (Pretty cool though)

![](/wp-content/uploads/2014/09/Screen-Shot-2014-09-30-at-17.17.13.png) 

Personally, I found the ‘scaled’ resolution of 1920×1200 to be the best for me because it uses HiDPI to give you that retina feel you’re used to. It will look like 1920×1200 but actually use more pixels to paint it. Here are the settings:

![](/wp-content/uploads/2014/09/Screen-Shot-2014-09-30-at-17.09.01.png) 

This is much more sensible (although I would like it smaller to be honest):  
![](/wp-content/uploads/2014/09/Screen-Shot-2014-09-30-at-17.11.33.png) 

The downside is that you lose some of the screen down the sides. Let me know if you have any better suggestions.

If you find the colors going a bit funny, I used SwitchResX to change the color profile to sRGB IEC61966-2.1 like this:  
![](/wp-content/uploads/2014/09/Screen-Shot-2014-09-30-at-17.13.17.png) 

## Ubuntu

[Thanks to Linus himself][3], I was able to get 2560×1440 working on Ubuntu:

`xrandr --newmode 2560x1440_30.00 146.27 2560 2680 2944 3328 1440 1441 1444 1465 -HSync +Vsync<br />
xrandr --addmode HDMI2 "2560x1440_30.00"<br />
xrandr --output HDMI2 --mode "2560x1440_30.00"`

If you make any mistakes, you can remove them with:  
`xrandr --delmode HDMI2 "2560x1440_30.00"<br />
xrandr --rmmode 2560x1440_30.00`

That will have to do for now although I may buy another graphics card for the Ubuntu machine, suggestions welcome 🙂

 [1]: http://support.apple.com/kb/SP658
 [2]: http://apple.stackexchange.com/questions/147565/late-2012-rmbp-not-outputting-anything-above-1080p/
 [3]: https://plus.google.com/+LinusTorvalds/posts/HQsCY7ErAL4