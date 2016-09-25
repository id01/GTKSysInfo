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
	python -m compileall main.py
	chmod +x main.pyc
	mv main.pyc out/main.pyc

freeze: main.py bin/c/checkroot.c bin/c/floatoper.c bin/c/floatopermulti.c bin/c/intoper.c bin/c/intopermulti.c bin/c/ramalloc.c bin/c/randgen.c bin/html/help.html bin/logos/ freeze.py README.md
	# Configuring for freeze...
	cp config_template.py config.py
	echo "COMPILED=True;" >> config.py
	# Building
	./build.sh
	# Freezing
	python freeze.py build
	# Done.

freeze-install: build/
	# Copying to /usr/lib/GSI...
	mkdir /usr/lib/GSI
	cp -vr build/* /usr/lib/GSI
	# Linking to /usr/local/bin/gsysinfo
	ln -s /usr/lib/GSI/exe*/main /usr/local/bin/gsysinfo
	# Done. Type gsysinfo to run.

freeze-uninstall:
	# Removing /usr/lib/GSI...
	rm -r /usr/lib/GSI
	# Removing symlink...
	rm /usr/local/bin/gsysinfo
	# Done.

.PHONY: freeze
.PHONY: freeze-install
.PHONY: freeze-uninstall
.PHONY: base