---
layout: post
title: "Org Mode ES2015+ Code Blocks"
date: 2015-10-06 16:57
comments: true
categories: 
---
I use __emacs org mode__ to keep notes including code nodes that support inline execution.  It is convenient for keeping useful code snippets, as well as experimenting while taking notes.  Because of features like [Org + Deft](http://rwx.io/blog/2013/03/04/nvalt-and-emacs/) it is really easy to find the sweet spot between kepping coding notes organized but aslo easily searched.

As I have started to explore more ES6 and even ES7 features I wanted a way to transpile on the fly in my coding notes. It turns out it is very easy.

First make a few changes to the emacs environment so you can use JavaScript in __org mode__, as well as find local _node.js_ modules you have installed. Replace _"~/org/node_modules"_ in the config below with the location of any local node modules you want to pick up. Using this approach you don't have to pollute the global node_module directory if you don't want to.

Add the following to your emacs init.el file and evaluate it (or restart emacs).

```
(setenv "NODE_PATH"
  (concat
   "~/org/node_modules" ":"
   (getenv "NODE_PATH")
  )
)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((js . t)))
```
Next install the babel npm module globally, this allows you toc call babel from the command line also. Then install any local modules you need to use. I chose to install them from the ~/org directory where my notes are kept, but anywhere works as long as you have the correct path set above.

```
npm install -g babel
npm install mongodb
npm install bluebird
```

The default  org-mode interpreter for js is node, so you need to have that installed and its path set. But the cool thing is that you can change the interpreter inline in your code blocks in the cases you want to experiment with upcoming language features. To do this you simply tell _org mode_ to use an alternative interpreter; in this case __babel-node__, which also transpiles.

Adding  _:cmd "babel-node"_   after the  _#+begin_src js_ tells _org mode_ to use the babel_node command instead of the default JavaScript interpreter. The _:results output_ tells _org mode_ that the results will be from an output statement _(using console.log() for JavaScript)_

 
       #+name: production.activities.findOne
       #+begin_src js :cmd "babel-node" :results output drawer
          (async function(){
              try {
                  let MongoDB = require('mongodb');
                  let Promise = require('bluebird');
                  Promise.promisifyAll(MongoDB);
                  let db = await MongoDB.MongoClient.connectAsync(process.env.PW_PROD_DB);
                  let activityCol = db.collection('activities')
                  let result = await activityCol.findOne();
                  db.close();
                  console.log("first activity name: ", result.name);
                }
               catch(err){
                 consule.log(err);
                 throw err;
               }
             })()
       #+END_SRC
 
Now, simply place the cursor anywhere in the block and execute it using C-c C-c. The results will be placed under the block in second block entitled: _#+RESULTS:_

The block can be executed as often as you like and the results will be refreshed. See the updated example with its results block below.
 
       #+name: db.activities.findOne
       #+begin_src js :cmd "babel-node" :results output drawer
          (async function(){
              try {
                  let MongoDB = require('mongodb');
                  let Promise = require('bluebird');
                  Promise.promisifyAll(MongoDB);
                  let db = await MongoDB.MongoClient.connectAsync(process.env.PW_PROD_DB);
                  let activityCol = db.collection('activities')
                  let result = await activityCol.findOne();
                  db.close();
                  console.log(`The first activity name is ${result.name}`);
                }
               catch(err){
                 consule.log(err);
                 throw err;
               }
             })()
       #+END_SRC

       #+RESULTS: db.activities.findOne
       :RESULTS:
       The first activity name is Shopping
       :END:

You can see several new and experimental language features including _async functions_, the _await_ keyword for performing a non-blocking wait on a promise to complete, and _template strings_.