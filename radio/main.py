# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from gpiozero import MCP3008
import time
import os
import pygame



station_dial=MCP3008(0)
Magic = 'http://tx.whatson.com/icecast.php?i=magic1054.mp3.m3u'
Radio1 ='http://www.listenlive.eu/bbcradio1.m3u'

def change_station(station):
    os.system("killall mplayer")
    os.system("mplayer -playlist "+ station + " &")

current_station = None

class SelectionBar:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def draw(self):
        pass

class RadioScreen:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500, 400))
        print 'pygame init successful'

    def draw(self,length):
        self.window.fill((0,0,0))
        pygame.draw.rect(self.window, (255, 0, 0), (50, 400/2, length, 100))

    def update(self):
        pygame.display.update()


class Radio:
    def __init__(self):
        self.radio_screen = RadioScreen()
        self.current_station = None

    def start(self):
        print 'radio started'
        bar_length = 0
        while True:
            try:
                if station_dial.value >= 0.5:
                    if not self.current_station == Magic:
                        self.current_station = Magic
                        change_station(self.current_station)
                        print 'You are listening to Magic Radio'
                        bar_length = 255
                elif station_dial.value < 0.5:
                    if not self.current_station == Radio1:
                        self.current_station = Radio1
                        change_station(self.current_station)
                        print 'You are listening to Radio1'
                        bar_length = 125
                time.sleep(0.1)
                self.radio_screen.draw(bar_length)
                self.radio_screen.update()
            except KeyboardInterrupt:
                os.system("killall mplayer")
                print 'Killed all mplayer processes'

if __name__ == '__main__':
    radio = Radio()
    radio.start()