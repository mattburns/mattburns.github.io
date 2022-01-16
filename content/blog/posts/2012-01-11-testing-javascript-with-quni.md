---
title: Testing JavaScript with QUnit for for Dummies, sorry, Java developers
author: matt
type: post
date: 2012-01-11T13:03:50+00:00
url: /blog/2012/01/11/testing-javascript-with-quni/
categories:
  - Uncategorized

---
Disclaimer: I’m no javascript expert so I ~~may be~~ am almost certainly talking a load of rubbish here.

I was just looking for a unit testing framework for some javascript I’m writing (rather the the home-rolled framework I’ve out-grown) and came across [QUnit][1]. I’ve not tried any others so feel free to suggest alternatives. So far, it’s great and does everything I want and took me almost no time to learn. Easy.

The one thing that bugs me though is that they’ve swapped “expected” and “actual” parameter arguments around for the equality test. Technically it’s not that important since it won’t affect the result of the test, but in practice I think it’s very important. Your tests form part of your documentation of how the code should behave. If you get them the wrong way around and a test fails with “expected 10 but got 20” the developer may well go off and try to make the code return 10. \*shudder\*.

Java method signature in JUnit:

```
public static void assertEquals(Object expected, Object actual)
```

The [class][2] offers overloaded implementations with primitives or with message etc. There are also ways of writing your tests in a type-safe fashion to prevent this whole problem in Java, but in my experience, this is more common. Another post maybe…

Javascript function signature in QUnit:

```
equal( actual, expected, [message] )
```

I can only assume they reversed the order of the arguments because of the way that javascript allows optional arguments.

I flip between writing Java and JavaScript quite a lot which would be a disaster waiting to happen so I’ve just wrapped it in my own function:

```
function assertEquals(expected, actual, message) {
    equal(actual, expected, message);
}
```

This all feels wrong and stupid. What do you think?

 [1]: http://docs.jquery.com/QUnit
 [2]: http://kentbeck.github.com/junit/javadoc/latest/org/junit/Assert.html