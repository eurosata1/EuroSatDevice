# for localized messages
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
			

