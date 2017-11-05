#!/bin/sh
sudo pkill gunicorn
pkill -9 -f control.py

cd /home/pi/PhotoBooth/
sudo python ./control.py &
sudo gunicorn --bind 0.0.0.0:8000 --workers 10 webserver:app
