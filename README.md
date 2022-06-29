# rice-clock
A rice-like clock for terminals. <br > 
![Screenshot](ghoulss.gif)

# Usage
**Before running the script please make sure that have ran the `install-binaries.sh` script!**
The script can be used with entering `python rice-clock.py -(color)` or `rice-clock -(color)` (if you built the command).

# Creating a command
There are two ways to build a command for your linux system, using the binary from this repository or building you own. <br >
1. **Using binary from GitHub** <br >
Run `create-command.sh`. <br >
2. **Creating your own** <br >
Delete the pre-built binary in the folder of project and run `build-binaries.sh`, and then `create-command.sh`.

# Combining with other terminal color libs
For example, `rice-clock` works pretty good with [lolcat](https://github.com/busyloop/lolcat) (`rice-clock -w | lolcat`): <br >
![Gradient](gradient.png)

# Changelog
```
v1.0.0:
- First release

v1.0.1:
- Minor fixes

v1.1.0:
- Added:
	- Changelog tab to README
	- 2 more except blocks to the script
	- 1 more installation scrpt (install-depencies.sh)
	- 1 more credit to Credits tab
- Edited:
	- Instruction
	- Main script
	- Installation scripts
v1.1.1:
- Added:
	- New screenshot to README (gif now)
	- Minor fixes to different parts of project
	- New binary
- Edited:
	- README
	- Except blocks (now they work better)
	- 1 installation script (build-binaries.sh)
	- Code documentation
```

# To do:
- Switching the color of text in real time (while the script is running)

# Credits:
[Colorama](https://pypi.org/project/colorama/)
[Pyinstaller](https://pypi.org/project/pyinstaller/)

