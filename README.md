# PhotoBooth

## Functionality
### Flashback view
[http://localhost:8000/](http://localhost:8000/)  
Shows at best the last six pictures depending on the screen size.  
The view will automatically be updated as soon as a new image is available.

### Summary view
[http://localhost:8000/summary](http://localhost:8000/summary)  
Shows all pictures stored in the file system as thumbnails.  
Opens full-sized image on click.

### Trigger capture
The PiFace Digital 2 switch S0 (or connected switch) triggers the capture.  
Countdown will appear and photo will be taken after three seconds.  

## Setup
### Clone project
```
cd /home/pi
git clone https://github.com/danielsagert/PhotoBooth.git
cd /home/pi/PhotoBooth
chmod +x *.sh
```

### Raspi config
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

### Python modules
```
sudo pip install flask, picamera, gunicorn, pifacedigitalio, pifacecommon
```

### Install PiFace Digital 2 modules ###
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
