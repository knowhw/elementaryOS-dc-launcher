

"""
[Desktop Entry]
Name=Help
Comment=Get help with GNOME
Keywords=documentation;information;manual;help;
OnlyShowIn=GNOME;Unity;
StartupNotify=true
Terminal=false
Type=Application
Categories=GNOME;GTK;Core;Documentation;Utility;
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-Bugzilla-Component=general
X-GNOME-Bugzilla-Version=3.26.0
MimeType=x-scheme-handler/ghelp;x-scheme-handler/help;x-scheme-handler/info;x-scheme-handler/man;
X-Ubuntu-Gettext-Domain=yelp


"""
class test:
	
	def __init__(self, key):
		self.item = chr(32).join ([ value for item, value in globals().items() if item == key ])
	@property
	def text(self) -> str:
		return self.item if self.item else None
	@property
	def tolist(self) -> list:
		return [ item for item in self.item.split(';') if item ]


def getitem(key) -> object:
	return test(key)





