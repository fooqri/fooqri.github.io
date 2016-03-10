---
layout: post
title: "Deft and Emacs for Notes"
date: 2016-03-10
published: false
---

In the [nvALT and Emacs post](http://rwx.io/blog/2013/03/04/nvalt-and-emacs/) I described an integration between *nvAlt* and *Emacs* using [Deft](http://jblevins.org/projects/deft/) for *markdown* notes. I the past year I have moved to using *Deft* for *org* notes rather than *markdown* notes. The nice thing about combining Deft with Org is that your notes are indexed and easy to find using Deft, but also retain all of the power of Org to orgainize and present information. For example typing *parsing* into **deft** quickly cuts down hundreds of org text notes to the handful that have the tag or word **parsing** in them. Deft makes it easy to create new notes also, simply type a title and hit *ctrl-return* to create a new note with that title.

![img](/images/750af164-e70b-11e5-8302-040cce2069a4.png)

Below I describe setting up Deft for emacs, and show my current customization's.  Org also supports export to many different formats. In a future posts I will cover my setup for exporting notes to *markdown* documents, *reveal* presentations, and even *mindmaps*. 

Follow the instructions at [Deft](http://jblevins.org/projects/deft/) to install from source (usually the latest version this way) or use the Emacs package installer as shown below.

    M-x package-install deft

I prefer to use Deft for *org* files and not others (txt, md, etc), so that is reflected in my configuration below. Using [this technique](http://rwx.io/blog/2012/12/30/remapping-my-caps-lock-key/) I converted the tab key into a hyper-key (C-M-S-s), so with the key mapping below Deft can be called up with **tab-d** This technique is nice, because the tab key still works for tabbing, but when held down it acts like an additional modifier key that can be use in emacs key bindings.

    (require 'deft)
    (setq deft-default-extension "org")
    (setq deft-extensions '("org"))
    (setq deft-directory "~/org")
    (setq deft-recursive t)
    (setq deft-use-filename-as-title nil)
    (setq deft-use-filter-string-for-filename t)
    (setq deft-file-naming-rules '((noslash . "-")
                                   (nospace . "-")
                                   (case-fn . downcase)))
    (setq deft-text-mode 'org-mode)
    (global-set-key (kbd "C-M-S-s-d") 'deft)
    (global-set-key (kbd "C-x C-g") 'deft-find-file)
