#! /usr/bin/python2.7

import gaugette.rotary_encoder
import gaugette.switch
from time import sleep
from time import clock

from xbmcclient import XBMCClient,ACTION_EXECBUILTIN,ACTION_BUTTON

host = "localhost"
port = 9777

xbmc = XBMCClient("Pi Remote", "")
xbmc.connect()

A_PIN  = 9
B_PIN  = 7
SW_PIN = 8
 
encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)
last_state = 0

stepcount=0
nullify=0
switch_last=clock()

 
while True:

    delta = encoder.get_delta()
    if delta!=0:
        #print "rotate %d" % delta
	stepcount+=delta

	if stepcount > 3:
		stepcount=0
		#print "rotation"
		if sw_state == 1:
			nullify=1
			xbmc.send_keyboard_button("left")
			sleep(0.05)
			xbmc.release_button()
		else:
			xbmc.send_keyboard_button("up")
			sleep(0.05)
			xbmc.release_button()
	elif stepcount < -3:
		stepcount=0
		#print "counterrotation"
		if sw_state == 1:
			nullify=1
			xbmc.send_keyboard_button("right")
			sleep(0.05)
			xbmc.release_button()
		else:
			xbmc.send_keyboard_button("down")
			sleep(0.05)
			xbmc.release_button()


 
    sw_state = switch.get_state()
    if sw_state != last_state:
        #print "switch %d" % sw_state
        last_state = sw_state

	if sw_state == 1:
		switch_last = clock()
		nullify=0
		
	if sw_state == 0:
		if nullify == 0:
			if clock() > switch_last + 1:
				xbmc.send_keyboard_button("backspace")
				sleep(0.05)
				xbmc.release_button()
			else:
				xbmc.send_keyboard_button("enter")
				sleep(0.05)
				xbmc.release_button()
