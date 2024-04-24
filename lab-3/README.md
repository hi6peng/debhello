无 Makefile（shell，命令行界面）

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

~~~
$ debmake -b ":sh" -t -p debhello -u 0.1 -r 1 -x1
$ cd ..
~~~


~~~
$ cp -af debhello-0.1 lab-3
$ cd lab-3
~~~

... hack, hack, hack, ...
