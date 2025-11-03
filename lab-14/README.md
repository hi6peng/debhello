https://john-tucker.medium.com/debian-packaging-by-example-118c18f5dbfe


~~~
$ export EMAIL=hi6peng@qq.com; dch --create -v 1.0-1 --package hideb
$ tar -czvf hideb_1.0.orig.tar.gz hideb-1.0
$ debuild -us -uc
~~~
