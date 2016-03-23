# Seth Holloway - https://github.com/smholloway
#
# The Jekyll Alias Generator, https://github.com/tsmango/jekyll_alias_generator,
# is a handy way to create meta refresh redirects from an old URL pattern to the
# new. This is helpful when changing blog formats as it helps maintain search
# engine rankings. Unfortunately, you have to create your own alias entries.
# With over 400 posts, I had # to automate it! This script will find all
# Markdown files in your _posts directory then generate an alias entry under the
# title attribute.
#
# To use, edit the alias_link_from_post_file to return your previous URL format
#
# One easy way to test: place a return statement after line 33

#!/usr/bin/env python
import os
import glob
import fileinput

def main():
    for f in glob.glob('_posts/*.md'):
        add_alias_line_to_post(os.path.basename(f))

def alias_link_from_post_file(f):
    ''' Converts a filename like 2013-04-26-thoughts-on-learning-clojure.md
        to /blog/2013/04/26/thoughts-on-learning-clojure'''
    post_title = os.path.splitext(f)[0].split('-')
    year       = post_title[0]
    month      = post_title[1]
    day        = post_title[2]
    title      = '-'.join(post_title[3:])
    base_path  = '/blog'
    link       = '/'.join([base_path, year, month, day, title])
    return link

def add_alias_line_to_post(f):
    alias_link = alias_link_from_post_file(f)
    print 'Adding alias: {0} to {1}'.format(alias_link, f)
    found_title = False # add the alias once after the first title attribute
    for line in fileinput.input(f, inplace=1):
        print line,
        if line.startswith('title: ') and not found_title:
            print 'alias: {}'.format(alias_link)
            found_title = True

if __name__ == '__main__':
    main()
