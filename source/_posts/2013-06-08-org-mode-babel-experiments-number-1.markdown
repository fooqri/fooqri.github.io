---
layout: post
title: "org-mode babel experiments #1"
date: 2013-06-08 06:54
comments: true
categories: emacs, orb-mode, babel
---
As I mentioned in my post on [nvALT and Emacs](http://godd.io/blog/2013/03/04/nvalt-and-emacs/) I have been using Deft for notes. One change I have made is to switch from using markdown to org-mode. Org-mode is a very powerful tool for not only note taking but hen combined with [org-babel](http://orgmode.org/worg/org-contrib/babel/index.html) is a powerful tool for [Literate Programming](http://en.wikipedia.org/wiki/Literate_programming).

With the startup I am coding both server and client, but also managing the server and db enviornmnts. I try to be as efficient as possible by writig scripts to do common tasks. One issue is that amount of time that passes between some tasks, and how easy it is to lose the location of scripts, or the order they should be performed.

Checklists can be very handy for remembering, but not always for executing code. So I decided to experiment with literate programming in org-mode to combine checklists with code execution.

TODO:
- Show DB client lib
- Show static items like drop and load DB 
- Show dynamic items like running queries.
- Show an example of creating a report section of the file