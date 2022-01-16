---
title: Using an SSL certificate on a custom domain with Google App Engine
author: matt
type: post
date: 2015-03-04T10:23:03+00:00
url: /blog/2015/03/04/using-ssl-certificate-on-a-custom-domain-with-google-app-engine/
categories:
  - Uncategorized

---
This post is more a reminder for me. Sorry.

Get an SNI certificate from Gandi. And download the certificate

![](/wp-content/uploads/2015/03/Screen-Shot-2015-03-04-at-10.09.09.png) 

It will have a name like:

```
certificate-123456.crt
```

You need to create public and private pem files for google like this:

```
openssl rsa -in cameraforensics.key -text > private.pem
openssl x509 -inform PEM -in certificate-123456.crt > public.pem
```

(cameraforensics.key is my private key from when I created the SSL certificate from Gandi)

In Google Apps domain manager, upload those files under “Security > show more > [SSL for custom domains][1]“: ![](/wp-content/uploads/2015/03/Screen-Shot-2015-03-04-at-09.26.24.png)

I was upgrading my certificate so I see both the current and the new certificate:

![](/wp-content/uploads/2015/03/Screen-Shot-2015-03-04-at-09.28.06.png) 

I had to delete the assigned url from the old certificate, then assign it to the new certificate and then save changes:

![](/wp-content/uploads/2015/03/Screen-Shot-2015-03-04-at-09.29.09.png) 

Ahh, green padlock goodness:

![](/wp-content/uploads/2015/03/Screen-Shot-2015-03-04-at-10.21.17.png) 

UPDATE:

But wait, you’re not finished… It turns out that while Chrome on desktop give a nice green padlock, Chrome on Android still doesn’t trust it. You need to go back to Gandi, “Download the intermediate certificate” then append it to your public certificate. You’ll then need to upload that to Google instead. Eg:

```
cat public.pem intermediate.pem > publicAndChain.pem
```

You can check the certificate here: <https://www.sslshopper.com/ssl-checker.html>

Footnote:  
If you’re seeing this problem: “The identity of this website has been verified by Gandi Standard SSL CA but does not have public audit records. The site is using outdated security settings that may prevent future versions of Chrome from being able to safely access it.” Then follow this advice from Gandi

> You currently have a SHA1 certificate which is no longer the preferred standard for Chrome but is still a very valid form of encryption with which other browsers have no issue.
> 
> If you wish, you can generate a SHA2 certificate for free.
> 
> To do this, please first generate a SHA2 CSR :  
> http://wiki.gandi.net/en/ssl/csr#sha-2\_certificate\_request
> 
> Then, please follow the regeneration procedure (you will have to go through the validation process onceagain):  
> http://wiki.gandi.net/en/ssl/regenerate
> 
> For information, you will receive an email once the certificate is regenerated, you can then install it on your server. However the order will still show as pending because of the revoking of your previous certificate : the operation stays in this state for about 48 hours after the certificate issuance before showing as completed.
> 
> For more information on SHA1 and SHA2  
> https://www.gandi.net/news/en/2014-10-21/2460-sha-2\_certificates\_are\_now\_available

 [1]: https://admin.google.com/AdminHome#SecuritySettings:flyout=ssl