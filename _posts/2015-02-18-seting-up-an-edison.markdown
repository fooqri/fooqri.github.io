---
layout: post
title: "Setting Up a New Intel Edison"
date: 2015-02-18 12:42
comments: true
categories: edison iot 
---
<img src="//s3.amazonaws.com/rwx-blog/IMG_4161.JPG"  style="height: 400px; display: block; margin: auto;">

The Edison is a tiny and amazing computer, and ideal prototyping tool for wearable and IoT experiments. Here are the steps I am currently following to set up the Edison.

## Flashing the Edison
Like many developers I have Mac, Windows, and Linux laptops but I find that Linux is the best environment for flashing the Edison, even though I do most development on my Mac. I came to this conclusion after trying to recover an Edison with a lost password, the only platform that worked was Linux.

The first step is flashing the Edison. Follow [Flashing Edison Linux](https://communities.intel.com/docs/DOC-23200). You can also try [Flashing Edison Mac](https://communities.intel.com/docs/DOC-23193).

The only change I would recommend is to create a folder that contains the Edison images, and then unzip the downloaded folder into a sub directory named after the build number. Over time you may find yourself flashing to older or newer images based on the project needs.

## Setting up WiFi
Sparkfun offers a great guide for [Setting up WiFi](https://learn.sparkfun.com/tutorials/edison-getting-started-guide#connecting-to-WiFi) on the Edison. This takes only a few minutes and even if you don't plan to use WiFi in your projects it makes working with the Edison easier because you can use SCP and SSH to connect with the Edison over the network.

## Connect to Edison
For OSX or Linux the best way to connect to the Edison is via SSH. On OSX you can use the name you gave the Edison in the step above. For example *ssh root@edison2.local* where *edison2* is the name you gave your Edison. On Linux you will use the Edison's IP address, for example *ssh root@10.0.1.12*.

## Using Emacs
If you are an Emacs user then once WiFi is setup you can use [Emacs Tramp](http://www.emacswiki.org/emacs/TrampMode) to work with files on the Edison. Just use *C-x C-f* as usual, but instead of a directory use *root@edison2.local* or use the ip address for Linux.

Emacs will present a directory of files on the Edison that you can open, or just keep typing the name for auto suggest feature. For example *root@edison2.local/home/root/notes.md*.

## Setup Bluetooth
Bluetooth is available in the Edison, but in the default configuration is not enabled at boot. If you are using Bluetooth you will likely want to enable it on every reboot or power cycle.

### Enable Bluetooth at Boot
Use the **systemctl** command to cause Bluetooth to start automatically

     systemctl enable bluetooth

### Create a BT startup script
Create a script file with the following five lines (*/home/root/btup.sh*).

     #!/bin/sh
     /usr/sbin/rfkill unblock bluetooth
     /usr/bin/hciconfig hci0 up
     /usr/bin/hciconfig hci0 piscan
     /usr/bin/hciconfig hic0 sspmode 0

### Make the script executable

     chmod +x /home/root/btup.sh

### Create a new service file (*/lib/systemd/system/btup.service*).

     [Unit]
     Description=BTUP
     After=bluetooth.target
     Before=systemd-user-sessions.service
     [Service]
     Type=simple
     RemainAfterExit=true
     ExecStart=/home/root/btup.sh
     Environment="HOME=/home/root"
     WorkingDirectory=/home/root/
     [Install]
     WantedBy=multi-user.target
     
### Enable the service

     systemctl enable /lib/systemd/system/btup.service

### Reboot the Edison

     reboot

## Create a Backup
Now is a good time to create a backup of the Edison that can be recovered if you need to return to a clean install. For example you may want to update nodejs, or install node modules, or even other drivers that may cause an issue you want to start over from. 


Place a MicroSD card with at least 4GB of available space into the MicroSD slot on the dev kit board where the Edison is installed. Backup the Edison to an image file on the MicroSD. In the example below it is named *edison2_backup.img*. Make sure the file name has a *.img* extension. If you have a large MicroSD card you can store multiple backup images from multiple Edisons, making it quick and easy to recover each of them. It is wise to consider a consistent naming system.

     dd if=/dev/mmcblk0 of=/media/sdcard/edison2_bk.img

## Restoring an Edison from Backup
 If you need to restore the Edison from backup just reverse the process

     dd if=/media/sdcard/edison2_bk.img of=/dev/mmcblk0
