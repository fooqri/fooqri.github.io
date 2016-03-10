---
layout: post
title: "nvALT and Emacs"
date: 2013-03-04 11:19
comments: true
author: "Patrick Goddi"
categories: [emacs, productivity] 
---
In a previous post [wiki-searchable-notes](/blog/2012/12/17/wiki-plus-searchable-notes/) I mentioned that I was using nvALT for note taking. nvALT is a very simple way to create and search notes and store them in flat files that can be used by other tools. One use is publishing to a github wiki, today I will discuss another.

I am an Emacs user and often found myself dropping out of emacs to find a note I needed in nvALT. I went looking for the best way to index and access my nvALT notes inside Emacs, and found the very cool emacs script called [Deft](http://jblevins.org/projects/deft/) that works with [EMacs Markdown Mode](http://jblevins.org/projects/markdown-mode/) to create the equivalent of nvALT inside of emacs. It can be configured to work with the nvALT repository so they work well together.

A few pointers...

* If you use markdown in nvALT as I do, follow the instructions to install [markdown-mode](http://jblevins.org/projects/markdown-mode/) via git clone.
* Follow the instructions to install  [Deft](http://jblevins.org/projects/deft/) via git clone. It is an active repository, so clone makes keeping up-to-date easy. Also update init.el to require the deft.el script.
* For markdown and nvALT using the flat file config (see  [wiki-searchable-notes](http://www.pragmaux.com/post/38158334752/wiki-searchable-notes) for flat file config) you need to add a few additional expressions in init.el. Add these four lines as discussed on the deft documentation.
```
(setq deft-extension "md")
(setq deft-directory "~/Development/wikis/Notes.wiki/")
(setq deft-text-mode 'markdown-mode)
(setq deft-use-filename-as-title t)
```
* Follow the instructions to map a keyboard shortcut to open deft. I use H-d (see my [emacs hyper-key post](http://www.pragmaux.com/post/41867238595/emacs-experimental-hyper-key-mappings) ) but a simple function key mapping would be.
```
(global-set-key [f8] 'deft)
```      
* Create a symlink from ~/.deft to your nvALT notes directory, this is shown in the nvALT preferences under the notes tab. See example below.
```
ln -s ~/Documents/notes/ .deft
```
When you eval init.el or restart emacs you should be set. Fire up Deft and the UI will operate just like nvALT, only it works in an Emacs buffer!!

      