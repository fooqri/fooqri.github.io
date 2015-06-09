---
layout: post
title: "Revisiting Buyer's Agent app using React.js"
date: 2015-06-09 11:45
comments: true
categories: 
---

In a past post I showed a [Mobile Real Estate App](http://rwx.io/blog/2014/10/22/mobile-real-estate-app-version-1/) that was built with Polymer. This time around I will revisit the app but instead use <a href="https://facebook.github.io/react/" target="_blank">react.js</a>. The __Mobile Buyer's Agent__ is a simple web based application used to demonstrate a basic React.js mobile web app.The goal is to allows a real estate buyer's agent to deliver a personalized mobile app experience to their clients by adding data to a Google spreadsheet. The agent updates a Google spreadsheet, and the web app loads its data from the spreadsheet.

<a href="http://www.poggr.com/p-kz3NoHhgl:dZkIM34sBnlx?sheetid=1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m9" target="_blank"><img src="https://s3.amazonaws.com/fooqri-poggs/p-kz3NoHhgl/buyers_agent_1.png"></a>

This is a demonstration of using a shared _Google Spreadsheet_  as the data source for a simple web based application. By using poggr.com and <a href="http://facebook.github.io/react/" target="_blank">React.js</a> it is extremely easy to create a web application like the ___<a href="http://www.poggr.com/p-kz3NoHhgl:dZkIM34sBnlx?sheetid=1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m9" target="_blank">Mobile Buyer's Agent</a>___. 

The _Real Estate Shopper List_ Google spreadsheet contains properties the agent wishes to present in the app. The neighborhood column is associated with the dropdown box, and allows a simple grouping/categorization of properties. The agent also provides other features and details associated with the properties.

<a href="//docs.google.com/spreadsheets/d/1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m8/pubhtml" target="_blank"><img class="spreadsheet-screen" src="//s3.amazonaws.com/fooqri-poggs/p-kz3NoHhgl/buyers_agent2.png" ></a>

__Note:__ if you duplicate the example spreadsheet you must remember to publish it so it can be accessed by the _Mobile Buyer's Agent_ app. If you get an error it is likely you forgotto publish the spreadsheet. To publish a spreadsheet while viewing it, use the file menu on Google Docs and choose _"publish to the web"_, and follow the instructions.

### Trying your own spreadsheet

If you publish your own copy of the spreadsheet you can easily substitute it in the app with a simple url parameter called __sheetid__.

For example if the link your are given when you plublish your spreadsheet is 

```
https://docs.google.com/spreadsheets/d/1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m8/pubhtml
```

Then your sheetid is __1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m8__, and you can use it in this app by using a url with sheetid parameter as shown below:


<code style="white-space: nowrap;">po.gg/p-kz3NoHhgl:dZkIM34sBnlx?sheetid=1kv5haqhS8bUY_6IoJ6KBY5j42pN2WsY_wscDZSHb_m8</code>


This will substitue your spreadsheet for the default spreadsheet used in the app.

For info on the code take a look at the <a href="http://www.poggr.com/p-kz3NoHhgl:dbJMG3EjSneg" target="_blank">README</a> document.