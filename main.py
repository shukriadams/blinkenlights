from blinkt import set_pixel, set_brightness, show, clear
from urllib.request import urlopen
import time
import configparser
import threading
from RGBColor import RGBColor
from pathlib import Path

# ensure config.ini exists
iniPath = './config.ini'
if not Path(iniPath).is_file():
    print('Ini file not found @ {iniPath}. Please create a valid config file (check setup instructions)'.format(iniPath=iniPath))
    exit()

config = configparser.ConfigParser()
config.read(iniPath)
common = config['basic']
# remote url to check for status. 
checkUrl = common.get('checkUrl')
# LED brightness
brightness = float(common.get('brightness', 0.06))
# how often remote will be queried (in seconds)
pollInterval = int( common.get('pollInterval', 5))
# interval for status light update
pulseInterval = float(common.get('pulseInterval', 0.01))
blink = False
passed = False
hasConnected = False
r = RGBColor(5, 50) # cap red so we don't get distracting red on status
g = RGBColor(10)
b = RGBColor(15)

if checkUrl is None:
    print('error : checkUrl not set')
    exit()

print('Checking:')
print('- URL: {checkUrl}'.format(checkUrl=checkUrl))
print('- brightness: {brightness}'.format(brightness=brightness))
print('- pollInterval: {pollInterval}'.format(pollInterval=pollInterval))

def check_status():
    global passed
    global hasConnected

    while True:

        try:
            data = urlopen(checkUrl).read() 
            passed = data.decode('utf-8') == "0"
            hasConnected = True
        except Exception as e:
            # show red no last light on connection error
            hasConnected = False
            passed = False
            print (e)    

        time.sleep(pollInterval)

statusThread = threading.Thread(target=check_status)
statusThread.start()

while True:
    if hasConnected:
        # gradually shift last light color on successful poll
        set_pixel(7, r.incrementAndGetValue(), g.incrementAndGetValue(), b.incrementAndGetValue(), brightness)

        if passed == True:
            # green
            set_pixel(0, 0, 128, 0, brightness)
        else:
            # alternate between blank and red to flash on fail
            blink = not blink
            if blink:
                set_pixel(0, 0, 0, 0)
            else:
                # red
                set_pixel(0, 255, 0, 0, brightness)
    else:
        #rec
        set_pixel(7, 255, 0, 0, brightness)

    show()
    time.sleep(pulseInterval)
