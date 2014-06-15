---
layout: post
title: "CoreData.SQLDebug for RubyMotion"
date: 2013-06-01 12:23
author: "Patrick Goddi"
comments: true
categories: [development, RubyMotion, iOS]
---
It is sometimes handy to turn on CoreData.SQLDebug in the simulator when debugging a Core Data issue. I have found the output to be very useful in finding the hard to find little bugs that pop-up between restkit and core data. It can also help find performance issues with the database.  Unfortunately there isn't any documentation for how to do this in RubyMotion. I found one solution that works to a degree. It requires installing the ios_sim app and forcing the simulator into CoreData.SQLDebug mode after the rubymotion build.

You will need to install ios_sim

    $ brew install ios-sim

Then add the following two line as the last lines in your RubyMotion rakefile

    # Be sure to substitute your app name and make sure you are using
    # the correct path to the app based on simulator version.
    ios_sim = `which ios-sim`.strip
    sh "#{ios_sim} launch build/iPhoneSimulator-6.1-Development/appname.app --args -com.apple.CoreData.SQLDebug 1"

This will open the simulator in CoreData.SQLDebug mode, and log debug information to the terminal.