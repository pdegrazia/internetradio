# -*- coding: utf-8 -*-
#from gpiozero import MCP3008
#import time
import os

print 'init adc'
#station_dial=MCP3008(0)
print 'all good'


Magic = 'http://tx.whatson.com/icecast.php?i=magic1054.mp3.m3u'
Radio1 ='http://www.listenlive.eu/bbcradio1.m3u'

def change_station(station):
    os.system("killall mplayer")
    print 'here'
    os.system("mplayer -playlist "+ station + " &")
    print 'here'

change_station(Magic)

#while True:
    #change_station(Magic)
    #print 'starting loop'
    #print station_dial.value
    #if station_dial.value >= 0.5:
        ##station = Magic
        #print '>0.5'
        ##change_station(station)
    #elif station_dial.value < 0.5:
        #print '<0.5'
        #station = Radio1
        #change_station(station)
    #time.sleep(0.1)