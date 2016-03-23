---
layout: post
title: "Screen capture goodness..."
date: 2012-01-17 14:17
comments: true
author: "Patrick Goddi"
categories: [hacks, productivity]
---

### tl;wr
Take the shell script from below and create a TextExpander snippet to save any image in your OS X clipboard to disk with a unique uuid.png name, and automatically create a markdown image link that is pasted in place in your editor.

### verbose
When making notes on wireframes, screen designs, activity diagrams, etc, I have a particular workflow where I do a screen capture and want to link the result in my markdown notes or from our project wiki. The power of markdown text files is their portability, the challenge can be losing the rich cut and paste of apps like Evernote. 

In a previous post <a href="http://fooqri.tumblr.com/post/38158334752/wiki-searchable-notes" title="Wiki + Searchable Notes">Wiki + searchable notes</a>. I mentioned that I was now using the github clone feature for the wiki, allowing me to work on the wiki locally and then push changes to the server with git push. Another benefit of this approach, it makes it very easy to add images to the wiki. 

The problem was it took too many steps to go from capturing the screen, saving it, and finally linking to it in the wiki/notes file. So I created a TextExpander snippet to do all of this in 2 steps (OSX only)

1. screen capture (ctrl-cmd-shift-4)
1. type "wpng" into the editor where I want the image to be placed.


First you need <a href="http://smilesoftware.com/TextExpander/index.html" title="TextExpander">TextExpander</a> and also you need to install <a href="https://github.com/jcsalterego/pngpaste" title="pngpaste">pngpaste</a> a small bit of code that handles saving a clipboard image to a png file.

Then you just need this snippet (I used "wpng" as the snippet abbreviation):

{% gist 4321473 %}

I chose to just use a UUID for the file name to keep it simple and unique for each file.

I added this as a snippet in TextExpander and now instead of 10+ steps across 3 apps my workflow for getting a screen capture into a wiki page is this:

1. screen capture (ctrl-cmd-shift-4)
1. type "wpng" into the editor where I want the image to be placed. 

The result: typing "wpng" causes the last clipboard item to be saved as a png in the wiki images directory and the "wpng" text I just typed is replaced with the markup for the image that was just saved. Quick and simple. 