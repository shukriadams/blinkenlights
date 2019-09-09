from blinkt import set_pixel, set_brightness, show, clear
from urllib.request import urlopen
import time
import configparser
from RGBColor import RGBColor
from pathlib import Path

config = configparser.ConfigParser()
checkUrl = None

iniPath = './config.ini'

if Path(iniPath).is_file():
    config.read(iniPath)
else:
    print('Ini file not found @ {iniPath}. Please create a valid config file (check setup instructions)'.format(iniPath=iniPath))
    exit()

common = config['basic']
# remote url to check for status. 
checkUrl = common.get('checkUrl')
# LED brightness
brightness = float(common.get('brightness', 0.06))
# how often remote will be queried (in seconds)
pollInterval = int( common.get('pollInterval', 5))

if checkUrl is None:
    print('error : checkUrl not set')
    exit()

print('Checking:')
print('- URL: {checkUrl}'.format(checkUrl=checkUrl))
print('- brightness: {brightness}'.format(brightness=brightness))
print('- pollInterval: {pollInterval}'.format(pollInterval=pollInterval))

r = RGBColor(10)
g = RGBColor(20)
b = RGBColor(30)
blink = False

while True:

    passed = False
    hasConnected = false
    
    try:
        data = urlopen(checkUrl).read() 
        passed = data.decode('utf-8') == "0"
        hasConnected = true
    except Exception as e:
        # show red no last light on connection error
        set_pixel(7, 255, 0, 0, brightness)
        print (e)    
    
    if hasConnected:

        # gradually shift last light color on successful poll
        r.increment()
        g.increment()
        b.increment()
        set_pixel(7, r.getValue(), g.getValue(), b.getValue(), brightness)

        if passed == True:
            set_pixel(0, 0, 128, 0, brightness)
        else:
            # alternate between blank and red to flash on fail
            blink = not blink
            if blink:
                set_pixel(0, 0, 0, 0)
            else:
                set_pixel(0, 255, 0, 0, brightness)

    show()
    time.sleep(pollInterval)
