---
title: Simplify your API – Can Singletons be used for Good, not Evil?
author: matt
type: post
date: 2011-11-14T15:55:53+00:00
url: /blog/2011/11/14/simplify-your-api/
categories:
  - Uncategorized

---
I recently wrote [an article about singletons][1] in java. The only thing I wanted to cover was that if you really want a singleton, I recommend you use the enum pattern. This post was motivated after more interesting comments were raised about testability when you see the “static” keyword.

When you type “static” a little alarm bell should ring in your head to warn you that there could be trouble ahead. As [Dan][2] correctly pointed out, a reference to the static member INSTANCE will tightly couple the caller to Elvis. This is not good if testing with Elvis will cause you problems. For example, if Elvis is slow, or accesses a database or something like that which would be better tested with a mock implementation.

However, sometimes the static keyword makes sense because it is an implementation detail that you are not concerned with. By you I mean a client of the code. Why muddy an API so that you can pass around objects that will never change. To illustrate my point, I wrote a very simple bit of code that hopefully isn’t too contrived. 

Imagine you have to write a computer system for a Blackpool nightclub called “Elvis Live!”. This club has a different Elvis impersonator on every night. The system has to manage the bookings of the different Elvis impersonators and print the posters which list which impersonators are performing each night.

In my very simple implementation I wrote a class to represent the club:  `ElvisClub.java`

```
package uk.co.mattburns.elvis;
import java.util.Map;
import org.joda.time.LocalDate;
import com.google.common.collect.Maps;

public class ElvisClub {

    private final Map&lt;LocalDate, ElvisImpersonator> bookings = Maps
            .newTreeMap();

    public boolean bookImpersonator(LocalDate date,
            ElvisImpersonator impersonator) {
        if (bookings.containsKey(date)) {
            return false;
        } else {
            bookings.put(date, impersonator);
            return true;
        }
    }

    public ElvisImpersonator getImpersonatorOnDate(LocalDate date) {
        return bookings.get(date);
    }

    public String getPosterTitle() {
        return "Keeping The King Alive since " + Elvis.INSTANCE.died();
    }

    public String getPosterBody() {
        StringBuilder stringBuilder = new StringBuilder();
        for (LocalDate date : bookings.keySet()) {
            ElvisImpersonator act = bookings.get(date);
            stringBuilder.append(date.toString() + " : See " + act.name());
            stringBuilder.append(" who was born " + act.yearsBornAfterElvis()
                    + " years after Elvis");
        }
        return stringBuilder.toString();
    }
}
```

A simple pojo to represent a performer at the club: `ElvisImpersonator.java`

```
package uk.co.mattburns.elvis;
import org.joda.time.LocalDate;

public class ElvisImpersonator {

    private final String name;
    private final LocalDate birthdate;

    public ElvisImpersonator(String name, LocalDate birthdate) {
        this.name = name;
        this.birthdate = birthdate;
    }

    public String name() {
        return name;
    }

    public LocalDate birthdate() {
        return birthdate;
    }

    public int yearsBornAfterElvis() {
        return birthdate().getYear() - Elvis.INSTANCE.born().getYear();
    }
}
```

Crucially, both of these classes have a dependency on Elvis. I decided to make Elvis a singleton: `Elvis.java`

```
package uk.co.mattburns.elvis;
import org.joda.time.LocalDate;

public enum Elvis {
    INSTANCE;
    private final LocalDate born = new LocalDate(1935, 1, 8);
    private final LocalDate died = new LocalDate(1977, 8, 16);

    public LocalDate born() {
        return born;
    }

    public LocalDate died() {
        return died;
    }
}
```

You can browse all the source code [here][3]. Or better still, checkout the code and simply import the project into eclipse:

```
svn checkout http://elvis-club.googlecode.com/svn/trunk/ elvis-club-read-only
```

&nbsp;

I already know what you’re thinking:

> Elvis.java should be an interface: Celebrity.java. Then I could have a concrete Elvis to pass around which implements Celebrity.

> ElvisImpersonator.java should be an interface: Impersonator.java. Then I could write a CelebrityImpersonator.java which would take a Celebrity on construction.

That is one way of solving it, and it’s not a bad way. I agree that you should expect change, embrace it, marry it, have its babies, but don’t start writing code for it before it’s happened. One day the club may have a Marilyn Monroe night and in that case you anticipated change ~~beautifully~~ luckily. What if it changes into a comedy club? How about a restaurant?

What’s really important is writing code that’s easy for programmers to read, and therefore, easy for programmers to change.

Here is a snippet from some of my test code which gives you an idea of what I mean:

```
ElvisClub theClub = new ElvisClub();
LocalDate today = new LocalDate();
LocalDate brianBorn = new LocalDate(1970, 1, 1);
ElvisImpersonator brian = new ElvisImpersonator("Brian", brianBorn);
theClub.bookImpersonator(today, brian);
```

A similar snippet, without using the Elvis singleton would look something like this:

```
LocalDate brianBorn = new LocalDate(1970, 1, 1);
LocalDate elvisBorn = new LocalDate(1935, 1, 8);
LocalDate elvisDied = new LocalDate(1977, 8, 16);

Celebrity realElvis = new CelebrityImpl("Elvis", elvisBorn, elvisDied);
Impersonator brian = new CelebrityImpersonator("Brian", realElvis, brianBorn);
Club theClub = new Club(realElvis);
theClub.bookImpersonator(today, brian);
```

There’s not a massive difference but I still think the constructors are a bit “noisy”. In a real-world application, you would probably expect references to a more complex set of collaborating objects.

I haven’t sacrificed any testibility of my code. If anything, I’ve reduced the amount of code I _need_ to test. My way, there can only be Elvis and so I only need to test that the club handles things to do with Elvis. If I wrote a more generic version I would have to test that it handles Celebrities that are still alive, that they were born before they died, and so on.

I think I’m right but I’ve changed software design views pretty frequently over the last 10 years. If you think I’m wrong, I challenge you to convince me why…

 [1]: http://www.mattburns.co.uk/blog/2011/10/26/how-to-write-singletons-in-java/
 [2]: http://dantwining.co.uk
 [3]: http://code.google.com/p/elvis-club/source/browse/trunk/