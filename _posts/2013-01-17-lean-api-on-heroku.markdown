---
layout: post
title: "Lean API on Heroku"
date: 2013-01-17 08:46
comments: true
categories: [ruby, servers, development]
redirect_from: /blog/ruby/servers/development/2013/01/17/lean-api-on-heroku
---
We have recently been working on an iOS app that requires a backend service. In this case I was looking for something leaner, simpler, and faster than Rails since it was only an API for a mobile app, no web front-end. I wanted it to be very lean and scalable so we could make it through early user testing without spending a lot on servers. Ok, ideally without spending anything on servers; basically how much could I squeeze out of one Heroku worker.

After some investigation of the typical light weight ruby frameworks (Sinatra, Merb, etc) I stumbled upon [Grape](https://github.com/intridea/grape), a ruby API micro-framework. Grape uses a very simple DSL for defining APIs for your Ruby objects. Grape runs on [Goliath](https://github.com/postrank-labs/goliath), which is a non-blocking Ruby web server framework that uses Ruby fibers to simplify the handling of asynchronous requests. Goliath runs on the popular [EventMachine](https://github.com/eventmachine/eventmachine) reactor. EventMachine is an event-driven Ruby library that works much like Node.js.

The [Grape](https://github.com/intridea/grape) github page provides a great deal of information on getting started, and David Jones has a great [example](https://github.com/djones/grape-goliath-example) project on GitHub demonstrating how to deploy a grape API on Heroku.

The DSL is really simple and I was able to wrap some ruby objects in a day and deploy it on Heroku. Here is an snippet of what the DSL looks like.

{% gist 4555788 %}

As you can see the Grape framework supports API versioning, and the DSL provides a simple way to define API endpoints by defining resources and then specifying the HTTP requests (get, post, put, delete) for that resource. Any Rails developer should feel comfortable with the paths, params, and routes syntax in Grape.

In this code snippet I show part of the API definition for two resources (missions &amp; players). This will mean the path for accessing these are _/missions_ and _/players_. Because I specified _prefix 'api'_ at the top of the file, the actual path becomes _/api/missions_ and _/api/players_. So for example the _get "/:id"_ would correspond to a get request of /api/players/7E781305-777F-4044-9770-C7995585F540 where the UUID is a player id and would be available in the params[:id] variable. 

I should also note that even though these are simple _get_ requests Grape will expect a header to be set for the secret key(secretk), and also require an Accept header with the version, vendor info, and content type (json). The easiest way to test your API will be to use an app like [Postman](http://goo.gl/daZ5Q) that makes it easy to formulating requests, setting headers, from your Chrome browser. Postman also allows you to save requests, and re-run them. 

I happen to be using Mongo for this, but Grape supports most major DBs. I am only showing two get methods, my full definition supports CRUD for these objects, as well as a few common queries of the db. The error checking of the request is fairly straightforward. I am checking for an API key, but this would be replaced with an API key lookup function to validate the requestor. It is easy to respond with specific errors as you can see. 


The terse _error!, unless_ syntax makes the error handling code very readable. The request handling for these two examples are simple: I query a mongo collection for an id, then map that response onto objects, and then convert the objects to json. This looks funny since it is basically json-&gt;object-&gt;json since mongo returns json, but there is more that happens in the object mapping; the json from the db and the json from the object are not the same. 

By requiring _mission.rb_ and _player.rb_ at the top of the file, I pull in my Mission and Player classes so they can be used in the map operation.   Try to ignore the lame _.first_ operation, this was a bit of laziness in dealing with what is an array of one item resulting from the map operation. As with all Ruby, the output of the last operation is what is returned in the body of the response.

The DSL is very clean and makes API maintenance relatively easy. 

A few other handy links:

* [Grape Project](https://github.com/postrank-labs/goliath)
* [Grape Forum](https://groups.google.com/forum/?fromgroups#!forum/ruby-grape)
* [NewRelic-Grape Gem Info](https://github.com/flyerhzm/newrelic-grape) - NewRelic instrumentation for the Grape API DSL.
* [Heroku example](https://github.com/djones/grape-goliath-example)
* [Grape Intro Video](http://www.confreaks.com/videos/475-rubyconf2010-the-grapes-of-rapid)