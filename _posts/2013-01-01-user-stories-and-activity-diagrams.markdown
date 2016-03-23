---
layout: post
title: "User Stories and Activity Diagrams"
date: 2013-01-01 10:10
comments: true
author: "Patrick Goddi"
categories: [hacks, design]
redirect_from: /blog/hacks/design/2013/01/01/user-stories-and-activity-diagrams
---
I have been using Omnigraffle to create activity diagrams associated with user stories. Some people may find this overkill but I find doing these diagrams makes transitions clear that might otherwise be missed until later when they lead to costly re-architecting of the screens and flows.

I use Omnigraffle for UI wireframes, so it seemed natural to use it for activity diagrams, which is what I have been doing.  The issue is keeping the diagrams up to date.  Today, while playing with the [Ragel](http://www.complang.org/ragel/) state machine compiler I discovered Ragel's awesome states/transitions diagramming feature. I learned the feature uses [Graphviz](http://www.graphviz.org/) to create the diagrams from the parser grammar.  This led me to [Ruby Graphviz](https://github.com/glejeune/Ruby-Graphviz/), a Ruby library for interacting with Graphviz. It got me thinking that maybe there was a simple DSL that could be used to describe UI activities and screens and then automatically generate diagrams from the description. This would make keeping descriptions and diagrams in sync very easy. 

My first step is always to get a piece of the most basic idea working, then add another piece, etc until a basic prototype is complete. Given this approach the first step was to use ruby-graphviz to create a basic diagram similar to one of our activity diagrams (a very basic one). So here was a quick pass experiment for using ruby-graphvis to create a diagram. The next step would be to define a basic DSL and then write a parser and state-machine and incorporate the graph creation into the state machine as it parses the DSL activity description.

{% gist 4431708 %}

This above very simple example creates the diagram below.

![](http://media.tumblr.com/61f780009a654f9724bcd4a9c703d9b4/tumblr_inline_mfz8syDgFP1qz562v.png)

This needs some cleanup of the aesthetics but the possibility is interesting. The next steps will be to come up with a very simple dsl, as simple as possible, maybe something that is markdown compliant so it fits inside our wiki pages cleanly. It would need to cover start and end states as well as intermediate state nodes. It would need to also handle decision points (diamonds) as well as transitions (edges) and notes. The simplest form would be to allow listing all nodes and all decisions, and then listing the connections between them. Labels would also be needed on all of these. IDs would probably help for wiring up the connections.

Then it is a matter of running a parser on the wiki pages, looking for the syntax associated with the activity descriptions and generating a diagram using some ruby code. This might be a nice experiment to familiarize myself with Ragel to better understand its strengths and capabilities. 

I hope to get to spend some free time on this over the coming weeks, as it seems like a fun side project.
