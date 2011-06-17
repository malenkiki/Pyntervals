all:
	xgettext -j -f po/POTFILES.in -L Python -o po/messages.pot

mo:
	msgfmt -o locale/fr_FR/LC_MESSAGES/pyntervals.mo po/fr.po
