#!/bin/bash

echo "Creating directories"
mkdir out 2> /dev/null
mkdir out/bin 2> /dev/null
mkdir out/bin/c 2> /dev/null
mkdir out/bin/logos 2> /dev/null
mkdir out/bin/html 2> /dev/null
printf "Compiled: " > out/build.txt
echo $(date) >> out/build.txt
echo "" >> out/build.txt
cat README.md >> out/build.txt
echo "Compiling checkroot.c"
gcc -o out/bin/c/checkroot bin/c/checkroot.c
echo "Compiling floatoper.c"
gcc -o out/bin/c/floatoper bin/c/floatoper.c
echo "Compiling intoper.c"
gcc -o out/bin/c/intoper bin/c/intoper.c
echo "Compiling floatopermulti.c"
gcc -pthread -o out/bin/c/floatopermulti bin/c/floatopermulti.c
echo "Compiling intopermulti.c"
gcc -pthread -o out/bin/c/intopermulti bin/c/intopermulti.c
echo "Compiling floatoperlatent.c"
gcc -pthread -o out/bin/c/floatoperlatent bin/c/floatoperlatent.c
echo "Compiling intoperlatent.c"
gcc -pthread -o out/bin/c/intoperlatent bin/c/intoperlatent.c
echo "Compiling randgen.c"
gcc -o out/bin/c/randgen bin/c/randgen.c
echo "Compiling ramalloc.c"
gcc -o out/bin/c/ramalloc bin/c/ramalloc.c
echo "Compiling diskalloc.cpp"
g++ -o out/bin/c/diskalloc bin/c/diskalloc.cpp
echo "Copying Logos"
cp bin/logos/* out/bin/logos/
echo "Copying Help"
cp bin/html/* out/bin/html/
echo "Compiling config.py"
python3 -m compileall config.py | grep -v "Compiling config.py..."
mv __pycache__/config.*.pyc out/config.pyc
chmod +x out/config.pyc
echo "Compiling main.py"
python3 -m compileall main.py | grep -v "Compiling main.py..."
mv __pycache__/main.*.pyc out/main.pyc
chmod +x out/main.pyc
rm -r __pycache__