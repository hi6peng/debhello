# Autotools（单个二进制文件）

$ debmake -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'

... hack, hack, hack, ...

## build

~~~
cp -af lab-8 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
