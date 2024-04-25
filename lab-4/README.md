# Makefile（shell，命令行界面）

## init

~~~
$ mkdir debhello-0.1
$ cd debhell0-0.1
~~~

... hack, hack, hack, ...

~~~
$ tree
.
├── data
│   ├── hello.desktop
│   └── hello.png
├── README.md
└── scripts
    └── hello
~~~

hello
~~~
$ cat scripts/hello
#!/bin/sh -e
echo "Hello from the shell!"
echo ""
echo -n "Type Enter to exit this program: "
read X
~~~

hello.desktop
~~~
$ cat data/hello.desktop
[Desktop Entry]
Name=Hello
Name[fr]=Bonjour
Comment=Greetings
Comment[fr]=Salutations
Type=Application
Keywords=hello
Exec=hello
Terminal=true
Icon=hello.png
Categories=Utility;
~~~

Makefile
~~~
prefix = /usr/local

all:
        : # do nothing

install:
        install -D scripts/hello \
                $(DESTDIR)$(prefix)/bin/hello
        install -m 644 -D data/hello.desktop \
                $(DESTDIR)$(prefix)/share/applications/hello.desktop
        install -m 644 -D data/hello.png \
                $(DESTDIR)$(prefix)/share/pixmaps/hello.png

clean:
        : # do nothing

distclean: clean

uninstall:
        -rm -f $(DESTDIR)$(prefix)/bin/hello
        -rm -f $(DESTDIR)$(prefix)/share/applications/hello.desktop
        -rm -f $(DESTDIR)$(prefix)/share/pixmaps/hello.png

.PHONY: all install clean distclean uninstall
~~~

~~~
$ debmake -b ":sh" -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'
$ cd ..
~~~

~~~
$ cp -af debhello-0.1 lab-4
$ cd lab-4
~~~

... hack, hack, hack, ...
debian/rules

## build

~~~
cp -af lab-4 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
