pyinstaller -F --onefile rice-clock.py
cd dist
cp rice-clock ..
cd ..
rm -rf rice-clock.spec dist build
echo "Done!"
echo "Now run create-command.sh."
