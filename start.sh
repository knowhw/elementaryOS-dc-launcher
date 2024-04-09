#!/bin/sh
sudo systemctl stop dc-launcher.service 

sudo systemctl daemon-reload
sudo systemctl enable --now dc-launcher.service 
# sudo systemctl restart dc-launcher.service

sudo systemctl status dc-launcher.service

#
sudo apt autoremove deepin-picker kazam -y
sudo apt install deepin-picker kazam -y
