#!/usr/bin/env bash
# A bash script that sets up a web server for deployment of web_static.

sudo apt-get -y update
sudo apt-get -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current/
sudo echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current/
sudo chown -R ubuntu:ubuntu /data/
serve="location /hbnb_static/{\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "27i $serve" /etc/nginx/sites-available/default
sudo service nginx restart
