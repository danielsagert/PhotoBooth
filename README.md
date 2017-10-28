# PhotoBooth

## Setup
### Clone project
```
cd /home/pi
sudo git clone https://github.com/danielsagert/PhotoBooth.git
sudo chmod +x start-server.sh
sudo chmod +x start-ui.sh
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
sudo pip install flask, picamera, gunicorn
```

### Install PiFace Digital Modules ###
```
sudo apt-get install python3-pifacedigitalio
sudo apt-get install python3-pifacedigital-emulator
```

### Install Apache
Follow [this documentation](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md).

### Install and setup samba
```
sudo apt-get install samba samba-common-bin
```

```
sudo nano /etc/samba/smb.conf
```

Comment out `[homes]` section and add new share:

```
security = user

[PhotoBooth Photos]
path = /home/pi/PhotoBooth/static/photos
writeable = yes
guest ok = no
```

```
sudo smbpasswd -a pi
```

```
sudo /etc/init.d/samba restart
```

#### Configure kiosk mode
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```

Disable screensaver and do not turn off display 
```
# @xscreensaver -no-splash
@xset s off
@xset s noblank
@xset -dpms
```

#### Crontab
```
sudo crontab -e
```

Add lines for server start-up after boot.
```
@reboot /home/pi/PhotoBooth/start-server.sh
@reboot /home/pi/PhotoBooth/start-ui.sh
```
