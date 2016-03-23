---
layout: post
title: "Edison Wi-Fi Configuration"
date: 2015-08-16 13:55
comments: true
categories:
redirect_from: /blog/2015/08/16/edison-wifi-config
---

<img src="//s3.amazonaws.com/rwx-blog/IMG_4161.JPG"  style="height: 400px; display: block; margin: auto;">

I built a handful of prototype devices using Intel Edison boards to hand out to testers, but one challenge is each tester will bring the devices to their own Wi-Fi environment (home, work, etc). The default method for configuring an Edison is to use a console and the command line configuration tool to add a Wi-Fi access point.

```
configure_edison --wifi
```

The _configure_edison_ app will scan for Wi-Fi networks and provide a list of networks for the user to pick from, and then prompt the user for the access point password. Since my headless IoT device has no traditional interface, let alone terminal interface this posed a problem. I needed a way for users to configure the device for new Wi-Fi networks as they were encountered, and make it accessible using a web page presented by the Edison. I will post the code once I have it completed and tested with users but for a quick hint the trick is to allow the running node.js app to switch the device between access point mode and client mode so if no network is available the device becomes an access point allowing the user to use any Wi-Fi enabled device to connect with it. Once connected the user can use a standard web browser to update the configuration to include the new Wi-Fi network they are intending to use.


### wpa_supplicant

The Edison uses the wpa_supplicant service to manage the client-mode Wi-Fi. The wpa_supplicant configuration file is located at: __/etc/wpa_supplicant/wpa_supplicant.conf__

Wi-Fi networks are added and removed by updating this configuration file. Se an example configuration below.

```
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
config_methods=virtual_push_button virtual_display push_button keypad
update_config=1
fast_reauth=1
device_name=Edison
manufacturer=Intel
model_name=Edison

network={
  ssid="guest"
  key_mgmt=WPA-PSK
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  eap=TTLS PEAP TLS
  psk="guest_pw"
  id_str="guest"
  priority=4
}

network={
  ssid="MyPhone"
  key_mgmt=WPA-PSK
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  eap=TTLS PEAP TLS
  psk="hotspot_pw"
  id_str="iphone_hotspot"
  priority=2
}
```
As you can see I have added two networks to the configuration, and given the network associated with my phone (in personal hotspot mode) a lower priority so it will be a fallback only. _Note: you can change the name of your iPhone (and thus its personal hotspot) using itunes, and you can find the hotspot password in the hotspot settings on the iphone._


You can also add support for connecting to any open network (at your own risk) with an empty network statement

```
network={
  id_str="open"
  priority=0
}
```

If the network you are connecting to has a hidden ssid then you need to add _scan_ssid=1_ to the configuration description. Because _scan_ssid=0_ is the default setting and is used for a broadcast ssid it can be omitted from the configuration of networks using a broadcast ssid. 

```
network={
  scan_ssid=1
  ssid="MyHiddenSSID"
  key_mgmt=WPA-PSK
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  eap=TTLS PEAP TLS
  psk="hidden_hotspot_pw"
  id_str="hidden_hotspot"
  priority=2
}
```

### Switching to AP mode and back

The Edison comes pre-configured for AP mode but if you are curious about changing the settings the configuration file can be found at _/etc/hostapd/hostapd.conf_.  The other key networking file that should require no changes for this configuration is _/etc/network/interfaces_.

In the case when no configured network is available it is possible to connect a gesture (my device has an mpu-6050) to force the device into AP mode so it can get information from the user about how to connect to a new local network. The gesture observer thread can inform the node app when the preconditions of an AP mode switch should occur, the node app can then switch the Wi-Fi network temporarily to AP mode.

This is accomplished by stoping the wpa_supplicant service and starting the APN services using these two system commands that can be executed in  exec() or spawn() calls.

```
systemctl stop wpa_supplicant
systemctl start hostapd
```

### Adding a network
Now the device is in AP mode and the user can connect to the device by selecting it from the list of available networks, and go to the device confguration page for information about available networks and choose one to connect to. I won't get into the scanning now but you can look <a href="https://goo.gl/xDxM5R" target="_blank">here</a> for more info on using _wpa_cli scan__ and __wpa scan_results__ for getting info on available networks.


Once the user chooses a network and provides a password you can configure the device to use the network. My preference is to add the network and a config entry in the wpa_supplicant.conf file so the network can be used again in the future, but you can also use the wpa_cli to configure the network directly. Just use the format shown above to append your entry to the file.

### Switch back to Wi-Fi client mode to connect to the newly added network.

```
wpa_cli reconfigure
systemctl stop hostapd
systemctl start wpa_supplicant
```

I will add my code for the entire process to a public gist when I have fully tested it out, and update this post.
