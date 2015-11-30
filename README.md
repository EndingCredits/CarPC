# CarPC
Various files and resources for setting up a Pi based In-Car Entertainment system.. Mainly for my own reference but may be a good resource for others looking to do similar things.

== Installing Xbian ==


== Installing Wifi ==


https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/overview
http://www.daveconroy.com/turn-your-raspberry-pi-into-a-wifi-hotspot-with-edimax-nano-usb-ew-7811un-rtl8188cus-chipset/

== Setting up LCD ==

apt-get LCDproc

download lcdproc and make with ./configure --enable-drivers=serialVFD,hd44780, make (need to install build-utils)
edit LCDd.conf and copy into lcdproc directory, copy serialVFD.so into appropriate directory
http://www.rototron.info/lcdproc-tutorial-for-raspberry-pi/

http://www.sknorrell.de/blog/lcd-display-hd44780-20x4-under-openelec-and-xbmc-at-the-raspberry-pi/

wire up 5V,GND, tx, or wire up as above

install lcdproc addon for kodi with git clone https://github.com/herrnst/script.xbmc.lcdproc.git into ~/.kodi/addons/

sudo reboot and test

== Setting up GPIO as inputs to Kodi ==

Using Gaugette: https://github.com/guyc/py-gaugette

Install Wiring-pi2 with:
sudo apt-get install python-setuptools python-dev
git clone https://github.com/Gadgetoid/WiringPi2-Python.git
cd WiringPi2-Python/
sudo python setup.py install
cd ..

Install py-guagette with:
git clone https://github.com/guyc/py-gaugette.git
cd py-gaugette/
sudo python setup.py install
cd ..

Get xbmclient.py:
wget https://raw.githubusercontent.com/xbmc/xbmc/master/tools/EventClients/lib/python/xbmcclient.py

Run Switch.py

Setup Switch.py to run as a service (or kodi addon).

http://guy.carpenter.id.au/gaugette/2013/01/14/rotary-encoder-library-for-the-raspberry-pi/






