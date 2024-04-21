Create tarball: 
~~~
mv debhello debhello-0.1
tar --exclude='.git' -czf debhello-0.1.tar.gz debhello-0.1
~~~

After that is possible to start with packaging: 
~~~
debmake
~~~

Adjsut the override_dh_usrlocal:
~~~
#!/usr/bin/make -f
# You must remove unused comment lines for the released package.
#export DH_VERBOSE = 1
#export DEB_BUILD_MAINT_OPTIONS = hardening=+all
#export DEB_CFLAGS_MAINT_APPEND  = -Wall -pedantic
#export DEB_LDFLAGS_MAINT_APPEND = -Wl,--as-needed

%:
	dh $@  
override_dh_usrlocal:
#override_dh_auto_install:
#	dh_auto_install -- prefix=/usr

#override_dh_install:
#	dh_install --list-missing -X.pyc -X.pyo
~~~

Build

`dpkg-buildpackage -B`

or

`debuild`
