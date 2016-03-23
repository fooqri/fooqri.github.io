---
layout: post
title: Org Export Configurations
date: 2016-03-11
published: true
redirect_from: /blog/2016/03/11/Org-Export-Configurations
---

Emacs *org mode* offers a variety of export options that make it easy to look at your notes in different formats, or perhaps make them available for others to view. Three I use regularly are *markdown*, *mindmap*, and *reveal presentation*. 

# My approach to Note Taking

The best way to learn something is to sumarize the topic in your own words, in your own context, and present it to others with concrete examples. But in many cases notes must also serve to provide details that are easily forgotten like code snippets, checklists, etc. Even with detailed notes it is important to refactor the information into your own context to aid learning the topic. For this reason many of my notes on a topic have a *summary* section and a *details* section both organized in an org document. 

Another purpose for notes is information logging, such as meeting notes, project team notes, daily journal, etc. Although *org* does an excellent job of supporting information logging and task management, I will leave that as a topic for a future post.

Ideally the summary of a topic can easily be converted to a presentation, and the details can be converted to a markdown document.   I will describe below how to accomplish this. Further I will describe how to convert the notes to OPML so it can be explored as a mindmap. Also see [Deft + Org for Notes](http://rwx.io/blog/2016/03/10/Deft-and-Emacs-for-Notes/) for information on quick search of all notes. 

# Setting Export Directory

I want to keep everything under the org directory but to keep things tidy create sub directories by export type. The code snippet below when placed in init.el will set the correct export directory based on export type. Thus *opml* documents will be kept in `~/org/export_opml/`, *markdown* documents in `~/org/export_md/`, and *html* documents in `~/org/export_md/`

    (defvar org-export-output-directory-prefix "export_" "prefix of directory used for org-mode export")
    
    (defadvice org-export-output-file-name (before org-add-export-dir activate)
      "Modifies org-export to place exported files in a different directory"
      (when (not pub-dir)
          (setq pub-dir (concat org-export-output-directory-prefix (substring extension 1)))
          (when (not (file-directory-p pub-dir))
           (make-directory pub-dir))))

# Exporting to Markdown

The configuration below will export markdown every time an org file is saved. It will also save a copy of the exported file to my Google Drive folder. This way my notes are always available from any web browser. The [Minamalist Markdown Editor](https://chrome.google.com/webstore/detail/minimalist-markdown-edito/pghodfjepegmciihfhdipmimghiakcjf?hl=en) is a nice tool for viewing these documents on a Chromebook.

The (C-c m) keyboard sequence will open the markdown version of the current buffer in Marked 2. Because all notes are automatically converted the *Marked 2* app will also allow you to follow note links to any interlinked notes. *Marked 2* provides a very nice reading interface for detailed notes so having this option is handy.

    (defun export-org-md-command-events ()
      (interactive)
      (let* ((md-original-filename (concat (file-name-directory buffer-file-name) "export_md/" (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".md"))
             (google-drive-filename (concat  "../Google Drive/notes/" (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".md"))) 
        (execute-kbd-macro (kbd "C-c C-e m m"))
        (copy-file  md-original-filename google-drive-filename t)
        (message  "Saved to Google Drive: %s" (concat (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".md")) )
      )
    
    ;; Auto-export org files to Markdown when saved
    (defun org-mode-export-hook ()
      (when (equal major-mode 'org-mode)
        (add-hook 'after-save-hook 'export-org-md-command-events t t)
      )
    )
    
    (defun markdown-preview-file ()
      "run Marked on the current file and revert the buffer"
      (interactive)
      (execute-kbd-macro (kbd "C-c C-e m m"))
      (shell-command
       (format "open -a /Applications/Marked2.app %s" 
           (shell-quote-argument (concat (file-name-directory buffer-file-name) "export_md/" (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".md"))))
      )
    
    (global-set-key (kbd "C-c m") 'markdown-preview-file)

The markdown conversion works well but if you need to you can  embed markdown directly into your org document at any time using a markdown block. This will allow the markdown to pass through during export so it will be handled properly by the markdown rendering app.

    #+BEGIN_SRC js  :results output drawer
      var s = "JavaScript syntax highlighting"; 
      alert(s);
    #+END_SRC

# Exporting to Mindmap

Mindmaps are a visualization of an outline, and since org mode specializes in keeping notes in a hierarchical fashion it is fairly easy to convert notes to mindmaps. OPML is an XML format for outlines that is supported by all mindmapping  apps. You can use [org-freemind](https://www.emacswiki.org/emacs/FreeMind) to do mindmaps, but I use [org-opml](https://github.com/edavis/org-opml) instead. Follow the [org-opml](https://github.com/edavis/org-opml) installation instructions.

I also use a slight customization of the ox-opml.el file delivered with [org-opml](https://github.com/edavis/org-opml), because I use iThoughtsX and think it is cleaner to put paragraph blocks in notes rather than have them forced into a topic bubble.

    ;; modify original ox-opml.el to put paragraphs into the notes attribute of a topic
    ;; instead of displaying paragraph as topic name.  
    (defun org-opml-paragraph (paragraph contents info)
      (let* ((parent (org-element-type (org-export-get-parent paragraph)))
             (text (clean-text contents)))
        ;; Only display paragraphs when not in a list item
        (unless (eq parent 'item)
          (format "<outline text='notes' note='%s' structure=\"paragraph\"/>"  text))))
    
    (defun org-opml-item (item contents info)
      (let* ((p (car (org-element-contents item)))
             (elements (org-element-contents p))
             (text (mapconcat
                    (lambda (el)
                      (cond ((stringp el) (clean-text el))
                            ((equal (car el) 'link)  
                             (let ((url (org-element-property :raw-link el))
                                   (text (org-element-contents el)))
                               (clean-text (format "%s" (car text)))))
                            ((equal (car el) 'italic)
                             (format "/%s/" (car (org-element-contents el))))
                            ((equal (car el) 'bold)
                             (format "*%s*" (car (org-element-contents el))))
                            ((equal (car el) 'verbatim)
                             (format "=%s=" (org-element-property :value el)))))
                    elements " ")))
        (format "<outline text='%s' structure='list'>%s</outline>" text contents)))

A second modification I use is to change the key-bindings for export because they conflict with markdown export. Below I changed the `?m` in the original `ox-opml.el` file to `?g` so `Export to OPML` will appear in the org export menu under the `g` key, and not `m` key

    :menu-entry '(?g "Export to OPML"
                     (lambda (a s v b) (org-opml-export-to-opml a s v b)))

The Lisp snippet below can be added to init.el and will allow viewing an org buffer as a mindmap using iThoughtsX with the (C-c o) keyboard sequence.

    (defun opml-preview-file ()
      "run iThoughtsX on the current file and revert the buffer"
      (interactive)
      (execute-kbd-macro (kbd "C-c C-e g"))
      (shell-command 
       (format "open -a /Applications/iThoughtsX.app %s"  
           (shell-quote-argument (concat (file-name-directory buffer-file-name) "export_opml/" (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".opml"))))
    )
    
    (global-set-key  (kbd "C-c o") 'opml-preview-file)

# Exporting to Reveal Presentation

Another useful feature is exporting the current org buffer as a [Reveal Presentation](http://lab.hakim.se/reveal-js/) and opening it in a browser. To do this you need to install and configure [org-reveal](https://github.com/yjwen/org-reveal). Once installed you can use the Lisp snippet below, the (C-c p) keyboard sequence will open the the current buffer as a *Reveal Presentation* in Safari (I use Mac).

    (defun 'presentation-preview-file ()
      "run export with ox-reveal on the current file and open browser"
      (interactive)
      (execute-kbd-macro (kbd "C-c C-e R R"))
      (shell-command 
       (format "open -a /Applications/Safari.app %s" 
           (shell-quote-argument (concat (file-name-directory buffer-file-name) "export_html/" (file-name-sans-extension (file-name-nondirectory buffer-file-name)) ".html"))))
    )
    
    (global-set-key  (kbd "C-c p") 'presentation-preview-file)

## Hiding Content

I mentioned above that I like to organize my notes with both a summary for presentation, and details that would not work well in a presentation. To make it easy to hide content from the various export modules I added the code below to my init.el file. 

     (defun set-ignored-headlines-tags (backend)
     "Remove all headlines with tag ignore_heading in the current buffer. 
        BACKEND is the export back-end being used, as a symbol."
     (cond ((org-export-derived-backend-p backend 'md) (setq  org-export-exclude-tags '("noexport" "mdignore")))
           ((org-export-derived-backend-p backend 'reveal) (setq  org-export-exclude-tags '("noexport" "revealignore")))
           ((org-export-derived-backend-p backend 'opml)  (setq  org-export-exclude-tags '("noexport" "opmlignore"))) 
           (t (setq  org-export-exclude-tags '("noexport")))
       ) 
    )

Now I can hide content from reveal by adding a *:revealignore:* tag to the heading. The *:opmlignore:* and *:mdignore:* work similarly. *:noexport:* means hide from all exports. The tags support hierarchy so will hide any sub-headings.

    * My Slides :mdignore:opmlignore:
     ** Topic 1
        Slide content
     ** Topic 2
        Slide content
    * My Detailed Notes  :revealignore:
     ** Chapter Notes
     ** Code Experiments :opmlignore:

# Conclusion

With this setup is is easy to keep notes in a fashion that makes them easy to use in a number of formats, including presentations, mindmaps, and markdown documents. Org mode also supports the concept of [publishing](http://orgmode.org/manual/Publishing.html) that is useful when sharing specific content, for example exporting specific notes to a web site along with images and attachments used in the notes.
