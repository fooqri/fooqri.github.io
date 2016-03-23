---
layout: post
title: "Treetop and Parsing Expression Grammars (PEGs)"
date: 2012-12-30 04:54
comments: true
author: "Patrick Goddi"
categories: [parsers]
redirect_from: /blog/2012/12/30/treetop-and-parsing-expression-grammars-pegs
---
Over the holiday I had some time to investigate parsing expression grammers. I had done work in Lex and Yacc many years back when I was responsible for some kernel functionality and related system management kernel commands for a proprietary commercial operating system. I don't remember fondly my time working with Yacc. But then I read about [PEGs](http://en.wikipedia.org/wiki/Parsing_expression_grammar) and the [Treetop](http://treetop.rubyforge.org/) Ruby library. It allows the use of simple grammer rules based in regular expressions and creates a parser ruby class from the grammer that can then be used in a ruby program. It also allows ruby blocks to be embedded directly into the grammer rules. 

For our startup we have a core feature that includes some user generated instructions that are meant to create a mobile experience for others to participate in, sort of a simple [FSM](http://en.wikipedia.org/wiki/Finite-state_machine) driven experience. We could present the authoring environment in  a form-based interface, but this seemed a bit too restrictive. We may still go with forms, but I wanted to try an intermediate format using user readable text files, so we could write up test cases fast and easy, and compile them into the FSM class. I was also inspired by the simplicity of the [markdown](http://daringfireball.net/projects/markdown/) syntax and the way it is used in [FoldingText](http://www.foldingtext.com/). It may not pan out but I really had fun working on it.
 
I will post some code in the future, but thought I would post a link to the [tutorial](http://www.trsolutions.biz/blog/2010/03/10/treetop-introductory-tutorial-1-of-10/) I found very helpful in getting my experiment up and running quickly. It is a well written tutorial that starts with the basics of getting a simple parser working, and then explores just enough complexity to get you to a place where a moderately complex grammer can be written. I think this is a great tool for any Ruby developer's tool belt; and for certain classes of problems related to parsing information it is a very eloquent approach.