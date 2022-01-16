---
title: Generating a CMYK file for printing
author: matt
type: post
date: 2015-05-12T13:11:14+00:00
url: /blog/2015/05/12/generating-a-cmyk-file-for-printing/
categories:
  - Uncategorized

---
So you want to print something (like a banner) but the printers have asked for it to be int the CMYK colorspace? Well we could argue about how to spell colour or [whether CMYK is a colorspace][1] at all. But I can’t be bothered, let’s just cut and paste this command which is what I came up with after a morning of hacking…

```
convert -resize 9520 -density 300 rgb_input.pdf +profile icm -profile sRGB_IEC61966-2-1_black_scaled.icc -profile SWOP2006_Coated3v2.icc -quality 85 cmyk_output.jpeg
```

Importantly, rgb_input.pdf was exported with [scribus][2] using the output mode for screen.

Here are some dependencies for you macboy:

```
brew install ghostscript
brew install imagemagick --with-little-cms
brew cask install xquartz
brew cask install inkscape
brew cask install scribus
```

You’ll find ICC profiles [here][3].

Yes, this is another blog just for my personal notes 😉

**UPDATE** for [moo.com][4] users:

[Moo suggest][5] you upload media with the ‘Coated FOGRA39’ ICC profile. You can find it in [this zip file here][6]. Moo also have some [suggested resolutions for uploaded media][7] although I just multiplied those up a bit to make sure the quality was extra high just in case.

```
convert -resize 6192 -density 600 rgb_input.pdf +profile icm -profile sRGB_v4_ICC_preference.icc -profile CoatedFOGRA39.icc -quality 85 cmyk_output.jpeg
```

**BONUS!** : If this blog post was useful to you, [here’s my moo.com referral link][8] which will bag you £10 off your first order 😉

 [1]: http://www.imagemagick.org/Usage/formats/#color_profile
 [2]: http://wiki.scribus.net/canvas/Scribus
 [3]: http://www.color.org/srgbprofiles.xalter
 [4]: https://www.moo.com/
 [5]: https://support.moo.com/hc/en-gb/articles/202941410-Design-Colour-Settings
 [6]: http://supportdownloads.adobe.com/detail.jsp?ftpID=3680
 [7]: https://support.moo.com/hc/en-gb/articles/202677204-Design-Size-and-Resolution
 [8]: https://refer.moo.com/s/rdpyj