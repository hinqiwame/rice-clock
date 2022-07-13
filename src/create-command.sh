#!/bin/bash
echo "Copying binary into system binaries directory..."
sudo cp rice-clock /usr/bin/
cd /usr/bin/
clear
echo "Giving permissions for execution..."
sudo chmod +x rice-clock
clear
echo "Done!"
echo "Congrats! You now have pyfetch installed in your system!"
echo "(Location: /usr/bin/)"
