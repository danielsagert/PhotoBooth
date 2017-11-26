#!/bin/sh
sudo pkill gunicorn
pkill -9 -f control.py

cd /home/pi/PhotoBooth/

mkdir -p logs

sudo python ./control.py 2>&1 | tee logs/control.log &
sudo gunicorn --bind 0.0.0.0:8000 --workers 10 webserver:app 2>&1 | tee logs/webserver.log
