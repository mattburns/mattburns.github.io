---
title: 11 EL Implicit Variables
author: matt
type: post
date: 2010-04-07T09:30:08+00:00
url: /blog/2010/04/07/11-el-implicit-variables/
categories:
  - SCWCD tips

---
All the EL implicit variables are Maps except for pageContext.

To remember the attribute-holding scope objects, just remember to [Pick the Right Scope Automatically][1] and stick the word “Scope” on the end:

  * pageScope
  * requestScope
  * sessionScope
  * applicationScope

Then you have 4 param and header objects of the form : **(param|header)[Values]**

  * param
  * paramValues
  * header
  * headerValues

Then I just remember the last 3:

  * cookie
  * initParam
  * pageContext (not a Map, it’s the JavaBean)

 [1]: http://www.mattburns.co.uk/blog/2010/04/06/pick-the-right-scope-automatically/