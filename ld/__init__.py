
from ld import glob


def applications():

	import os
	
	
	# global path_desktop_items
	path_desktop_items = [ os.path.realpath(item) 
	for item in os.listdir(glob.appdir) ]


	dictionary = {}
	""" dictionary: app list => usr share applications """
	
	
	for item in path_desktop_items:
		
		
		name, extension = os.path.splitext(os.path.basename(item))
		if ".desktop" != extension:
			continue
		
		dictionary [name] = '%s/%s%s' % (glob.appdir, name, extension)
		""" 'path':'%s/%s%s' % (glob.appdir, exec, extension) """
		
	
	return dictionary


