---
layout: post
title: "Spreadsheet Driven Web Apps"
date: 2014-10-15 14:45
comments: true
categories: poggr google-docs polymer
redirect_from: /blog/poggr/google-docs/polymer/2014/10/15/spreadsheet-driven-web-apps
---

<a href="//fooqri.poggr.com/pgyUYTfcMUe:dgyFhkQ9M8e"><img src="//s3.amazonaws.com/goddip-poggs/pgyUYTfcMUe/example_screen.png"></a>

Using Google spreadsheets is a great way for a team to collaborate on a data set but it leaves a bit to be desired on presentation of the data. To that end I will be creating a series of fun examples showing how to build small interactive apps that utilize _Google Docs_ and _Polymer_ web components to quickly bring data to life. In this series I will be using a Google spreadsheet as the data source, but other data sources are possible, and I will get to those as well in future posts.

The first example is  ___[Hipster List](http://fooqri.poggr.com/pgyUYTfcMUe:dgyFhkQ9M8e)___, an app that shows cool places to visit in various cities. Check out the ___[README](//fooqri.poggr.com/pgyUYTfcMUe:dxJgUYaGcGUl)___ document for details on how this app is put together.

<a href="//docs.google.com/spreadsheet/ccc?key=0Ahy9ODkMXc1GdHRaTlI3Y2EydllTa2NsRjlxRVhMRlE&usp=sharing#gid=0"><img class="spreadsheet-screen" src="//s3.amazonaws.com/goddip-poggs/pgyUYTfcMUe/spreadsheet_screen.png"></a> 

A little convention is used to make it work. Namely, I use a [Hipster Hot Spots](https://docs.google.com/spreadsheet/ccc?key=0Ahy9ODkMXc1GdHRaTlI3Y2EydllTa2NsRjlxRVhMRlE&usp=sharing) Google spreadsheet, where each city's data is represented by a tab in the spreadsheet. There is also a _key_ tab that provides a list of all the cities in the spreadsheet and the tab id (_gid_) for each city's data. The app will load its data from the spreadsheet and populate the city drop-down list of _hot spots_, and display a map with markers for each _hot spot_. This was a fun first example, remember to checkout the [readme document](//fooqri.poggr.com/pgyUYTfcMUe:dxJgUYaGcGUl) for code and explanation.

__Note__: I enabled url fragment parameters so you can easily point the app at your own copy of the spreadsheet for testing. See the [readme document](//fooqri.poggr.com/pgyUYTfcMUe:dxJgUYaGcGUl) for the how-to instructions. Feel free to copy the spreadsheet and try out the app with your own list of cities and _hot spots_. 

 Separating code and data is always beneficial, but there is something cool about connecting an app to a Google spreadsheet. There are many spreadsheet users who would like to have an app to visualize their data, but may not be up to the coding challenge yet. I think many small useful apps could be built this way;  I will pick a few to build in the next few weeks and discuss them here. I am using the _[poggr.com](//www.poggr.com/home)_ service for the example, which is a service I built just for these types of small quick apps that can rely on an external data service. It is basically working to merge interactive content creation and blogging into a single service.

 Leave me a comment if you have an small spreadsheet driven app you would like me to build. If it seems reasonable I may add it to the list.







