# PhotoBooth

## Setup
### Clone project
```
cd /home/pi
sudo git clone https://github.com/danielsagert/PhotoBooth.git

sudo mkdir -p /home/pi/PhotoBooth/static/photos
sudo chown -R pi:pi /home/pi/PhotoBooth/static/photos
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
sudo pip install flask, picamera
```

### Install PiFace Digital Modules ###
```
sudo apt-get install python3-pifacedigitalio
sudo apt-get install python3-pifacedigital-emulator
```

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

### Install Apache
Follow [this documentation](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md).

### Crontab
```
sudo crontab -e
```
Add lines for server start-up after boot.
```
@reboot python /home/pi/PhotoBooth/webserver.py
```