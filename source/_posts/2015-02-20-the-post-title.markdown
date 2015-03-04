---
layout: post
title: "Zetta Experiments"
date: 2015-02-20 15:22
comments: true
categories: 
---

## I spant the day experimenting with [Zetta](http://www.zettajs.org/), an open-source Internet of Things Platform built on Node.js. I added it to one of the Edison boards I had, and wanted to experiment with integrating a few devices. Nothing to interesting yet but wanted to record the basics of getting it working.

I decided to use a few devices I had around. In this case they were:

* The [Intel Edison](http://www.intel.com/content/www/us/en/do-it-yourself/edison.html)
* The [LightBlue Bean](https://punchthrough.com/bean/)
* The [Philips Hue](http://www2.meethue.com/en-us/)

### Step 1: Create a node project on the Edison
     mkdir zetta-experiments
     cd zetta-experiments
     npm init

### Step 2: Install Zetta and supporting libraries

     npm install zetta --save
     npm install zetta-led-edison-driver --save
     npm install zetta-bean-driver --save
     npm install zetta-hue-driver --save
     npm install color --save

## The [zettajs](www.zettajs.org) has some nice getting started documents so I will just make a few notes here.

### Step 3: Create a server.js file
     
     var zetta = require('zetta');
     var led = require('zetta-led-edison-driver');
     var bean = require('zetta-bean-driver');
     var Hue = require('zetta-hue-driver');
     var Color = require('color');

     var beanApp = require('./apps/bean');
     var ledApp = require('./apps/led');
     var hueApp = require('./apps/hue');


     zetta()
       .name('Fooqri-Jones')
       .use(bean, "Bean")
       .use(led, 13)
       .use(Hue)
       .use(beanApp)
       .use(ledApp)
       .use(hueApp)
       .link('http://rwx-zetta.herokuapp.com/')
       .listen(1337, function(){
          console.log('Zetta is running at http://127.0.0.1:1337');
       });  

### Step 4: Create the individual modules for interacting with the Edison LED, Hue, and Bean.

      mkdir apps
      cd apps
      touch led.js
      touch hue.js
      touch bean.js

### Step 5: 