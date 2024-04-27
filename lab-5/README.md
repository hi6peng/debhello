# Makefile（shell，图形界面）

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
├── Makefile
├── man
│   └── hello.1
├── README.md
└── scripts
    └── hello
~~~

hello
~~~
$ cat scripts/hello
#!/bin/sh -e
zenity --info --title "hello" --text "Hello from the shell!"
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
        install -m 644 -D man/hello.1 \
                $(DESTDIR)$(prefix)/share/man/man1/hello.1

clean:
        : # do nothing

distclean: clean

uninstall:
        -rm -f $(DESTDIR)$(prefix)/bin/hello
        -rm -f $(DESTDIR)$(prefix)/share/applications/hello.desktop
        -rm -f $(DESTDIR)$(prefix)/share/pixmaps/hello.png
        -rm -f $(DESTDIR)$(prefix)/share/man/man1/hello.1

.PHONY: all install clean distclean uninstall
~~~

~~~
$ debmake -b ":sh" -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'
$ cd ..
~~~

~~~
$ cp -af debhello-0.1 lab-3
$ cd lab-3
~~~

... hack, hack, hack, ...
debian/rules

## build

~~~
cp -af lab-5 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
