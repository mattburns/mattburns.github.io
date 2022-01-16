---
title: A build that’s green, should never be seen.
author: matt
type: post
date: 2010-01-14T23:00:53+00:00
url: /blog/2010/01/15/a-build-thats-green-should-never-be-seen/
categories:
  - Uncategorized

---
Your [continuous integration][1] server should stay green all the time. The odd broken test here and there means you get numb to the failed status on your build server, which in turn means it takes you longer to notice that the build has broken. When the build breaks, you should stop whatever you’re doing and make fixing it your top* priority. After you check in, the faster you fail the better because you haven’t had time to start thinking about your next task, and the thing you did to break the build is still fresh in your mind. That’s also why it’s so import to [keep the builds fast][2]**.

At work, we’ve just installed the [Radiator View Plugin][3]\*** for [Hudson][4] which allows you to see the status of all your builds at a glance. We have a spare monitor displaying this screen in the middle of the office so that you can see if the build has failed while you’re stood around the water cooler chatting about your [coffee cup metric][5].

There are two things that still bug me about this though:

  1. That monitor is burning up quite a bit of '[leccy][6].
  2. I don’t want to waste any thought power on a green build.

The first point is obvious but the second is a little more subtle. To me, [no news is good news][7]. A green screen in the middle of the office will still get my attention, when what I really want, is to pay it no attention whatsoever. That is, unless it’s red, which is when it gets all my attention. To achieve both of these requirements, I want the screen off when the build is fine, and on when it’s not.

Introducing… [screenwaker][8]!

[screenwaker][8] is a silly little java webstart app I knocked up that polls the build page and turns off the screen if everythings ok, but fires it back up again if anything fails. Perfect.

I’m not sure anyone else has ever faced this problem, or ever will, but there it is for you to use as you please none-the-less.

Matt

* Yes, _top_ priority. I don’t care if you were going to the loo.

** I searched for a good article on why it’s so important to keep the build fast but couldn’t find a good one. Suggestions welcome.

\*** I don’t really get the “Radiator” analogy. Surely “Dashboard” would be better?

\**** Well, in an ideal world, I’d like the monitor to disappear but that is beyond the scope of this post.

 [1]: http://dantwining.com/2009/03/19/the-12-steps-of-continuous-integration/
 [2]: http://en.wikipedia.org/wiki/Continuous_integration#Keep_the_build_fast
 [3]: http://wiki.hudson-ci.org/display/HUDSON/Radiator+View+Plugin
 [4]: http://hudson-ci.org/
 [5]: http://pauljulius.com/blog/2009/09/14/cup-of-coffee-metric-for-continuous-integration/
 [6]: http://www.urbandictionary.com/define.php?term=Leccy
 [7]: http://books.google.co.uk/books?id=PkZdv3UNTCgC&lpg=PA30&ots=b6QlomKGug&dq=unix%20%22no%20news%20is%20good%20news%22&pg=PA30#v=onepage&q=unix%20%22no%20news%20is%20good%20news%22&f=false
 [8]: http://www.mattburns.co.uk/screenwaker/