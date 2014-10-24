---
layout: post
title: "Photo Caption Challenge - using Facebook Login, S3, and DynamoDb in browser app"
date: 2014-10-23 13:18
comments: true
categories: 
---

One of the challenges of building social web apps without a traditional back-end server is storing global state in a secure way. In my exploration of ways to store state I decided to build a very simple multi-player social app that allows players to participate in a simple photo challenge game. The game author specifies a _photo caption_ and then invites friends to add photo responses that _most creatively_ match the caption. The second feature is to allow people to vote on their favorite photo responses.

See a live example below. Please keep it clean as I have allowed any Facebook user to participate in the demo.  I don't want to be forced to shut down upload for the demo app because of inappropriate photos. I think it is handy that visitors can try it out.

<div class="over">
    <iframe  src="http://fooqri.poggr.com/peJE7qM0YUl::1"  seamless="seamless"></iframe>
</div>

Such a game would typically require a server to support a few key behaviors:

* __player login__: is needed to connect players with their uploaded photos, and also to limit their votes so as to keep voting fair.
* __photo storage__: photo upload and storage is needed to store the photos so they can be displayed when the page is loaded.
* __global state__: is generally provided by a database that stores information such as: which players have uploaded photos, and where the corresponding photos are located.

There are many challenges to running a back-end server to support an app, including configuration, maintenance, and security. In the ideal case one could build all sorts of small fun apps without having to manage any such servers. With the __Photo Caption Challenge__ app I explore using the following services instead of running an app server.

* __player login__: I will use Facebook for player login as a way to differentiate players, and connect ids to votes and photos.
* __photo storage__: I will use Amazon S3 for storing photos uploaded buy players.
* __global state__: I will use Amazon DynamoDB to provide a simple table that stores information about photo entries and votes.

I will also use the Amazon IAM service to glue everything together from a privileges standpoint. Don't worry about the details yet, This is a simple overview. I will point to the _[README](http://www.poggr.com/peJE7qM0YUl:dxkgN7qMCtLg)_ document for the app that explains more in details, and also the [configuration tool](http://www.poggr.com/peJE7qM0YUl:dl1SEX9f0K8e) that provides help for how to set up these services. __Note:__ These instructions are poggr specific but any changes for a non-pogg app should be minor.

## Facebook Login

This is fairly straight forward, you visit the [Facebook Developers Page](https://developers.facebook.com/) and create a Facebook Web App. With the signup you get a small bit of JavaScript that can be used to integrate Facebook Login with your page. The main goal is to get a unique ID for each user that can be used in the DynamoDB database.

## Amazon S3 Photo Storage
One of the key issues is allowing photos to be uploaded from the browser directly to S3 but only for JavaScript run in your domain, and only by users who have logged in via Facebook. It turns out that Amazon IAM works very well for creating such restrictions. You can configure a IAM policy that integrates with Facebook Login and controls access to S3 permissions like photo upload, delete, etc.

## Amazon DynamoDB
Another key issue is storing data about who has uploaded each photo, and which photos each user has up-voted. The last requirement is a design constraint as I wanted to balance each persons voting power. In essence a user can vote for several photos, but each vote is simply dividing the users vote across the up-voted photos. This decision allows a user to change their votes at any time as the game winds down, hopefully converging towards a winner.

Again Amazon IAM helps here, as it can be used to secure individual rows in a DynamoDB table so that they are secured by the user associated with that row. Thus a different user can't open up the JavaScript console and cancel another players vote, the table cells are protected by player login at Amazon, not in the browser. For more information see [Fine-Grained Access Control for DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/FGAC_DDB.html).

So essentially the player of the _Photo Caption Challenge_ is given limited permission based on their id provided by their Facebook login. They are allowed to create rows in the games DynamoDB table. These rows can be of two types __vote__ or __upload__ and each row contains:

* __userId__: the user's id returned as part of the Facebook login
* __submissionId__: a unique transaction id for the upload or vote
* __creationDate__: a timestamp for the transaction
* __gameId__: It is possible to run multiple games simultaneously with different captions, so a gameId is needed for each game.
* __submissionType__: signifies the type of record (vote or upload)
* __filename__: the name of the file in the games  Amazon S3 bucket. Technically every user gets a unique folder that holds their uploaded photos in the bucket. This allows an IAM policy to secure each folder using Facebook login info.
* __voteId__: in the case of a vote there is also a voteId to uniquely identify each vote.

In addition to the table structure, there is a separate index for the table that allows queries by gameId and  submissionType. This allows for quick lookup of all photos or all votes for a particular game.

In [Mobile Real Estate App](http://octopress.dev/blog/2014/10/22/mobile-real-estate-app-version-1/) and [Spreadsheet Driven Web Apps](http://octopress.dev/blog/2014/10/15/spreadsheet-driven-web-apps/) I  described a technique for using a Google Spreadsheet to provide web application data, but this works best when the application data is read only. For an app that requires both read, and query transactions, a database like DynamoDB is a great solution.

Like many examples on this blog, I built this app using _[poggr.com](http://www.poggr.com)_ because poggs are incredibly flexible and require zero configuration.  If you have a poggr account you can clone [this pogg](http://www.poggr.com/#/projects/project/peJE7qM0YUl), check out its [README](http://fooqri.poggr.com/peJE7qM0YUl:dxkgN7qMCtLg), and use the customized service [configurator tool](http://fooqri.poggr.com/peJE7qM0YUl:dl1SEX9f0K8e) to set up Facebook, S3, IAM, and DynamoDB and have your version of the game running in less than 5 minutes.




