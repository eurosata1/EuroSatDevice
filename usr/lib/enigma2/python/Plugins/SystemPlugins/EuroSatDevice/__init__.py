# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext

#def localeInit():
#	gettext.bindtextdomain("EuroSatDevice", resolveFilename(SCOPE_PLUGINS, "SystemPlugins/EuroSatDevice/locale"))

def _(txt):
	t = gettext.dgettext("EuroSatDevice", txt)
	if t == txt:
#		print "[EuroSatDevice] fallback to default translation for:", txt
		t = gettext.gettext(txt)
	return t

#localeInit()
#language.addCallback(localeInit)
