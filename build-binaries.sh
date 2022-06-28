pyinstaller -F --onefile clock.py
cd dist
cp clock ..
cd ..
rm -rf clock.spec dist build
echo "Done!"
echo "Now run create-command.sh."
