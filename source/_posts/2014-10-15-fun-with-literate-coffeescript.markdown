---
layout: post
title: "Fun with Literate CoffeeScript"
date: 2014-10-15 16:53
comments: true
categories: poggr literate-coffee-script
---

As an emacs/<a href="http://orgmode.org/" target="_blank">org-mode</a>/<a href="http://orgmode.org/worg/org-contrib/babel/" target="_blank">babel</a> user I have always been fascinated with the potential of <a href="http://en.wikipedia.org/wiki/Literate_programming">literate programming</a> and combining inline code in my notes. I have many org-mode documents that interactively execute code for various tasks and procedures. These tasks includes certain maintenance activities, or destructive operations I don't want to get wrong. I have an entire org document devoted to db maintenance, filled with Ruby code to execute complicated db queries and operations.  It is nice to see the example code inline in my notes, and be able to modify the code and execute it directly in my notes. This works especially well for checklist types of notes where calculations or actions are called for. You might even say org-mode was one inspiration for building _<a href="http://www.poggr.com/home" target="_blank">poggr.com</a>_; creating a browser based tool that is simple, flexible, and powerful for creating interactive and compelling documents that work in any web browser.

The potential of browser-based literate programming is why I find the idea of _Literate CoffeeScript_ facinating. It is not just the idea of documenting code or even the idea of describing code in a blog post. It is the idea of creating flexible and effective browser based _task_ and _tool_ documents. The power in these types of documents is you see the code you are executing, which is extremely useful for programmer's notes. It seems literate CoffeeScript might have something to say about how to create browser-based interactive notes that include inline code, like emacs/org-mode/babel has done for emacs users. 

Since _<a href="http://www.poggr.com/home" target="_blank">poggr.com</a>_ supports compiling CoffeeScript into JavaScript  I decided to turn on literate CoffeeScript and give it a go to see if this is a legitimate way to combine code and blogging in a single pogg document.

### Poggr CoffeeScript Compilation 
The way poggr works is that when you save a _CoffeeScript_ document _poggr_ keeps both source code and compiled _JavaScript_ code. Just like when you save a _markdown_ document poggr saves both the source markdown and the compiled html. When a document is requested using a _poggid_ in an http request, poggr will deliver the compiled code unless a query parameter is used to request source. This works out quite well in most cases, since the compiled version is what browsers are expecting (html, css, JavaScript). This model allows poggr to support other markup and languages like _less_, _scss_, _yaml_, etc to work similarly.

_LitCoffeeScript_ is unique in that compilation produces two documents (markdown -> html) and (CoffeeScript -> JavaScript). Thus, one challenge is knowing whether a document request is for the  html or JavaScript version. I felt compelled enough to experiment that I added a test case where adding a __.js__ extention to a _poggid_ will return the JavaScript, otherwise it will return the compiled html version of the document.

```
...
<script src="//www.poggr.com/peJo73gk0Nx:dxkfEl2RANx.js">
...
```

I wanted to pick something fun to experiment with so I chose a game originally created by _[Marc-André Cournoyer](https://gist.github.com/macournoyer)_.
in his _<a href="https://gist.github.com/macournoyer/7357908" target="_blank">game.litcoffee</a>_ gist.

You can see my version of the  literate CoffeeScript post in action <a href="http://goddip.poggr.com/peJo73gk0Nx:dxkfEl2RANx" target="_blank">here</a>. What you will notice it the game is running as part of the post, and all the code is also embedded in the post. This may look like a normal code example post, but if you look at the  <a href="//source.poggr.com/peJo73gk0Nx:dxkfEl2RANx" target="_blank">source code</a> you will see at the end of the source document that the post actually loads the js version of itself. So by saving a literate CoffeeScript document you automatically get a blog post; in addition all of the fenced  CoffeeScript code is compiled into a JavaScript document.  Any changed inline code is re-compiled into an updated JavaScript document with each save. ___Mind Blown right!___

I can't see it replacing my emacs/org/babel workflow yet, but it certainly opens some possibilities for having a set of private online notes, experiments, and tools I can call up in any browser to edit and execute. One down-side is while emacs is mode-less in that editing and execution happen together, the browser model is built for view-only. Poggr is built on browser-based document editing, but viewing the rendered results is still a separate action. Although it is not exactly the same emacs/org-mode, there are cases where it is actually better. Emacs does not excel where rich visualization and rendering are beneficial, this is what the browser does best.

When I get a chance I will port a few of my org-mode notes over to literate CoffeeScript documents on poggr and make a note here when they are up. 