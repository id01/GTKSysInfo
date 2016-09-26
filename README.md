## GTK System Information
This is a simple front end GUI for multiple command line system info utilities on GTK.  
This is the python 3 port.

## Installation
To build for your system, run: 
```
make
```
All files will be put in the out/ directory. If built this way, dependencies must be installed on the system.

To run:
```
out/gsysinfo
```

## Contributors
id01 (Main Developer)

## Libraries Used
* [PyGObject](http://www.pygtk.org/), by James Henstrige, Licensed under GNU LGPL. Imported in main.py.
* [Python3](https://www.python.org/) and included libraries, by Python Software Foundation, Python License. Used in all py files.
* C++ Used in bin/c/*.cpp
* C Used in bin/c/*.c
* Disclaimer: Manufacturer logos are not my own. Intel logos are (c) Intel Inc. AMD logos are (c) AMD Inc.

## System Requirments
Same as Python 2, but replacing Python 2 modules with their python 3 counterparts.

## Changelog
* 0.1.0 (Testing, Python3)
 * Ported to Python 3
* 0.1.0 (Testing)
 * High latency stress tests
* 0.0.9 (Prerelease)
 * Created makefile
 * Created configuration python file
* 0.0.8 (Prerelease)
 * Created Landing page
 * Created Help.html
 * Removed "no root" warning popup
 * Updated comments, preparing for publicizing of repository.
* 0.0.7 (Prerelease)
 * Added more images
 * Ramalloc.c instead of .cpp, more efficient, more accurate result.
 * Stress test units in Kx/s instead of x/s
* 0.0.6 (Prerelease)
 * Added images
* 0.0.5 (Prerelease)
 * Added freeze.py install
 * Got $PATH working
 * Fixed freeze.py crash if no arguments included
* 0.0.4 (Prerelease):
 * Added CPU information.
 * Added other MB information.
 * Preparing to add a few images.
 * Disabled freeze.py install (not working)
 * Extended path support (slightly)
* 0.0.3 (Prerelease):
 * Added freeze support.
 * Slight changes in main.py to support freeze.
 * Improved on stress test save feature.
 * Added support for absolute paths.
* 0.0.2 (Prerelease):
 * Added README.
 * Modified Multicore to show cumulative power instead of average power.
 * Added root features.
 * Added ability to save stress test results.
 * Added copy/paste for stress test results.
* 0.0.1 (Prerelease):
 * Initial Commit
 * Added main.py
 * Added stress test
 * Added disk data
 * Added build.sh
 * Added pretty much everything that wasn't in later releases
