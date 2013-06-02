---
layout: post
title: "Wiki + searchable notes."
date: 2012-12-17 13:25
comments: true
author: "Patrick Goddi"
categories: 
---
For our startup I have been using github wiki to keep the product specs, design docs, user stories, etc organized and up-to-date. The nice thing about github is you can clone the wiki and work on it locally and push changes up to the server. See this <a href="https://github.com/wicketstuff/core/wiki/Editing-Wiki-Locally" title="writeup" target="_blank">writeup</a> for more info. This is handy because you can then work on the wiki using markdown syntax in a regular text editor versus a web page editor.

The ease of this made me wonder if there was a way to do my normal note taking, code journalling, etc in markdown vs Evernote. I did some looking around and found <a href="http://brettterpstra.com/project/nvalt/" title="nvAlt" target="_blank">nvALT</a>, which is a markdown based notebook that can save notes as flat .md files.

So as an experiment I cloned my personal notes wiki from github.  After configuring nvALT to use the cloned wiki directory as its directory I could immediately see and search all of my wiki files as nvALT note files. Also I could add new files and they would now become linkable as wiki files. So basically nvALT acts as a note taking system, but notes can be also linked together via a mmd link notation that is supported by the github wiki. You can install the <a href="https://github.com/github/gollum" title="Gollum">gollum</a> gem and interact with the wiki locally to test the wiki pages.

So I can now create, edit, search notes in markdown, but also link them, as well as view them as a wiki.

I will post again after a few weeks trying out the solution with more info on how it is working. 