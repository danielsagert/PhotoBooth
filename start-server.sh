#!/bin/sh
cd /home/pi/PhotoBooth/
sudo gunicorn --bind 0.0.0.0:8000 --workers 10 webserver:app
