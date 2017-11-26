# PhotoBooth

## Setup
### Clone project
```
cd /home/pi
git clone https://github.com/danielsagert/PhotoBooth.git
chmod +x start-server.sh
chmod +x start-ui.sh
```

### Raspi Config
```
sudo raspi-config
```
**Enable camera:**  
*5 Interfacing Options -> P1 Camera*

**Enable SPI**  
*5 Interfacing Options -> SPI*
 
```
sudo apt-get install python-picamera
```

### Python Modules
```
sudo pip install flask, picamera, gunicorn, pifacedigitalio, pifacecommon
```

### Install PiFace Digital Modules ###
```
sudo apt-get install python3-pifacedigitalio
sudo apt-get install python3-pifacedigital-emulator
```

#### Configure kiosk mode
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```

Disable screensaver, do not turn off display and start browser 
```
# @xscreensaver -no-splash
@xset s off
@xset s noblank
@xset -dpms
@sh /home/pi/PhotoBooth/start-ui.sh
```

#### Crontab
```
sudo crontab -e
```

Add lines for server start-up after boot.
```
@reboot /home/pi/PhotoBooth/start-server.sh
```
