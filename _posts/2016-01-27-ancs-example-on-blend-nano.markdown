---
layout: post
title: "ANCS Example on BLE Nano"
date: 2016-01-27 12:19
comments: true
categories:
redirect_from: /blog/2016/01/27/ancs-example-on-blend-nano
---
<img src="https://s3.amazonaws.com/rwx-blog/nano.png">

I decided to try getting *Apple Notification Center Service (ANCS)* working with the <a href="http://redbearlab.com/blenano/" target="_blank">RedBearLab BLE Nano</a>, and this post describes one way to get the Nordic ANCS demo running on a BLE Nano. This post shows how to get an *ARM* development environment and toolchain up and running on OS X in order to develop apps for the Nordic BLE SoC's (e.g. nRF51822 based boards like the BLE Nano).

There are a few options for developing applications for the BLE Nano:

1. Using the *Nordic nRF5 BLE SDK* along with the  *arm-gcc* compiler. This requires setting up a toolchain on your local development machine (Mac OS X in my case).
2. Using <a href="http://mbed.org" target="_blank">mbed.org</a> and the <a href="https://developer.mbed.org/teams/Bluetooth-Low-Energy/" target="_blank">mbed Bluetooth Low Energy API</a>. This is the fastest way to get started, but unfortunately at the time of this post the API does not yet support peripherals as GATT Clients, and thus does not support ANCS development. 
3. Using the Arduino SDK along with the <a href="https://github.com/RedBearLab/nRF51822-Arduino" target="_blank">nRF51822-Arduino add-on</a>. I am not sure whether this add-on would support peripherals as GATT Clients either, and haven't yet investigated the option.

I decided to start with approach 1 since it seemed like the most stable approach to development. Below I describe my steps to getting the environment set up on OS X. For more on approach 2 & 3 see <a href="http://redbearlab.com/getting-started-nrf51822" target="_blank">Getting Started with nRF51822</a>

## Setting Up the Tool Chain on OS X

Install the *arm-gcc compiler* for OS X so you can compile for ARM devices. Fortunately both *HomeBrew* and *MacPorts* have recipes for installing the compiler. Pick the one that works for you. If you don't have either HomeBrew or MacPorts installed please install one of them before proceeding.

Install the gcc-arm compiler using either *brew* command (HomeBrew) or *port* command (MacPorts):

```
brew install gcc-arm-none-eabi
```

or

```
port install arm-none-eabi-gcc
```

*Note: If you get a permissions error you may need to prepend the sudo command to provide brew/port with enhanced security privileges.*

You will need to save the location of the arm-gcc compiler for updating the nRF5 toolchain config files later. In my case it was located in

```
/usr/local/gcc_arm/gcc-arm-none-eabi-5_2-2015q4/
```

you will also need the compiler version number, just run the command below and write down the resulting version number

```
/usr/local/gcc_arm/gcc-arm-none-eabi-5_2-2015q4/bin/arm-none-eabi-gcc  --version 
```

In my case the */arm-none-eabi-gcc* version was *5.2.1*

## Download the Nordic SDK
The next step is to download the <a href="http://developer.nordicsemi.com/nRF5_SDK/" target="_blank">Nordic nRF5 SDK</a> I chose *nRF51_SDK_v10.x.x*. Unzip into a location that will be your working directory for the project. 

## Download the Nordic Soft Device BLE Protocol Stack
Nordic uses the term *Soft Device* to refer to its BLE protocol stack. I chose to use *S130-SD*, it can be downloaded from the <a href="http://www.nordicsemi.com/eng/Products/Bluetooth-Smart-Bluetooth-low-energy/nRF51822#Downloads" target="_blank">Nordic Download Page</a> under soft devices.

You will need to reference the soft device later, so I suggest saving it in your working directory at the same level you saved the SDK so it is easy to find.



## Updating the SDK configuration
The next step is to modify the SDK configuration to point to your arm-gcc compiler. In your SDK directory edit *components/toolchain/gcc/Makefile.posix* to correct the *GNU_INSTALL_ROOT* and *GNU_VERSION*.  **GNU_INSTALL_ROOT** should be the location of the arm-gcc compiler directory.  **GNU_VERSIO*N* should be the version number of the arm-gcc compiler that I mentioned above. My *Makefile.posix* file looks like this:

```
GNU_INSTALL_ROOT := /usr/local/gcc_arm/gcc-arm-none-eabi-5_2-2015q4/
GNU_VERSION := 5.2.1 
GNU_PREFIX := arm-none-eabi
```

## Compile the ANCS example

The ANCS example is located in the sdk driectory under the **examples** subdirectory. Change to the subdirectory for the ble_app_ancs_c example. For example from the main SDK directory:

```
cd examples/ble_peripheral/ble_app_ancs_c
```

Like all the examples the ble_app_ancs_c directory contains *board package* subdirectories that are set up for the various development boards. For my test I changed to subdirectory:

```
pca10028/s130/armgcc/
```

This is essentially choosing the example created for *board package* **pca10028** and *soft device* **s130** and finally the **armgcc** build directory.

In this directory your will find a Makefile for compiling this example, so run **make** to compile the example.

```
make
```

The compilation process will create a new subdirectory called **_build** that will hold the output of the compile. The key file for our purposes will be the one with a **.hex** extension. In my case is was named *nrf51422_xxac_s130.hex*. This is the hex code that will be loaded by the bootloader on the BLE Nano's nRF51822 SoC. 

Since the nRF51 device is completely flash based. All the executable code, including Nordic’s “Soft Device” protocol stack and your applications, is programmed in this flash memory. The soft device is always in the lower region of the flash, using up to 128 kB, and the rest of the upper region of flash is available for your application. So before your applications hex code can be loaded on the BLE Nano, it must be merged with the hex code for the soft device, in this case the *S130* hex code.

To manipulate hex code you will need the **srecord** tool, which can be installed with HomeBrew or MacPorts. 

```
brew install srecord 
```

or 

```
port install srecord
```

## Merging application Hex Code with Soft Device Hex Code.

Assuming the *S130 Soft Device* code was uncompressed into the same working directory as the sdk and was named *s130_nrf51_1.0.0* and the example application hex code file was named *nrf51422_xxac_s130.hex*. Then from inside the *_build* directory created above we could merge the hex code files with the following command.


```
srec_cat <SDK_DIRECTORY>/s130_nrf51_1.0.0/s130_nrf51_1.0.0_softdevice.hex -intel nrf51422_xxac_s130.hex  -intel -o ancs.hex -intel --line-length=44
```

The above command would create a new (combined) hex code file in _build named **ancs.hex**

## Loading the code on the BLE Nano

<img src="https://s3.amazonaws.com/rwx-blog/nano2.png">

This is the easy part. With the BLE Nano piggy backing on its MK20 USB board and plugged into a USB port, a folder named MBED should appear on your desktop (at least that is what it is named in my case). Just drag the combined hex file we created above *(ancs.hex)* to the MBED folder associated with the Nano device. The bootloader should load the new code, and the USB device may disappear momentarily from the desktop, then reappear.

## Test that the ANCS application was loaded correctly
On an iPhone, open the *Settings* app, and choose *Bluetooth* and make sure Bluetooth is on. Under Devices you should see ANCS appear, and by tapping ANCS you should be able to successfully pair with the device.

## Next Steps
The goal of this process was to get the ARM toolchain and Nordic SDK set up, next steps would be to use the ANCS example as a starting point to develop a custom ANCS app for some device that utilizes the BLE Nano. I hope to post some examples in the future as I work with the Nano more.