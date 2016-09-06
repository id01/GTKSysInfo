#!/bin/bash

printf "Compiled: " > out/build.txt
echo $(date) >> out/build.txt
echo "" >> out/build.txt
cat README.md >> out/build.txt
echo "Creating directories"
mkdir out 2> /dev/null
mkdir out/bin 2> /dev/null
mkdir out/bin/c 2> /dev/null
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
echo "Compiling randgen.c"
gcc -o out/bin/c/randgen bin/c/randgen.c
echo "Compiling ramalloc.cpp"
g++ -o out/bin/c/ramalloc bin/c/ramalloc.cpp
echo "Compiling diskalloc.cpp"
g++ -o out/bin/c/diskalloc bin/c/diskalloc.cpp
echo "Compiling main.py"
python -m compileall main.py | grep -v "Compiling main.py..."
chmod +x main.pyc
mv main.pyc out/main.pyc