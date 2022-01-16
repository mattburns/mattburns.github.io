---
title: Tapiriik not syncing to Dropbox?
author: matt
type: post
date: 2015-03-31T13:24:50+00:00
url: /blog/2015/03/31/how-to-fix-problem-when-tapiriik-not-syncing-dropbox-files/
cover:
    image: /wp-content/uploads/2015/03/bg-sunset.4f0ac5f2dce2.png
categories:
  - Uncategorized

---
My activities hadn’t been syncing to Dropbox for a while (since mid-November 2014).

> This activity was not synchronized to the following services:
>
> Dropbox: There was a problem indexing your activities on Dropbox, so no activities will be uploaded to Dropbox.


Everything else was syncing fine (Strava, Endomondo, Garmin).

A quick email to the author and everything is solved:

> If you look in your Dropbox folder there should be a number of files with .tcx.summary-data extensions. Move those out of the folder and it should start working again – this is a rather ancient artefact of a mistake I made in Dropbox sync back in 2013, surprised it kept working as long as it did. 

Sorted.

## TL;DR*

Delete any files with `.tcx.summary-data` extensions from your Dropbox folder.

*I only recently found out what that was short for. I’ve been ignoring it for years assuming it was invalid html markup.