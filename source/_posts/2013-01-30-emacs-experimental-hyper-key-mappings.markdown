---
layout: post
title: "Emacs Experimental Hyper-Key Mappings"
date: 2013-01-30 10:19
comments: true
categories: 
---
In a previous post [Remapping My Caps Lock Key](http://www.pragmaux.com/post/39243391147/remapping-my-caps-lock-key) I mentioned that I remapped my caps-lock key to escape, but also created a "hyper-key" (ctrl-shift-cmd-opt) when the caps-lock key is held down. This opens up a keyboard worth of new shortcuts for emacs. Here are a few I have been playing with for the past few days. An alternative key mapping would be to map the hyper key to holding down the tab key, if you already have the caps lock key mapped to control, and thus muscle memory might preclude this mapping from working for you.

H is the remapped caps-lock HyperKey from my earlier post, which translates as C-M-S-s in the emacs init.el key-mappings. I include an init.el excerpt at the end of the post for all of these mappings.

* (H-l) This will mark the entire current line, from any position on the line. Using the arrow keys will extent the selection one line at a time either up or down.
* (H-f) This invokes text expansion for code completion, I do this a lot so I wanted it to be very comfortable.
* (H-3) This invokes the comment/uncomment function on a region, ruby comment is the # so I thought I would try this binding.
* (H-Right Arrow) This opens a new window to the right of the current window, I do this often enough I wanted it to be quick
* (H-Left Arrow) This closes the current window, sort of the opposite of Right arrow.
* (H-Down Arrow) This opens a new window below the current window
* (H-p) In the current window switch to the previous buffer
* (H-n) In the current window switch to the next buffer
* (H-delete) Kill this buffer
* (H-w) Quick copy line, pressing multiple times adds more lines to the copy
* (H-k) Quick cut line, pressing multiple times adds more lines to the cut
* (H-c) Copy region into register (prompts for register number)
* (H-v) Paste from register (prompts for register number)
* (H-spacebar) Open a popup shell in directory of current buffer.
* (H-e) Eval buffer, mostly used to eval init.el after tweaks

I will likely be tweaking more in the upcoming weeks as I experiment with key mappings, I will post an update after I get a chance to work with the hyper-key for a while, and settle on a favorite set of key-mappings. See the excerpt from my init.el below.

{% gist 5691402 %}
