out: config.py main.py bin/c/checkroot.c bin/c/floatoper.c bin/c/floatopermulti.c bin/c/intoper.c bin/c/intopermulti.c bin/c/ramalloc.c bin/c/randgen.c bin/html/help.html bin/logos/ README.md
	# Configuring for normal build...
	cp config_template.py config.py
	echo "COMPILED=False;" >> config.py
	# Building
	./build.sh
	ln -sf main.pyc out/gsysinfo
	# Done.

base: main.py
	# NOTE: This only builds main.py. Intended for development purposes.
	python3 -m compileall main.py
	chmod +x main.pyc
	mv main.pyc out/main.pyc

.PHONY: base