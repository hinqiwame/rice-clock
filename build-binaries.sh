sudo apt install pyinstaller
pyinstaller -F --onefile rice-clock.py
cd dist
cp rice-clock ..
cd ..
rm -rf rice-clock.spec dist build
echo "Done!"
