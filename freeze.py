import sys
import os
import re
import gi
import time
from cx_Freeze import setup, Executable

if sys.argv[1].strip()=="build":
	os.system("./build.sh");
	os.system("mkdir build");
packages = ["re","os","sys","gi","time"]
setup(name="GTKSysInfo", version="0.0.2", description="Frontend system information for Linux GTK", options = {"build_exe": {"packages": packages}}, executables=[Executable("main.py")])
if sys.argv[1].strip()=="build":
	os.system("mv out/* build/exe*/");
	os.system("rm build/exe*/main.pyc");