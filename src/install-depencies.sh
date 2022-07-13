#!/bin/bash
echo "Installing python3... (needs root password, the process will be skipped if python3 is already installed)"
sudo apt install python3
clear
echo "Installing pip..."
sudo apt install python3-pip
clear
echo "Installing all required modules..."
sudo python3 -m pip install -r requirements.txt
clear
echo "Done!"
echo "Now run build-binaries.sh to build your binary.."
