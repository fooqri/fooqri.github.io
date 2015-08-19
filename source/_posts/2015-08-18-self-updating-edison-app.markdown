---
layout: post
title: "Self Updating Edison Apps"
date: 2015-08-18 10:49
comments: true
categories: 
---
One of the challenges I have had in handing out prototype devices is keeping the software up to date. Solutions like <a href-"www.resin.io" target="_blank">resin.io</a> do a nice job of deploying <a href="http://bundler.io/" target="_blank">bundler images</a> onto devices like the Edison. The primary issue I had was the overhead of pushing bundler images around when the only thing that was changing was the node app. It seemed easier to just use git and npm to handle the updates. I may go the resin.io route later, but this early in dev and testing the git route seems simpler.

## Overview of What I Did
The product I am prototyping has two parts, an Edison device (with additional sensors and actuators) running a node app, and a node web service for managing device configuration and data running in the cloud.

1. The device's node app is published in a private github repository.
2. I installed and configured git on each of the Edison devices.
3. I cloned the github repository onto each of the Edison devices.
4. I installed the forever module on each of the devices to keep the app up and allow easy restarting of the app.
5. I created a startup script that starts the app using forever.
6. I created and enabled a linux service that runs the startup script on boot.
7. I added code to the app to periodically ask the web service what the latest version of the app should be.
8. If a new version is available the app will do a pull and use forever to do a restart using the new version.

## The Details

### Initial Cleanup

* Remove any app from the default Edison node_app_slot directory so you don't accidentally start the app using the default Edison process.

```
mv /node_app_slot /node_app_slotbk
mv  ~/.node_app_slot/ ~/.node_app_slotbk
```

### Install Git
#### Update /etc/opkg/base-feeds.conf with these 3 lines
```
src all     http://iotdk.intel.com/repos/1.1/iotdk/all
src x86 http://iotdk.intel.com/repos/1.1/iotdk/x86
src i586    http://iotdk.intel.com/repos/1.1/iotdk/i586
```
#### Update opkg and install git
```
opkg update
opkg install git
```

### Option 1: Modify Edison's default port
I wanted to use port 80 for the node app so I moved the default Edison config service to port 8080

#### Change default port in edison-cofig-server

Edit _/usr/lib/edison_config_tools/edison-config-server.js_
and change the last line to use a port other than 80.

```
http.createServer(requestHandler).listen(8080);
```

#### Option 2: Disable the Edison config web service

```
systemctl disable edison_config
systemctl stop    edison_config
```

### Setup to use github

#### Generate a key for use with github
* ssh-keygen -t rsa -b 4096 -C "me@my.email"

Follow the directions, easiest is just to hit return at the prompts. I chose to not do a passphrase for my small pilot.

#### Generate a deployment key for the github repository
* Go to your app's github repository, choose _settings_, choose _deployment keys_
* Click the _Add Deployment Key_ button
* Give it a title (the host name for the device works)
* Back on the Edison run cat /home/root/.ssh/id_rsa.pub to get the text for the public key
* copy the text for the public key to the _Key_ input box back on github.

### Clone your repo
Back on the Edison

```
cd /
git clone <your repo> AppDirName
cd /AppDirName
```

### Pull Latest code
Now any time you update code on master a simple _git pull_ will update the latest code.

```
git pull
```

### Install forever module using npm
Forever will automatically restart a node app if it crashes. It also has some handy restart features.

```
npm install -g forever
```

### Create a startup script & service
Creating a startup service will allow your app to start automatically using forever.

#### Create startup.sh to start node app (server.js in this case)
```
#!/bin/sh
cd /AppDirName 
forever start server.js
```

#### Make startup.sh executable

```
chmod -x startup.sh
```

#### Create a startup service file at /lib/systemd/system/startup.service

```
[Unit]
 Description=STARTUP
 [Service]                           
 Type=idle                           
 RemainAfterExit=true
 ExecStart=/AppDirName/startup.sh
 Environment="HOME=/home/root"    
 WorkingDirectory=/AppDirName/   
 [Install]                     
 WantedBy=multi-user.target 
```

#### Enable startup service

```
systemctl enable /lib/systemd/system/startup.service
```

### Enable your node app to update itself

By using a simple update function you can get your app to update itself and restart.

```
var spawn = require('child_process').exec;
var semver = require('semver');
var bunyan = require('bunyan');
var log = bunyan.createLogger({
    name: 'pocketwatch',
    streams: [{
        type: 'rotating-file',
        path: '/var/log/pocketwatch.log',
        period: '1d',
        count: 7        
    }]
});
var pjson = require('./package.json');

var checkVersion = function(){
  var currentVersion = pjson.version;
  var options = {  hostname: 'www.myhost.com',
                             port: 80,
                   path: 'http://www.myhost.com/device_version/',
                   method: 'GET',
                   headers: {'Content-Type': 'application/json'}
                };
  var callback = function(response) {
    var dataStr = '';
    response.on('data', function (chunk) {
      dataStr += chunk;
    });

    response.on('end', function () {
      var versionInfo = JSON.parse(dataStr);
      var latestVersion = versionInfo.client_version || "0.0.0"; //don't update if missing version info
      log.info("current version: ", currentVersion);
      log.info("latest version: ", latestVersion);
      if (semver.gt(latestVersion, currentVersion)){
        log.info("pulling newer versions");
        spawn('git pull', function(error, stdout, stderr) {
          if (error){
            log.error("ERROR pulling latest: ", error);
          }
          else{
            log.info("updating packages");
            spawn('npm update', function(error, stdout, stderr){
              if (error){
                log.error("ERROR updating packages: ", error);
              }
              else {
                log.info("restarting node");
                spawn('forever restartall', function(error, stdout, stderr){
                  if (error){
                    log.error("ERROR restarting: ", error);
                  }
                  else {
                     log.info("restarted");
                  }
                });
              }           
            });
          }
        }); 
      }
    });
  };

//check for updates at app startup
checkVersion();

//then check for updates every hour;
setInterval(function() {
    checkVersion();                                                       
  }, 3600000);
  
```

### On the server
You will need to add a route on your server to provide the version info. In this example the route was a GET request to the  _/device_version_ route. For simplicity I just use an env_var on the service. I simply update the env_var when a new version is available. Then in the logic for the _/device_version_ route I pass back the version found in the env_var.

The logic for comparing versions is very basic and flawed, but will work in this simple case.

### Improvements
Ideally instead of a straight _git pull_ you can instead download a tagged version, and keep the current and next version info for each device in the web service db. This would allow rolling out upgrades to specific devices, etc. Another approach would be to pass back version info to the device so updates could roll out immediately if the device is in use. Finally more logic on the device to schedule an update when not active would be ideal. In that case maybe adding more than _versionNumber_ of the latest version to the server response, maybe a priority value also.

This was a quick experiment it getting updates to percolate out to devices prototype devices, and so far it seems to be working well.


