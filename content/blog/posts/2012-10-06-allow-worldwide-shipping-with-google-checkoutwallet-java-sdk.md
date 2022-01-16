---
title: Allow worldwide shipping with Google Checkout/Wallet java SDK
author: matt
type: post
date: 2012-10-06T14:47:19+00:00
url: /blog/2012/10/06/allow-worldwide-shipping-with-google-checkoutwallet-java-sdk/
categories:
  - Uncategorized

---
[Google’s java SDK][1] for interacting with the checkout API is [not a fun experience][2]. It’s generated from the WSDL using JAXB which has a unique ability to generate client interfaces that no human could ever “design”.

It’s not actually that hard to write code with, you just have to think like a [deranged machine][3].

By default, the only [allowed shipping destination][4] will be your country. If you wish to allow worldwide shipping, you have to do something like this:

```
ApiContext apiContext = new ApiContext(environment, "yourMerchantId", "yourMerchantKey", "GBP");
CheckoutShoppingCartBuilder cartBuilder = apiContext.cartPoster().makeCart();
CheckoutShoppingCart cart = cartBuilder.build();
FlatRateShipping frs = new FlatRateShipping();
frs.setName("flat rate");

ShippingRestrictions shippingRestrictions = new ShippingRestrictions();
AllowedAreas allowedAreas = new AllowedAreas();
allowedAreas.getUsStateAreaOrUsZipAreaOrUsCountryArea().add(new WorldArea());
shippingRestrictions.setAllowedAreas(allowedAreas);
frs.setShippingRestrictions(shippingRestrictions);
```

I just posted this because I could not find one example on the internet. Crazy I know, but now there is one.

 [1]: http://code.google.com/p/google-checkout-java-sdk/
 [2]: http://productforums.google.com/forum/#!msg/checkout-merchant/7ICny4H_Nj4/YXWg_OZVmJcJ
 [3]: http://en.wikipedia.org/wiki/Holly_(Red_Dwarf)
 [4]: http://support.google.com/checkout/sell/bin/answer.py?hl=en&answer=71391