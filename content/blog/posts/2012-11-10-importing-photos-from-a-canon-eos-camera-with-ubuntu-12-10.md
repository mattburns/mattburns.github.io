---
title: Importing photos from a Canon EOS camera with Ubuntu 12.10
author: matt
type: post
date: 2012-11-10T12:13:41+00:00
url: /blog/2012/11/10/importing-photos-from-a-canon-eos-camera-with-ubuntu-12-10/
categories:
  - Uncategorized

---
For some reason, when I try to connect my [Canon EOS 7D][1] in Linux I get this error:<figure style="width: 300px" class="wp-caption alignnone">

![](/wp-content/uploads/2012/11/Screenshot-from-2012-11-10-120547.png)

    Unable to mount Canon Digital Camera  
    Error initialising camera: -1: Unspecified error

I get no love from lsusb:

```
matt@beast:~$ lsusb
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 003: ID 045e:0745 Microsoft Corp. Nano Transceiver v1.0 for Bluetooth
```

Thanks to a comment in [this thread][2] I tried a different usb port and now it works. Huzzah. It seems to be a problem with the usb 3 ports, no idea why.

I hope this post helps someone out 🙂

 [1]: http://www.amazon.co.uk/gp/product/B002LSI1LO/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B002LSI1LO&linkCode=as2&tag=mattburnscouk-21
 [2]: http://ubuntuforums.org/showthread.php?t=2045211