# blinkenlights

Raspberry Pi status strip for https://github.com/shukriadams/arewedown. Shows constant green when all processes pass, flashes red when any process fails. Also has a status light which slowly changes color if the AreWeDown server is available, and red if it isn't reachable.

## Requirements 

- Rasperry Pi
- Pimoroni Blinkt (https://shop.pimoroni.com/products/blinkt)
- Raspbian Buster (may work on previous versions)
- Python 3 as global version

## Setup

- force python 3 with following command (force python 3 (this should be added to ~/.bashrc to make it permanent)
  
      alias python='/usr/bin/python3.7'

- install required packages

      sudo apt-get install python3-blinkt -y
      
- clone this repo, then CD to it.

- to manually start run

      python main.py

- to set blinketlights up as a service 
      
      sudo cp blinketlights.service /etc/systemd/system/blinkenlights.service &&
      sudo systemctl daemon-reload &&
      sudo systemctl start blinkenlights &&
      sudo systemctl enable blinkenlights

- to stop it run

      sudo systemctl stop blinkenlights

- to get its status

      sudo systemctl status blinkenlights
