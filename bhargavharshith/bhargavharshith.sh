#!/bin/bash
sudo apt update -y
sudo apt install docker.io -y
sudo apt update -y
sudo apt install apache2 -y
sudo systemctl start apache2
sudo systemctl status apache2
