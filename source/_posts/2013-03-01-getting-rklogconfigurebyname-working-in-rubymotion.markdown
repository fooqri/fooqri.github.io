---
layout: post
title: "Getting RKLogConfigureByName working in RubyMotion"
date: 2013-03-07 15:21
comments: true
categories: [RubyMotion]
author: "Patrick Goddi"
publish: true
---
Just a quick note, I was getting an undefined constant error for
RKLogConfigureByName, the standard way of setting up logging in
RestKit. It seems that the #define statements in the
_/vendor/Pods/RestKit/Code/Support/RKLog.h_ file are not getting
picked up. I am using the pod and loading with RubyMotion pod support,
so Iåm not sure what the issue is. I will need to investigate further
but this quick workaround works, just call the lower-level method
mapped via the #define. For example instead of RKLogConfigureByName
use RKlcl_configure_by_name.  I also list all the RKlcl_v constants to
use instead of the RKLogLevel constants. I also included an example of
how they are used, in this case I have put the setup in a method, and
it gets called from the the standard didFinishLaunchingWithOption
application block.

{% gist 4733618 %}

