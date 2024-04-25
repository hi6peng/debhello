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

clean:
	: # do nothing

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/bin/hello
	-rm -f $(DESTDIR)$(prefix)/share/applications/hello.desktop
	-rm -f $(DESTDIR)$(prefix)/share/pixmaps/hello.png

.PHONY: all install clean distclean uninstall
