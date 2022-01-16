---
title: 4 reasons to design your logo in CSS (and a few why you shouldn’t)
author: matt
type: post
date: 2013-02-24T19:22:08+00:00
url: /blog/2013/02/24/4-reasons-to-design-your-logo-in-css-and-a-few-why-you-shouldnt/
categories:
  - Uncategorized

---
## Intro

I recently changed the [OddPrints][1] logo on the website from an image to simple text styled with CSS and [@font-face][2]. To me it seems like the obvious thing to do but very few websites seem to employ the technique. I thought I’d explain my thoughts and I’d love to hear what you think…

## 1 – Sharper

This is the main reason. I recently bought a Retina MacBook Pro and the screen quality is amazing. I like to think I’m an optimist and I would normally just be happy with the obvious upgrade. The reality is that I mainly notice the apps and graphics that are not “retina ready” and just look soft and fuzzy. This in turn makes me feel dirty that I have to interact with something so dated and stupid. Here is an exaggerated example of what my logo looked like when zoomed in.

[![](/wp-content/uploads/2013/02/Screen-Shot-2013-02-20-at-21.29.08.png)][3]

and now using @font-face…[![](/wp-content/uploads/2013/02/Screen-Shot-2013-02-20-at-21.28.42.png)][4]

For a programming geek, I am relatively late to stumping up the cash to join The Retina Revolution. Until now, I was blissfully unaware that work needed to be done to make your site shine on such a device. If you don’t own a retina device, pop in your local fruit shop, grab a retina macbook pro and browse a few websites. It won’t take you long to find a website that has a logo or icons that look noticibly fuzzy next to that the razor-sharp text in the body. I hope it’s not your site. [People much smarter than me][5] agree that you should make sure your logo and icons look good on such a display. The recent launch of the [Chromebook Pixel][6] should be further evidence that we’re on the brink of a future with more pixels.

## 2 – SEO

This should be obvious but images aren’t as simple as text when it comes to being indexed by Google. Keeping things as plain html markup means I don’t have to worry about sensible alt attributes or whatever. You can still cut-and-paste the text which is handy sometimes (but not so handy that it deserves its own section, jeez). This isn’t a big reason, more a bonus feature.

## 3 – Internationalisation

If you happen to write [an awesome website][7] that is used by people around the world, they probably want to read it in their language. I can’t be bothered to internationalise my sites when Google translate does such a good job. I recently saw a [French blog post][8] and this screenshot made me look twice:[![](/wp-content/uploads/2013/02/objet-volé-2.jpg)][9]

Now, of course this could be seen as a bad thing if your logo is poorly translated or your branding is so important that you need full control of the exact appearance. As I’m writing this, the more I’m going off this point. It not like my url changes so why should my logo… thoughts please!

## 4 – Accessibility

<h1>Awesome Homepage</h1> is about as simple as it gets for html markup. If you’re blind or using some obscure text-based web browser, this is handy.

## Cons

Legacy browser support is sketchy. Initial page load may be slower if using javascript or the font files are big. You may experience a [flash of un-styled text][10] in some browsers. These problems can all be reduced with crazy tweeks like only including the characters you need in the font file, or base64 encoding them in the css. Tools such as [fontsquirrel][11], [Google’s web fonts][12] (and [loader][13]) solve most things, but even that takes a little reading just to get your head around. This all boils down to the same con: It’s hard to get right. Of course, if you’re already using web fonts elsewhere on your site, you’ve already solved these problems 😉

## Alternatives

If you still want to serve images, and I’m not putting forward a fantastic argument why you shouldn’t, I strongly recommend serving higher-resolution alternatives to displays that need them. It’s pretty simple to do with libraries such as [retina.js][14]. For example, when on my laptop, [microsoft.com][15] serves me a nice [high resolution version of their logo][16]. Fail to do this and your site just lost 5 subconscious quality points in your customer’s noggin.

You could also just upload your [logo as a vector image][17]. Similar problems with browser support but certainly a valid option.

## Conclusion

Designing your logo as a simple font that can be rendered in a browser isn’t for everyone. Big companies pay designers to draw clever graphics that need more than just a font file, and many websites care more about appearing the same on as many devices and browsers as possible. If however you just want something that looks great on most platforms but you care more about impressing those visitors on modern, expensive devices, maybe a font-face/css/svg logo is for you.

 [1]: http://www.OddPrints.com
 [2]: https://developer.mozilla.org/en-US/docs/CSS/@font-face
 [3]: http://www.mattburns.co.uk/blog/wp-content/uploads/2013/02/Screen-Shot-2013-02-20-at-21.29.08.png
 [4]: http://www.mattburns.co.uk/blog/wp-content/uploads/2013/02/Screen-Shot-2013-02-20-at-21.28.42.png
 [5]: http://www.youtube.com/watch?v=WhZpKdQcKhU&t=13m51s "Discussion about retina-ready images"
 [6]: http://www.google.co.uk/intl/en/chrome/devices/chromebook-pixel
 [7]: http://www.stolencamerafinder.com
 [8]: http://www.pixelistes.com/blog/stolen-camera-finder-un-moyen-de-retrouver-sur-internet-des-cliches-pris-avec-votre-appareil-photo/
 [9]: http://www.mattburns.co.uk/blog/wp-content/uploads/2013/02/objet-volé-2.jpg
 [10]: http://paulirish.com/2009/fighting-the-font-face-fout/
 [11]: http://www.fontsquirrel.com/tools/webfont-generator
 [12]: http://www.google.com/webfonts
 [13]: https://developers.google.com/webfonts/docs/webfont_loader
 [14]: http://retinajs.com/
 [15]: http://www.microsoft.com/
 [16]: http://i.s-microsoft.com/global/ImageStore/PublishingImages/logos/hp/logo-lg-2x.png
 [17]: http://dbushell.com/2010/06/30/using-svg-logos/