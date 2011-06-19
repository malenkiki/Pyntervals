all: extract merge mo

extract:
	xgettext -j -f po/POTFILES.in -L Python -o po/messages.pot

merge: extract
	msgmerge -U po/fr.po po/messages.pot
	msgmerge -U po/ru.po po/messages.pot
	msgmerge -U po/el.po po/messages.pot

mo: merge
	msgfmt -o locale/fr_FR/LC_MESSAGES/pyntervals.mo po/fr.po
	msgfmt -o locale/ru_RU/LC_MESSAGES/pyntervals.mo po/ru.po
	msgfmt -o locale/el_GR/LC_MESSAGES/pyntervals.mo po/el.po
