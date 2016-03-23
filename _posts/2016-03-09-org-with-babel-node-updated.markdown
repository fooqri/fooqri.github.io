---
layout: post
title: "Org Mode ES2015+ Code Blocks (updated)"
date: 2016-03-09 16:57
comments: true
categories:
redirect_from: /blog/2016/03/09/org-with-babel-node-updated
---
- **Note:** In this post I have updated the instructions for use with *Babel 6x*. For *Babel 5x* see the [original post](/blog/2015/10/06/org-with-babel-node/).

Babel 6x is a significant change from Babel 5x, as the *cli* is now a separate node module called _babel-cli_ and transforms are now also delivered as separate packages.

First make a few changes to the emacs environment so you can use JavaScript in __org mode__, as well as find local _node.js_ modules you have installed. Replace _"~/org/node_modules"_ in the configuration below with the location of any local node modules you want to use. Using this approach you don't have to pollute the global node_module directory if you don't want to.

Add the following to your emacs init.el file and evaluate it (or restart emacs). Make sure the $HOME environment variable is set in your environment; or you could just hard code the absolute path to the node_modules directory in the code below.

```
(setenv "NODE_PATH"
  (concat
   (getenv "HOME") "/org/node_modules"  ":"
   (getenv "NODE_PATH")
  )
)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((js . t)))
```

You can choose to install the Babel modules globally, or you can do it locally. In this example I will install them locally in the org directory (~/org/node_modules).

Next install the _babel-cli_ module, this allows you to call Babel from the command line. You will also want to install the transforms you plan to use, the example below installs the common preset transforms used with *Babel 6*. Also install any local modules you need to use. I chose to install them from the ~/org directory where my notes are kept, but anywhere works as long as you have the correct path to *node_modules* set above.


```
npm install --save-dev babel-cli
npm install --save-dev babel-preset-es2015
npm install --save-dev babel-preset-stage-0
npm install --save-dev babel-preset-stage-1
npm install --save-dev babel-preset-stage-2
npm install --save-dev babel-preset-stage-3
npm install --save-dev babel-preset-react
npm install --save-dev mongodb
npm install --save-dev bluebird
```

Next you want to set up a symbolic link to the *babel-cli* script you just installed so it can be found from the command line. I decided to call it _org-babel-node_ so it won't interfere with a _babel-node_ executable linked to a global module of the same name. 

```
ln -s ~/org/node_modules/babel-cli/bin/babel-node.js /usr/local/bin/org-babel-node
```

The default org-mode interpreter for JavaScript is *Node*, so you need to have that installed and its path set. But the cool thing is that you can change the interpreter inline in your code blocks in the cases you want to experiment with upcoming language features. To do this you simply tell _org mode_ to use an alternative interpreter; in this case the __babel-node__ transpiler installed earlier and linked as _org-babel-node_.

Adding  _:cmd "org-babel-node"_   after the  _#+begin_src js_ tells _org mode_ to use the *org-babel-node* transpiler instead of the default JavaScript interpreter. Because _Babel 6_ uses external modules for transforms you need to also tell Babel which preset or plugins you wish to use with either the **--presets** or **--plugins** options. The _:results output_ tells _org mode_ that the results will be from an output statement _(using console.log() for JavaScript)_

 
       #+name: db.activities.findOne
       #+begin_src js :cmd "org-babel-node --presets stage-1" :results output drawer
          (async function(){
              try {
                  let MongoDB = require('mongodb');
                  let Promise = require('bluebird');
                  Promise.promisifyAll(MongoDB);
                  let db = await MongoDB.MongoClient.connectAsync(process.env.MY_DB);
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
 
Now, simply place the cursor anywhere in the block and execute it using C-c C-c. The results will be placed under the block in second block entitled: _#+RESULTS:_

The block can be executed as often as you like and the results will be refreshed. See the updated example with its results block below.
 
       #+name: db.activities.findOne
       #+begin_src js :cmd "org-babel-node --presets stage-1" :results output drawer
          (async function(){
              try {
                  let MongoDB = require('mongodb');
                  let Promise = require('bluebird');
                  Promise.promisifyAll(MongoDB);
                  let db = await MongoDB.MongoClient.connectAsync(process.env.MY_DB);
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