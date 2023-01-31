#!/bin/bash

echo ">>>>Installing git"
  sudo apt-get install -y git-core

echo ">>>>Downloading Mininet Wifi"
  sudo git clone https://github.com/intrig-unicamp/mininet-wifi.git

echo ">>>>Installing Mininet Wifi"
  cd mininet-wifi
  sudo util/install.sh -Wlnfv