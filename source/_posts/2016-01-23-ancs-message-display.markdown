---
layout: post
title: "ANCS Message Display"
date: 2016-01-23 11:12
comments: true
categories: 
---

## Overview
Ever want to see that last iPhone message without checking your phone. It is actually fairly easy to create a secondary message display using an Arduino, BLE, and an LCD display to conect to the *Apple Notification Center Service* on your iPhone.
<img src="https://s3.amazonaws.com/rwx-blog/IMG_6097.JPG">

For this project I used the <a href="http://redbearlab.com/blendmicro/" target="_blank">Blend Micro</a> from  RedBearLab, combined with an <a href="https://www.adafruit.com/product/358" target="_blank">AdaFruit ST7735R TFT LCD display</a>  The *Blend Micro* combines an Atmel ATmega32U4 micro-controller with a Nordic nRF8001 BLE chip. Simply hook up the LCD using SPI and you are in business. For this project I added a <a href="https://www.adafruit.com/products/160">piezo buzzer</a> for sound effects and a button to wake up the display if it has timed out.

<img src="//s3.amazonaws.com/rwx-blog/IMG_6098.JPG">

The basic idea is to have the iPhone pass along alerts to the device using BLE/ANCS and to have the device play a tone and display the alert information. There is a timeout to power down the backlight on the display after a minute, and a button that can be pressed to turn the display's backlight on, so the last message can be viewed after the one minute timeout.  This power savings mode could allow the device to be powered by a battery.

I created a demo project on <a herf="https://codebender.cc/sketch:222511" target="_blank">codebender</a> to make it easy to replicate. You will need to import a few libraries into your personal libraries on codebender to get the project to work. It would be easy to enhance the project to save the last several messages and use a <a href="https://www.adafruit.com/product/444">2-Axis Analog Thumb Joystick</a> to control a simple interface that scans through messages.

Unfortunately the *Blend Micro* does not have an on-board LIPO charging circuit, so if you want to enable a combined USB/Battery solution a charging circuit would have to be added. RedBear warns that connecting a battery to VIN and USB simultaneously could damage the board.

I printed up a simple enclosure on the 3D printer and here is the enclosed LCD panel.

<img src="https://s3.amazonaws.com/rwx-blog/IMG_6111.JPG">

## Pinouts
```
  VIN & GND -> to LIPO battery (DO NOT use USB power when battery connected)
  PIN 2     -> ST7735R LITE
  PIN 8     -> ST7735R D/C
  PIN 9     -> ST7735R Reset
  PIN 10    -> ST7735R TFT_CS
  PIN 11    -> ST7735R MOSI
  PIN 13    -> ST7735R SCK
  PIN V33   -> ST7735R VCC
  PIN GND   -> ST7735R GND

  Button -> PIN 5, GND
  Buzzer -> PIN 3, GND

```
  
## Detailed Instructions

Follow the instructions for using <a href="http://redbearlab.com/quick-start-codebender" target="_blank">Blend Micro on codebender</a>. You should be able to get the LED Blink example working before continuing.

### Add key libraries
To compile the code in the project above you will need to add several libraries to your personal libraries on codebender. Go to  <a href="https://codebender.cc" target="_blank">codebender.cc</a> and you will see the **Upload Libraries* button on the upper right side of the page. There are four libraries you need to add.

* <a href="https://github.com/NordicSemiconductor/ble-sdk-arduino" target="_blank">Nordic Bluetooth low energy SDK for Arduino beta version 0.9.0</a>
* <a href="https://github.com/RedBearLab/nRF8001/" target="_blank">RedBearLab nRF8001 Library version 20140701</a>
* <a href="https://github.com/RedBearLab/nRF8001/" target="_blank">RedBearLab Blend Add-On version 20140701</a>
* <a href="https://github.com/robotastic/ANCS-Library" target="_blank">Robotastic/ANCS-Library</a>

Just download each of these as a zip file from github, and upload them to your *codebender personal library*. I created a fork of the *ANCS-Library* to thin it down a bit as memory was tight on the *Blend Micro* for another version of the project I am working on. It is on a branch called **code-diet** available on github  <a href="//github.com/fooqri/ANCS-Library/archive/code-diet.zip">ANCS-Library on a code-diet zip</a>

Finally, clone my <a herf="https://codebender.cc/sketch:222511" target="_blank">codebender ANCS_Display_ST7735 project</a> and verify the code compiles with the libraries you uploaded, and run the project on Arduino.

Open the iPhone  *Settings* app and select *Bluetooth*. If everything is working correctly you should see **ANCS_RUSK** listed under *MyDevices*. Select it and choose pair.
<img src="https://s3.amazonaws.com/rwx-blog/IMG_6095.PNG">
<img src="https://s3.amazonaws.com/rwx-blog/IMG_6094.PNG">

Once paired you should hear a tone on the device, and the display will change from **Status: Not Connected** to **Status: Connected**.  If you receive any alerts on your iPhone you should now hear a tone on the device and the screen should display a message.

You can update the code to support custom tones and messages for different alert types, or add other interesting features. 


## Additional Notes
* The <a href="http://redbearlab.com/blenano/">Blend Nano</a> from ReadBearLab is a tiny alternative to the Blend Micro but it is based on the ARM Cortex-M0 SoC and uses the newer Nordic nRF51822 BLE chipset. The *ANCS-Library* is only compatible with the Nordic nRF8001 BLE chipset, so some work would be needed to port the library to the new platform.
* Adafruit has just announced a few similar Arduino+BLE boards. The <a href="https://www.adafruit.com/products/2829">Feather 32u4 Bluefruit LE</a> using the ATmega32u4, and the <a href="https://www.adafruit.com/products/2995">Feather M0 Bluefruit LE</a> using the ATSAMD21G18 ARM Cortex. Both these boards provide a built in 100mA lipoly charger, so either would be a better choice for a mobile device. Both these boards use the  nRF51822 BLE chipset so like the Blend Nano would require porting the *ANCS-Library* before the code above could be used.
* I have a <a href="https://www.adafruit.com/products/1393">SHARP Memory Display Breakout</a> from adafruit, which is a really nice eInk type display, but was unable to get it working with this demo on first try. This <a href="https://codebender.cc/sketch:220214">codebender sketch</a> was my first attempt. It seems that there is a conflict between the *Adafruit_SharpMem* library and the *ANCS Library*, because instantiating the Adafruit_SharpMem display object causes calls to notif.setup() to hang. I may look at it a bit more if I get a chance, but this was to be a quick experiment. There were some memory size issues initially, but I believe the hang may be an SPI issue, but I haven't yet had time to investigate further.
* I also started to play with a headless version that instead uses neoPixels. I will post when I finish it. I like the idea of a fun neoPixel and sound only display connected with an iOS app that allows the user to customize what notifications the display responds to and how it responds. This would allow cheap simple peripheral displays to be created that respond to different notifications in different ways.
* The <a href="http://makezine.com/2015/12/09/meet-esp32-new-big-brother-to-iot-board-esp8266/">ESP32</a> should make for an interesting platform for these types of displays because they could allow BLE for notifications, and use WiFi for connection to the home network. This could allow control a wide range of WiFi enabled home devices based on iOS app notifications. That sounds fun.  