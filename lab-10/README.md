# Autotools（多个二进制软件包）

此处的 -b',libsharedlib1,libsharedlib-dev' 选项是用以指明生成的二进制包。

$ debmake -b',libsharedlib1,libsharedlib-dev' -t -p debhello -u 0.1 -r 1 -x1 -e hi6peng@qq.com -f '6peng'

... hack, hack, hack, ...

## build

~~~
cp -af lab-10 debhello-0.1
tar -czf debhello-0.1.tar.gz debhello-0.1
cd debhello-0.1
debmake
debuild
~~~
