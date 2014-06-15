---
layout: post
title: "RubyMotion iOS Apps"
date: 2013-01-17 11:28
comments: true
categories: [rubymotion]
---
I wanted to make a quick note that I have been using [RubyMotion](http://www.rubymotion.com/) the past few months. I don't mind building natively in Objective-C but since I have been coding both the app and the server side I found switching between Objective-C and Ruby a bit frustrating. I really find Objective-C to be too verbose a syntax for my taste. I also prefer to code in emacs vs. the Xcode UI. Call me old fashioned, but I find I can work much faster when I can operate on the code directly, versus through an intermediary UI.

The second reason for switching to RubyMotion is the libraries that are being created, they make iOS development feel so comfortable to a Ruby developer. Three key examples are [BubbleWrap](https://github.com/rubymotion/BubbleWrap), [SugarcCube](https://github.com/rubymotion/sugarcube) and [Teacup](https://github.com/rubymotion/teacup).

The third reason is testing and debugging, I like that RubyMotion comes with an RSpec clone, this means I have the same testing framework on both app and server. I also love the interactive console, there is nothing like tweaking your app live from a console (REPL). I find I can debug a lot of the code from the console, but RubyMotion also supports GDB for the more serious debugging needs. I hadn't used GDB in a few years but it came back to me pretty quickly once I started using it.

I also like the DSL approach of Teacup in styling RubyMotion iOS apps. I like that I can create style files much like I do with CSS and have my app UI built with the style information, makes changing style feel more natural to me as a web developer.

I have no doubt that there are many Objective-C developers who are extremely efficient in building apps, but it is always a challenge to become expert on multiple platforms. To become an expert iOS developer you need to become expert in the Cocoa libraries; the nice thing about RubyMotion is it allows you to learn the libraries within a familiar syntax if you are a ruby developer. It also allows you to create Ruby wrappers and generators that make developing for Cocoa feel more natural to a Ruby developer. Finally, since RubyMotion creates compiled native iOS apps, their is very little performance hit. 

I have a backlog of notes that I will post when I get a chance; including my experiences with development,  debugging, meta-programming, deploying via TestFlight, etc. I just wanted to give RubyMotion some praise from this Ruby developer, it has made developing iOS apps very similar to deploying ruby apps. 