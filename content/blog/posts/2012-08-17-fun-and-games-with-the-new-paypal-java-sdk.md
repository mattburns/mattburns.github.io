---
title: Fun and games with the new PayPal java SDK
author: matt
type: post
date: 2012-08-17T12:35:45+00:00
url: /blog/2012/08/17/fun-and-games-with-the-new-paypal-java-sdk/
categories:
  - Uncategorized

---
Up until now I’ve handled my payments for [stolencamerafinder][1] and [OddPrints][2] with [Google Wallet][3]. It’s not fantastic api ([I’ve even had to fix it][4]) but it’s pretty straight forward. There’s good documentation and the SDK saves you from writing all that boilerplate for talking to a web service.

I’ve had quite a few requests for allowing PayPal so I’ve spent the last couple of days flicking through their documentation and was quickly shown that:

> The X.Commerce Developer Tools team announces the stable release of [new SDKs][5] for PayPal APIs after several months in beta testing.

Great news. A stable release. It even includes [some work][6] that allows it to run on Google App Engine.

Time to crack on, right, where’s the documentation. Oh. There isn’t any because it has:

> Self-documented classes that describe the APIs

Ok, fine, I’m cool with that. I’ve downloaded the SDK, added it to my project. Now all I have to do is rummage through the packages to find the class that will serve as my entry point to the API. Tell you what, I’ll give you a head start, [here’s the package][7] it’s in.

Yep, there it is, buried amongst 172 generated classes, you want the PayPalAPIInterfaceServiceService. What a name. I’ve gone through the JAXB pain far too many times in my java career and although I don’t find it particularly difficult any more, it is still impossible not to vomit over my keyboard each time I’m forced to code against it.

This is (my first attempt at) a very basic call to the api:

```
PayPalAPIInterfaceServiceService paypal;
        try {
            InputStream is = req
                    .getSession()
                    .getServletContext()
                    .getResourceAsStream(
                            "/WEB-INF/paypal-sdk-config.properties");

            paypal = new PayPalAPIInterfaceServiceService(is);
        } catch (FileNotFoundException e) {
            // Urgh, I have to catch a checked exception that can only be thrown
            // by the other, overloaded, file-based constructor. Nice work
            // PayPal.
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        SetExpressCheckoutReq setExpressCheckoutReq = new SetExpressCheckoutReq();
        SetExpressCheckoutRequestType setExpressCheckoutRequestType = new SetExpressCheckoutRequestType();
        SetExpressCheckoutRequestDetailsType setExpressCheckoutRequestDetails = new SetExpressCheckoutRequestDetailsType();

        List paypalItems = Lists.newArrayList();

        PaymentDetailsItemType paypalItem1 = new PaymentDetailsItemType();
        BasicAmountType amount1 = new BasicAmountType();
        amount1.setValue("0.50");
        paypalItem1.setAmount(amount1);
        paypalItem1.setQuantity(1);
        paypalItems.add(paypalItem1);

        PaymentDetailsItemType paypalItem2 = new PaymentDetailsItemType();
        BasicAmountType amount2 = new BasicAmountType();
        amount2.setValue("0.25");
        paypalItem2.setAmount(amount2);
        paypalItem2.setQuantity(1);
        paypalItems.add(paypalItem2);

        PaymentDetailsType paymentDetails = new PaymentDetailsType();
        paymentDetails.setPaymentDetailsItem(paypalItems);

        setExpressCheckoutRequestDetails.setPaymentDetails(Lists
                .newArrayList(paymentDetails));
        setExpressCheckoutRequestDetails
                .setCancelURL("http://oddprints/cancel");
        setExpressCheckoutRequestDetails
                .setReturnURL("http://oddprints/checkout");

        BasicAmountType totalAmount = new BasicAmountType();
        totalAmount.setValue("0.75");
        totalAmount.setCurrencyID(CurrencyCodeType.USD);
        
        // not this, this is deprecated (but not deprecated in the code)
        // setExpressCheckoutRequestDetails.setOrderTotal(totalAmount);

        // set both of these instead
        paymentDetails.setItemTotal(totalAmount);
        paymentDetails.setOrderTotal(totalAmount);

        setExpressCheckoutRequestType
                .setSetExpressCheckoutRequestDetails(setExpressCheckoutRequestDetails);
        setExpressCheckoutReq
                .setSetExpressCheckoutRequest(setExpressCheckoutRequestType);
        SetExpressCheckoutResponseType response = null;

        try {
            response = paypal.setExpressCheckout(setExpressCheckoutReq);
        } catch (SSLConfigurationException e) {
            // TODO
        } catch (InvalidCredentialException e) {
            // TODO
        } catch (HttpErrorException e) {
            // TODO
        } catch (InvalidResponseDataException e) {
            // TODO
        } catch (ClientActionRequiredException e) {
            // TODO
        } catch (MissingCredentialException e) {
            // TODO
        } catch (OAuthException e) {
            // TODO
        } catch (IOException e) {
            // TODO
        } catch (InterruptedException e) {
            // TODO
        } catch (ParserConfigurationException e) {
            // TODO
        } catch (SAXException e) {
            // TODO
        }
```

