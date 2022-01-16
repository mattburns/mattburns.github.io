---
title: How to access your app engine dev server from another machine
author: matt
type: post
date: 2014-10-10T16:03:14+00:00
url: /blog/2014/10/10/how-to-access-your-app-engine-dev-server-from-another-machine/
categories:
  - app engine
  - software

---
I keep forgetting how to do this so I’m writing it down in the vain hope I may commit it to memory.

## The problem

You want to access your locally running dev server on another machine on your local network or maybe even from a virtual machine. whatevs.

## The solution

Start your dev server with this extra program argument (you can find this under “debug configurations” in eclipse):

`--address=0.0.0.0`

_Now remember it you stupid brain._

## Gradle users

If you’re using [Gradle][1] then you need to set it in httpAddress like this:

```
appengine {
    httpAddress = "0.0.0.0"
    httpPort = 8888
    downloadSdk = true
```

 [1]: https://gradle.org/