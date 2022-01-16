---
title: Listeners and Events
author: matt
type: post
date: 2010-04-07T09:51:30+00:00
url: /blog/2010/04/07/listeners-and-events/
categories:
  - SCWCD tips

---
There are 8 Listeners to remember. We know there are attributes in 4 scopes because we know how to [Pick the Right Scope Automatically][1], but you can’t listen to Page attributes, it doesn’t make sense, so that leaves us with RSA; **Request**, **Session** and **Application**. These tally with the objects:

  * ServletRequest
  * HttpSession
  * ServletContext

There is a Listener for each of these objects for lifecycle events, and for attribute events, so that gives us 6 of the Listener Interfaces:


*   ServletRequest[Attribute]Listener
*   HttpSession[Attribute]Listener
*   ServletContext[Attribute]Listener

HttpSession gets the 2 extra interfaces:


*   HttpSessionBindingListener – Attribute objects implement this if they themselves want to know whenthey are [un]bound
*   HttpSessionActivationListener – Listen here to have a nose when the session is gallivanting around

## Events

There are just 6 events, one for each lifecycle event:


*   ServletRequestEvent
*   HttpSessionEvent
*   ServletContextEvent

and one for each attribute-related event:

*   ServletRequestAttributeEvent
*   HttpSessionBindingEvent – (It’s easy to remember this black sheep because its initials rhyme with the worlds local bank HSBE)
*   ServletContextAttributeEvent


 [1]: http://www.mattburns.co.uk/blog/2010/04/06/pick-the-right-scope-automatically/