---
title: How to grant access to AWS billing to an IAM user
author: matt
type: post
date: 2015-06-17T11:59:33+00:00
url: /blog/2015/06/17/how-to-grant-access-to-aws-billing-to-an-iam-user/
categories:
  - AWS

---
First you must go to your account settings and grant access to IAM users: <https://console.aws.amazon.com/billing/home#/account>

Click “edit”

![](/wp-content/uploads/2015/06/Screen-Shot-2015-06-17-at-12.54.45.png) 

And “activate”

![](/wp-content/uploads/2015/06/Screen-Shot-2015-06-17-at-12.55.00.png) 

&nbsp;

Then you can go do all the policy group nonsense that every other google result will give you. Basically, just create a user and add them to a group with these policies:

![](/wp-content/uploads/2015/06/Screen-Shot-2015-06-17-at-12.57.08.png) 

&nbsp;

Bosh.