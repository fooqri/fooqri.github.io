---
layout: post
title: "Parsing a simple markdown style list in Ragel"
date: 2013-01-19 13:04
author: "Patrick Goddi"
comments: true
categories: [ruby, parsers]
redirect_from: /blog/ruby/parsers/2013/01/19/parsing-a-simple-markdown-style-list-in-ragel
---
In an earlier post [Simple state machine example](http://www.pragmaux.com/post/40689737812/simple-state-machine-example), I provided an example of using the Ruby _state_machine_ gem to create a state machine for handling a simple list of tasks. In this post I will provide a similar but not exactly compatible description of building a parser to read lists from a text file. In this example I use the markdown syntax for lists, where items can be placed hierarchically, thus removing the need for a separate "list" object. 

I found the [Ragel documentation](http://www.complang.org/ragel/ragel-guide-6.7.pdf) to be excellent. The only issue is a lack of practical examples. Given the dearth of examples available, I though I would add my +1 example to help the cause. If you are serious about using Ragel I recommend reading the documentation start to finish quickly, then a second go through taking notes on key items like default machines, syntax, priorities, actions, etc before building a parser. Having a strong base will help tremendously when using examples. 

There are three files involved in this solution to the list problem: 

* lists.txt: a data file that contains two lists for the parser to parse.
* mdlist.rb: a ruby class that will call the parser and output the list returned from the parser.
* mdlist_parser.rl: A file that will be used by Ragel to create a parser class definition (mdlist_parse.rb).

I added all three files to one gist, which is shown below. Below the lists.txt data file uses a markdown like syntax where hierarchy is expressed through indentation (4 spaces or a tab).

<!--more-->

{% gist 4573704 %}

To create an app that supported operating on these lists you would need to parse the list and create objects that could be operated on. Perhaps adding checkboxes in a UI, or strike-through font when the item is marked complete.

In this example I am using Ragel, which uses a set of state machine definitions to generate a state machine. In this case I am using Ragel to generate a parser to parse lists similar to the ones shown in lists.txt. In Ragel you specify a Ruby class that uses a series of preprocessors (%%) that are processed by the Ragel library.  Ragel will replace these blocks and preprocessor commands with ruby parser code and a parse table; resulting in a state machine for parsing the file.  The documentation will describe all of the required preprocessor commands for Ruby. Ragel supports many languages and the preprocessor commands differ slightly for different languages. Check the documentation for meaning.

The bulk of the instructions for creating a parser are inside the _%%{ }%%_ block. The block is made up of machine definitions and actions. Ragel state machines recognize byte sequences as regular expression machines do, but can also execute code at arbitrary points in the recognition of a regular language (actions).  Here regular expressions are used to define a regular grammar, see type-3 in the [Chomsky hierarchy](http://en.wikipedia.org/wiki/Chomsky_hierarchy).  

Thus when you see the statement:

    task_title =  [^\n]+ [\n]

this is defining a machine (_[^\n]+ [\n]_) and assigning it a name _task_title_. The Ragel documentation refers to the right side of the expression as a _regular expression machine_ or _machine_, this is roughy equivalent to production rules in tradition grammar design. Using named expressions this way allows grammar rules to be built up recursively, much like non-terminals are used in traditional grammar definitions.

Thus an expression like:

   task = (task_header &gt;MarkTaskStart) . task_item*; 

uses the rules _task_header_**** and _task_item_**** in the definition of the expression. Ragel expressions look unusual at first because they are both defining a grammar and embedding behavior (code). For example the above expression includes a reference to of a block of code **_MarkTaskStart_** that should be executed when the **_task_header_** machine is matched. These code blocks are called _actions_ in Ragel. It can be useful to use a convention like all lowercase for rules, and CamelCase for actions to make the expressions easier to read.

Ragel defines a syntax for specifying when an action is to be called relative to state transitions between machines. For example before a transition, after a transition, or at the end of file, etc. The documentation is very good, though it is terse.

<table border="1">
<col style="padding-right: 30px;" />
<col style="padding-right: 30px;" />
<col />
  <tr>
    <th>Name</th>
    <th>Syntax</th>
  </tr>
  <tr>
    <td style="width: 200px;">entering action</td>
    <td style="width: 200px;">expr &gt;action</td>
  </tr>
  <tr>
    <td style="width: 200px;">finishing action</td>
    <td style="width: 200px;">expr @ action </td>
  </tr>
    <tr>
    <td style="width: 200px;">all transitions action</td>
    <td style="width: 200px;">expr $ action</td>
  </tr>
  <tr>
    <td style="width: 200px;">leaving actions</td>
    <td style="width: 200px;">expr % action</td>
  </tr>
</table>
<br />
Ragel also allows you to embed error handling behavior using a similar mechanism.

Finally, one of the challenges of regular grammars is the requirement that they are [DFA's](http://en.wikipedia.org/wiki/Deterministic_finite_automaton) and thus need to be deterministic. Ragel provides a mechanism for including priorities in the case where multiple next states are possible; you can define which state will be taken. For more see the Ragel documentation on priorities and guarded expressions. The reason I suggested reading through the documentation prior to reading example grammars is that Ragel expressions can begin to look very confusing if you are not versed in the difference between the syntax associated with machines, actions, priorities and guards, since they all appear intermingled in a Ragel expression.

To create a parser for the _mdlist_parser.rl_ file shown above use this command:

     ragel -R mdlist_parser.rl

This will create a parser written in ruby called _mdlist_parser.rb_ that can be included into your Ruby program.  

Now we need a simple Ruby program to use the parser, I am including this because I didn't see a lot of examples for how to do this so wanted to add one here.  

The simple ruby class defined in _mdlist.rb_ will open the data file and read it in to a string, and pass the string to the parser. The parser will return a Ruby object that has a _lists_ method that returns the list in a data structure. The above class will then output the list formatted to show the hierarchy. The list could easily be used to create a list object that includes the state machine from my earlier [state machine](http://www.pragmaux.com/post/40689737812/simple-state-machine-example) post. 

I will assume you have Ragel, installed, if not get it [here](http://www.complang.org/ragel/). To see the parser in action you need all three files (mdlist_parser.rl, mdlist.rb, lists.txt) in the same directory and then take these steps:

1. **run the ragel parser:**   ragel -R mdlist_parser.rl
2. **run irb** and enter the following into irb:

     * load "mdlist.rb"
     * list = MDList.new("lists.txt")

You should see the output of the puts statements displaying the lists data structure with information about the hierarchy of the list. It would be easy to replace the puts with a call to a method like add_item() from my state_machine example referenced earlier. 

That's it. Defining grammars and using parser generators can seem challenging at first, but once you get through a few examples and build a simple grammer it will become very simple, since the rules are really very simple. The language of grammar definition can be challenging at first,  but just try to understand the concepts and don't get too bogged down in the terminology. Ragel is a very powerful tool for any developer to have in their tool belt, especially if you are interested in building high performance APIs, it combines a powerful parser generator with an expressive syntax for generating powerful state machines. To fully understand this and other examples check out the Ragel documentation and tutorials listed below.

* [Ragel Home](http://www.complang.org/ragel/)
* [A simple intro to writing a lexer with Ragel.](http://thingsaaronmade.com/blog/a-simple-intro-to-writing-a-lexer-with-ragel.html)
* [A Hello World for Ruby on Ragel 6.0](http://www.devchix.com/2008/01/13/a-hello-world-for-ruby-on-ragel-60/)
* [Ragel State Charts](http://www.zedshaw.com/essays/ragel_state_charts.html)
* [Regular Expressions Will Stab You in the Back](http://tech.blog.cueup.com/regular-expressions-will-stab-you-in-the-back)

Also see this great [ Consuming Gherkin: One Byte at a Time video](http://www.confreaks.com/videos/491-rubyconf2010-consuming-gherkin-one-byte-at-a-time) intro of Mike Sassak &amp; Greg Hnatiuk discussing their experience using Ragel for the Cucumber parser. 