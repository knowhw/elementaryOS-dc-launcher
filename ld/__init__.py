
from ld import glob

def applications():
	
	import os

	dictionary = {}
	""" dictionary: app list => usr/share/applications """
	
	
	for item in [ os.path.realpath(item) for item in os.listdir(glob.appdir) ]:
		
		
		name, extension = os.path.splitext(os.path.basename(item))
		if ".desktop" != extension:
			continue
		
		dictionary [name] = '%s/%s%s' % (glob.appdir, name, extension)
		""" 'path':'%s/%s%s' % (glob.appdir, exec, extension) """
		
	
	return dictionary


