#!/bin/bash
echo "Compiling the file..."
pyinstaller -F --clean clock.py
clear
echo "Removing dist/var files..."
cd dist
cp clock ..
cd ..
rm -rf clock.spec dist build
mv clock rice-clock
clear
echo "Done!"
echo "Now run create-command.sh to install new binary in your system."
