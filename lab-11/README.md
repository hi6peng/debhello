# CMake（多个二进制软件包）

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
