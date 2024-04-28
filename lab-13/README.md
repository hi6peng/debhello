# Autotools（多个二进制软件包）

~~~
gettextize
rm -rf m4 build-aux *~
fgrep -v '[fr]=' data/hello.desktop > data/hello.desktop.in
rm data/hello.desktop
~~~

... hack, hack, hack, ...

po/Makevars
$ rm po/Makevars.template

src/hello.c
lib/sharedlib.c


~~~
$ cat po/POTFILES.in
src/hello.c
lib/sharedlib.c
data/hello.desktop.in
~~~

~~~
$ cat Makefile.am
# recursively process `Makefile.am` in SUBDIRS
SUBDIRS = po lib src man

ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = build-aux/config.rpath m4/ChangeLog
~~~

po/debhello.pot
xgettext -f po/POTFILES.in -d debhello -o po/debhello.pot -k_

* po/LINGUAS 与 po/zh_CN.po
echo 'zh_CN' > po/LINGUAS
cp po/debhello.pot po/zh_CN.po
vim po/zh_CH.po


此处的 -b',libsharedlib1,libsharedlib-dev' 选项是用以指明生成的二进制包。

$ debmake -b',libsharedlib1,libsharedlib-dev' -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'

... hack, hack, hack, ...

## build

~~~
cp -af lab-11 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
