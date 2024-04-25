#
# Regular cron jobs for the debhello package
# See dh_installcron(1) and crontab(5).
#
0 4	* * *	root	[ -x /usr/bin/debhello_maintenance ] && /usr/bin/debhello_maintenance
