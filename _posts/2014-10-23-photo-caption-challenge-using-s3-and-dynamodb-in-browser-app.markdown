---
layout: post
title: "Photo Caption Challenge - using Facebook Login, S3, and DynamoDb in browser app"
date: 2014-10-23 13:18
comments: true
categories:
redirect_from: /blog/2014/10/23/photo-caption-challenge-using-s3-and-dynamodb-in-browser-app
---

One of the challenges of building small mobile web apps without a traditional back-end server is storing global state in a secure way. In my exploration of ways to store state I decided to build a very simple multi-player social app that allows players to participate in a simple photo challenge game. The game author specifies a _photo caption_ and then invites friends to add photo responses that _most creatively_ match the caption. The second feature is to allow people to vote on their favorite photo responses.


<a href="//fooqri.poggr.com/peJE7qM0YUl" target="_blank"><img src="//s3.amazonaws.com/fooqri-poggs/peJE7qM0YUl/static/images/peJE7qM0YUl_screen.png"  style="height: 400px; display: block; margin: auto;"></a>

Such a game would typically require a server to support a few key behaviors:

* __player login__: is needed to connect players with their uploaded photos, and also to limit their votes so as to keep voting fair.
* __photo storage__: photo upload and storage is needed to store the photos so they can be displayed when the page is loaded. In addition a back-end service is typically used to re-size uploaded images before storing them to reduce storage costs.
* __global state__: is generally provided by a database that stores information such as: which players have uploaded photos, and where the corresponding photos are located.

There are many challenges to running a back-end server to support an app, including configuration, maintenance, and security. In the ideal case one could build all sorts of small fun apps without having to manage any such servers. With the __Photo Caption Challenge__ app I explored using the following services instead of running an app server.

* __player login__: I  used Facebook for player login as a way to differentiate players, and connect ids to votes and photos.
* __photo storage__: I used Amazon S3 for storing photos uploaded by players, and  used _canvas_ and _canvas.toBlob()_ (using [JavaScript Canvas to Blob](https://github.com/blueimp/javascript-canvas-to-blob) polyfill) to re-size images and store them in a blob for upload to S3. Thus all image re-sizing is done in the client.
* __global state__: I used Amazon DynamoDB to provide state via a table that stores information about photo entries and votes.

I  also used the Amazon IAM is the way to limit privileges from the client app to the data services (S3 and DynamoDB). For example you want the user to have write/delete access to only their information in the data services, but client API calls to the server can be manipulated, thus authentication information is critical to limiting privileges in accessing the data services.

IAM policies can specify an _identity provider_ like Facebook to make sure to limit access based on current session identity information, and not the API request data. For example you can configure an IAM policy for S3 that secures S3 bucket privileges so that sub-folder privileges are connected to user identity. In the case of "Photo Challenge" the policy states any logged in Facebook user running the Photo Challenges app will be able to view photos in any sub-folder, but only upload, modify, or delete items that are in a folder that matches their identity provider's assigned userid. It also states that any user can create a folder in the bucket as long as the folder name matches their identity provider's assigned userid. 

The Amazon IAM policy for DynamoDB works similarly. Any logged in Facebook user running the Photo Challenges app will be able to query the DB index for the current list of photo entries, but can only add/delete records that have a userId value that matches their identity provider's assigned userid. Thus a user can't spoof who added the record, it is connected to their userId or it is rejected by the IAM policy assigned to the DynamoDB table. For more information see [Fine-Grained Access Control for DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/FGAC_DDB.html).

## Conclusion
In [Mobile Real Estate App](http://octopress.dev/blog/2014/10/22/mobile-real-estate-app-version-1/) and [Spreadsheet Driven Web Apps](http://octopress.dev/blog/2014/10/15/spreadsheet-driven-web-apps/) I  described a technique for using a Google Spreadsheet to provide web application data, but this works best when the application data is read only. For an app that requires both read, write, and query transactions, a database like DynamoDB is a great solution.

Like many examples on this blog, I built this app using _[poggr.com](http://www.poggr.com)_ because poggs are incredibly flexible and require zero configuration.  Use this app at [fooqri.po.gg/peJE7qM0YUl](http://fooqri.poggr.com/peJE7qM0YUl:dxJ4NmcMAK8x) or if you have a poggr account you can clone [this pogg](http://www.poggr.com/#/projects/project/peJE7qM0YUl) and use its configuration tool to set up Facebook, S3, IAM, and DynamoDB and have your version of the game running in less than 5 minutes. If you don't have an account you can still check out the pogg's [README](http://fooqri.poggr.com/peJE7qM0YUl:dxkgN7qMCtLg) to learn more about how it was build and view the source documents.




