EXTRA_DIST = $(dist_icon_DATA) $(dist_desktop_DATA)

themedir = $(datadir)/icons/hicolor
size = 48x48
context = apps

icondir = $(themedir)/$(size)/$(context)
dist_icon_DATA = hello.png
 
desktopdir = $(datadir)/applications
dist_desktop_DATA = hello.desktop

%.desktop: %.desktop.in
	$(AM_V_GEN)$(MSGFMT) --desktop --template $< -d $(top_srcdir)/po -o $@
