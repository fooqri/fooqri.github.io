---
layout: post
title: "Simple state machine example"
date: 2013-01-15 12:24
author: "Patrick Goddi"
comments: true
categories: [ruby, state-machines, development]
redirect_from: /blog/ruby/state-machines/development/2013/01/15/simple-state-machine-example
---
I have been investigating using the ruby [state_machine](https://github.com/pluginaweek/state_machine) gem for a project. State machines can be very handy in simplifying code where objects move through various states. The [state_machine](https://github.com/pluginaweek/state_machine) gem embeds state machine behavior into any class that uses it. My first test was to create a simple todo list example.  The todo list will include a main list that contains items and sublists.  This allows a way to organize items easily into sublists.

A simple way to do this is to declare two classes _List_ and _Item_ and allow an object of class _List_ to contain a list of _Lists_ and a list of _Items_. This approach allows a flat list with many items, or a hierarchical list with top-level items, but also sub-lists that contain their own items. 

In addition to lists and items, I want is to track whether I have completed all of the items in a list. In the case of a hierarchical list this means all items of sub-lists as well. Thus in addition to lists and items, we need to track whether items and lists are in progress or completed.

The next step is deciding on the states of the two object types. For my example, I decided:
* a list will have an initial state of _available_, and will transition to state _started_ when the first item on the list is completed. When all items and sublists are _completed_ the list will move to the state _completed_.
* an item will have an initial state of _available_ and will transition to _completed_ when the item is finished.

Finally I want to inform the user when:
* an item is completed
* a list is completed
* the project is completed (all items and sublists are completed)

Here is a quick example of the code to meet these requirements:

{% gist 4549146 %}

As you can see there is a rich environment for embedding behavior, including adding it in the _state_ definitions, adding it using the _before_transition_ method, and adding it using the _after_transition_ method. You can also define methods inside the state definition so you can extend the functionality of a state.

Now if you load this example in IRB you can play with the lists and items like so:

     load "list_example.rb"
     list = List.new("Groceries", "Get some groceries")
     wf = list.add_list("Whole Foods", "Get some groceries from Whole Foods")
     milk = list.add_item("Milk", "2% Milk")
     strawberries = wf.add_item("Strawberries", "Ripe organic Strawberries"))
     oranges = wf.add_item("Oranges", "Ripe mandarine oranges")

     strawberries.finish 
     =&gt; finished item Strawberries

     oranges.finish  
     =&gt; finished item Oranges
     =&gt; congrats on completing list Whole Foods

     milk.finish
     =&gt; finished item Milk
     =&gt; congrats on completing project Groceries


This was a really simple example, but shows how easy it is to create classes that embed state machines. For more check out the [state_machine](https://github.com/pluginaweek/state_machine) gem.


### State Diagrams

The library also allows you to generate graphs of the states and transitions in each class. For example:

create a Rakefile.rb

     require 'tasks/state_machine'
     require './list_example.rb

Then in terminal execute:

     rake state_machine:draw CLASS=List 

For the _List_ class shown above this will generate a png file named _List_list_state.png_ that looks like the image below.

![](http://media.tumblr.com/d78e332b4656b62dec36c2a2d2408a82/tumblr_inline_mgqav0Q8uW1qz562v.png)

The _List_ class is very simple so the diagram is also simple. In the case of my project there are many states and more complicated transitions between states so the diagram can be very handy to visualize what is happening when  debugging a strange transition,

### Wrapup

This todo list example is very simple but it allows exploring the basic features of the [state_machine](https://github.com/pluginaweek/state_machine) gem, and demonstrates how simple it is to add state machine functionality to classes.  If a class you are designing has variables that keep state, and you are triggering behaviors when those variables change, then a state machine will likely be a more clean approach to organizing behavior in your class. 