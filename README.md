## GTK System Information
This is a simple front end GUI for multiple command line system info utilities on GTK.

## Installation
To build for your system, run: 
```
./build.sh
```
All files will be put in the out/ directory. If built this way, dependencies must be installed on the system.

To run:
```
out/main.pyc
```

To build a portable version, run:
```
python freeze.py build
```
Files will be placed in the build/ directory. Program may run into problems if built this way.

## Contributors
id01 (Main Developer)

## Libraries Used
[PyGObject](http://www.pygtk.org/), by James Henstrige, Licensed under GNU LGPL. Used in main.py.
[Python](https://www.python.org/), by Python Software Foundation, Python License. Used in main.py and freeze.py.
[cx_Freeze 4.3.4](https://pypi.python.org/pypi/cx_freeze), by Anthony Tuininga, Python License. Used in freeze.py.
[C++](https://isocpp.org), by Standard C++ Foundation. Used in bin/c/*.cpp
C Used in bin/c/*.c

## Changelog
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