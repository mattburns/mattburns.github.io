---
title: How to stop Google Chrome using your location when searching
author: matt
type: post
date: 2011-04-08T05:56:19+00:00
url: /blog/2011/04/08/how-to-stop-google-chrome-using-your-location-when-searching/
categories:
  - Uncategorized

---
When you use Chrome’s omnibar to search, Chrome will redirect you to search results based on when you are geographically. This is great when I’m at home because I see (more relevant) results from google.co.uk and not google.com.

However, I’m travelling at the moment and getting my results from google.co.th is painful since most of [the results][1] are not in english.

  1. Close Chrome.
  2. Open the file `Local State` in notepad. Mine was in: `C:\Users\matt\AppData\Local\Google\Chrome\User Data\Local State`. Linux users may find it in `~/.config/google-chrome/` or `~/.config/chromium/`, and OS X users can try `~/Library/Application Support/Google/Chrome.`
  3. Look for `last_known_google_url` and `last_prompted_google_url` and change their values to the local Google page of your choice.
  4. Save and close.
  5. Done.

You may find [other pages](http://www.google.com/support/forum/p/Chrome/thread?tid=45b1d65f4aeee39e&hl=en) telling you to hardcode the url in the Chrome options page when you “manage search engines”. This works to an extent but breaks other things like suggest.

Thanks to Siavash for [originally posting this][2].

 [1]: http://www.google.co.th/search?q=test
 [2]: http://code.google.com/p/chromium/issues/detail?id=1521