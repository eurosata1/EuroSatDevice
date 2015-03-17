#
#  EuroSatDevice Mod. EuroS@t
#  thx Coded by Dr.Best (c)2010
#  Support: www.dreambox-tools.info
#
#  This plugin is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported 
#  License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative
#  Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially 
#  distributed.
#
from . import _

from HddSetup import HddSetup
from HddMount import HddFastRemove
from Plugins.Plugin import PluginDescriptor

def deviceManagerSetup(session, **kwargs):
	session.open(HddSetup)

def deviceManagerFastRemove(session, **kwargs):
	session.open(HddFastRemove)


def Plugins(**kwargs):
	return [PluginDescriptor(name = _("EuroSat Device"), description = _("Format/Partition your Devices and manage Mountpoints"), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc = deviceManagerSetup)]
			

