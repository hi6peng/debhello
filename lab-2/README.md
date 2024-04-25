debmake 使用 -x4 选项来生成最大数量的模板文件
~~~
$ mkdir debhello-0.1
$ cd debhell0-0.1
$ debmake -t -p debhello -u 0.1 -r 1 -x4
$ cd ..
~~~

复制 debhello-0.1/debian/ 目录下所有生成的模板文件到您的软件包中
~~~
$ mkdir lab-2 
$ cd lab-2
$ mv ../debhello-0.1/debian .
~~~
