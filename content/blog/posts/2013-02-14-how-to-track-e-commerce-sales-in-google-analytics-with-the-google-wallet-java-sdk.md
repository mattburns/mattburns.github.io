---
title: How to track e-commerce sales in Google Analytics with the Google Wallet Java SDK
author: matt
type: post
date: 2013-02-14T14:54:17+00:00
url: /blog/2013/02/14/how-to-track-e-commerce-sales-in-google-analytics-with-the-google-wallet-java-sdk/
categories:
  - Uncategorized

---
If you have your cart built up in javascript then just follow [Google’s documentation][1]. If you submit your Google Wallet cart server-side using the java SDK and want to track the sale using Google Analytics’ [ecommerce feature][2], then this blog is for you…

Before you start, make sure you have [enabled the ecommerce feature][3] in Google Analytics.

In your Java code, you need to set the analyticsData (String) in the cart:

```
merchantflowSupport.setAnalyticsData(analyticsData);
```

To get that analyticsData string, I pass it to my server with a query param using a bit of javascript:

```
$("#google-purchase-link").click(function(e){
    _gaq.push(function() {
        var pageTracker = _gaq._getAsyncTracker();
        setUrchinInputCode(pageTracker);
        console.log(getUrchinFieldValue());
        window.location = "/purchase/google?analyticsData=" + getUrchinFieldValue();
    });
    e.preventDefault();
});
```

I use the async version of Google Analytics, jQuery, and Jersey so I’ve skipped that stuff because that’s not important and you probably do it differently. If you use the old ga.js and GWT, then [this blog post][4] may help you better.

If you get stuck, I use this solution for [OddPrints.com][5] which is open-source so that should fill any gaps.

 [1]: https://developers.google.com/checkout/developer/checkout_analytics_integration
 [2]: https://developers.google.com/analytics/devguides/collection/gajs/gaTrackingEcommerce
 [3]: http://support.google.com/analytics/bin/answer.py?hl=en&answer=1009612
 [4]: http://blog.broc.seib.net/2010/10/integrating-google-checkout-with.html
 [5]: http://www.oddprints.com/