#!/bin/sh
sudo pkill gunicorn
sudo pkill -9 -f control.py

cd /home/pi/PhotoBooth/

mkdir -p logs

sudo python ./control.py >> ./logs/control.log 2>&1 &
sudo gunicorn --bind 0.0.0.0:8000 --workers 10 webserver:app >> ./logs/webserver.log 2>&1 &