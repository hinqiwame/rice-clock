pyinstaller -F --onefile clock.py
cd dist
cp clock ..
cd ..
rm -rf clock.spec dist build
mv clock rice-clock
echo "Done!"
echo "Now run create-command.sh."
