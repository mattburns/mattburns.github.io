---
title: Pick the Right Scope Automatically
author: matt
type: post
date: 2010-04-06T17:13:51+00:00
url: /blog/2010/04/06/pick-the-right-scope-automatically/
categories:
  - SCWCD tips
tags:
  - scwcd
  - SCWCD tips

---
As [I previously metioned][1], I’m taking the [SCWCD][2] exam tomorrow. When trying to cram for any exam I like to make up short poems, acronyms or just random chains of though. For example, I know the difference between Mitosis and Meiosis because Meiosis begins with “Meow” which is what cats do and they have four legs… anyway…

My first thing to remember is that a JspContext has a findAttribute method that I can use to **Pick the Right Scope Automatically**.

The acroynym, PRSA, is the order scopes are searched for attributes: Page, Request, Session, Application. You know that the S stands for Session because you can’t put attributes in a servlet. This also allows you to remember which objects can have attributes.

 [1]: http://www.mattburns.co.uk/blog/2010/04/06/head-first-servlets-and-jsp-errata/
 [2]: http://in.sun.com/training/certification/java/scwcd.xml