---
title: Connecting to EC2 from Chrome’s Secure Shell using only a PEM file
author: matt
type: post
date: 2012-11-15T10:35:37+00:00
url: /blog/2012/11/15/connecting-to-ec2-from-chromes-secure-shell-using-only-a-pem-file/
categories:
  - Uncategorized

---
Gee, what a title. I know this post is going to be popular.

First, you need to generate your public key from your private key like this:

```
ssh-keygen -y -f yourkey.pem > yourkey.pub
```

Then, in [Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo), select the “Import…” link to bring up a file picker. You must import two files for each identity.  A private key and a public key.  For example, you would select both “yourkey.pem” and “yourkey.pub”.



It should look something like this:

[![](/wp-content/uploads/2012/11/secureshell.png)](http://www.mattburns.co.uk/blog/wp-content/uploads/2012/11/secureshell.png)





Then just connect! Once connected, you can bookmark the page for instant access.













