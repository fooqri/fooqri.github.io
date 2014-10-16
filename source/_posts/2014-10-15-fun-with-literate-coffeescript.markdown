---
layout: post
title: "Fun with Literate Coffeescript"
date: 2014-10-15 16:53
comments: true
categories: poggr literate-coffee-script
---

As an emacs/org-mode user I have always been enamored with the possibility of combining inline code in my notes. I actually have a number of org-mode files that interactively execute code for procedures where I may go long periods of time between use. This includes certain maintenance activities, or destructive operations I don't want to get wrong. It is nice to see the example code inline in my notes, and be able to execute it directly in my notes. 

That is why I find the idea of _Literate Coffeescript_ facinating. It is not just the idea of documenting code or the idea of describing code in a blog post. It is actually writing a blog post where the code is extracted and compiled and available as a javascript document seperate from the document it was created in.

Since _[poggr.com](//www.poggr.com)_ supports compiling coffeescript into javascript  I decided to turn on litcoffeescript and give it a go to see if this is a legitimate way to combine code and blogging in a single pogg document.

### Poggr Coffeescript Compilation 
The way poggr works is that when you save a coffeescript document poggr keeps both source code and compiled javascript code. Just like when you save a markdown document poggr saves both the source markdown and the compiled html. When a document is requested in an http request poggr will deliver the compiled code unless a query parameter is used to request source. This works out quite well in most cases, since the compiled version is what browsers are expecting (html, css, javcript). This model allows other markup like scss, yaml, etc to work similarly.

_Litcoffeescript_ is unique in that the compiled output is both html and javascript, and in some cases you may want the javascript without the html. I felt compelled enough to experiment that I added a test case where adding a __.js__ extention will return the javascript, otherwise it will return the compiled html version of the document.

```
...
<script src="//www.poggr.com/peJo73gk0Nx:dxkfEl2RANx.js">
...
```

I wanted to pick something fun to experiment with so I chose a game originally created by _[Marc-André Cournoyer](https://gist.github.com/macournoyer)_.
in his _[game.litcoffee](https://gist.github.com/macournoyer/7357908)_ gist.

You can see my version of the  litcoffeescript post in action [here](http://goddip.poggr.com/peJo73gk0Nx:dxkfEl2RANx). What you will notice it the game is running as part of the post, and all the code is also embedded in the post. This may look like a normal code example post, but if you look at the [source code](//source.poggr.com/peJo73gk0Nx:dxkfEl2RANx) you will see at the end of the source document that the post actually loads the js version of itself. So by saving a litcoffeescript document you automatically get a blog post and all of the fenced  coffeescript code is compiled into a javascript document.  __Mind Blown right!__


So basically any change to the inline code automatically re-compiles the js document with each save. I can't see it replacing emacs/org/babel for me but it certainly opens some possibilities for single page interactive blog posts where displaying the code is important.