Bleurgh. Having to write this kind of shit gives java a really bad name. Is there really any improvement over just calling the API without any SDK? There are so many things wrong with this that I’m surely going to miss stuff:

  * Declaring you throw a checked expection that you don’t throw.
  * Inconsistent naming.
  * The insane object nesting generated by JAXB .(SetExpressCheckoutReq>SetExpressCheckoutRequestType>SetExpressCheckoutRequestDetailsType etc.).
  * Who cares we’re using a strongly typed language, let’s pass doubles in strings and just document what’s valid – “Must not exceed $10,000 USD in any currency. No currency symbol. Decimal separator must be a period (.), and the thousands separator must be a comma (,).”
  * Redundantly having to pass the total for the whole basket.

Matt, keep calm, breath deeply. It’s ok. You can wrap this cruft up behind a nice clean bit of code and you never have to look at it again…

Phew, let’s run it.

Bang. That threw a ClientActionRequiredException. Looking at the response I can see “XML syntax error”. No more help than that. Time to take a look at the xml that was generated and I quickly spot that it’s not legal:

<ebl:Amount0.5</ebl:Amount>

What? I’m using an SDK and it still generates duff xml. I was pretty pissed off at this point and lost my cool. I glanced at the source code and thought I’d found a bug so fired off a [bug report][8].

It turned out it wasn’t so much a bug, just an example of why munging xml by hand is a bad idea. It was my fault for not sending the currency code for each and every item in the basket.

Now we can add one more thing to our list or gripes:

  * Having to pass the currency code for each item in basket.

I didn’t want this post to be a rant. No-one wants to read that, I’m just frustrated that it’s taken me two days to get to the simplest end-to-end test. If anyone at PayPal reads this, please hide away the JAXB objects and expose a cleaner set of interfaces for the java SDK. It’s the sort of thing I would normally write myself and open-source, but I feel in this case, it’s not something that would benefit the people so much as it would benefit PayPal.

 [1]: http://www.stolencamerafinder.com "stolen camera finder"
 [2]: http://www.oddprints.com "OddPrints"
 [3]: http://www.google.com/wallet/ "Google Wallet"
 [4]: http://productforums.google.com/d/msg/checkout-merchant/7ICny4H_Nj4/YXWg_OZVmJcJ
 [5]: https://www.x.com/developers/paypal/documentation-tools/paypal-sdk-index
 [6]: http://bpossolo.blogspot.co.uk/2012/06/new-paypal-sdks-on-google-app-engine.html
 [7]: https://github.com/paypalx/SDKs/tree/master/Merchant/merchant-java-sdk/src/urn/ebay/api/PayPalAPI
 [8]: https://github.com/paypalx/SDKs/issues/14