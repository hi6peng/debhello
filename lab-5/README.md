# setup.py（Python3，图形界面）

$ debmake -b ":py3" -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'

... hack, hack, hack, ...

debian/rules
debian/control

## build

~~~
cp -af lab-5 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
