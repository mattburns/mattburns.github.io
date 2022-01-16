---
title: Convention ÷ Configuration
author: matt
type: post
date: 2009-05-18T22:25:24+00:00
url: /blog/2009/05/18/convention-÷-configuration/
categories:
  - software
tags:
  - eclipse
  - java
  - maven

---
I’ve long been sold on the concept of [Convention Over Configuration][1]. For me it’s a no-brainer, not only am I lazy, but when I am forced to make a decision about something technical, well, let’s just say the number of times I get it wrong is > 0.

Recently I’ve been playing around with [Maven][2], something I should have done years ago. Maven seems pretty sold on the convention idea too and so I just expected a simple project to work “out of the box”.

[![](/wp-content/uploads/2009/05/maven1-300x157.png)][3]Unfortunately, when I tried, I hit a problem with my first simple project. As you can see from the “reconstruction” screenshot, I had problem with recognising simple java 5 features.

I was using the latest copy of eclipse, on a fresh install of Ubuntu using OpenJDK. I’ve not developed with OpenJDK and so blamed that at first, it couldn’t possibly be Maven… So, I downloaded the Sun JDK, and as you can guess, I realised it was a Maven thing.

When you create a simple Maven project using the [m2eclipse][4] eclipse plugin it defaults to a Java 1.4 compliance level. What kind of sensible convention is that? I like to think there is a good reason for that because I imagine it has cost the community quite a few potential Mavenees.

Once you realise this is the problem, just change the project specific Java compiler settings to whatever makes sense for you.

I’ve not got any research or references to hand, but my gut tells me that the convention should be to use whatever the majority of the programming community agrees is the best version of the best tool for the job. If someone wants to use Maven for a project that needs to support backwards compatibility, then let them do the configuring, not me.

It also defaults to JUnit 3.8.1, another warning sign in my head. Everything else in Maven I have done so far has been a pleasure and m2eclipse looks like a great plugin, I just wish the defaults were not so 2004.

To fix this within the POM you need to add the following:

> <plugins>  
> <plugin>  
> <groupId>org.apache.maven.plugins</groupId>  
> <artifactId>maven-compiler-plugin</artifactId>  
> <configuration>  
> <source>1.6</source>  
> <target>1.6</target>  
> </configuration>  
> </plugin>  
> …  
> </plugins>

 [1]: http://en.wikipedia.org/wiki/Convention_over_Configuration
 [2]: http://maven.apache.org/
 [3]: http://www.mattburns.co.uk/blog/wp-content/uploads/2009/05/maven1.png
 [4]: http://m2eclipse.codehaus.org/