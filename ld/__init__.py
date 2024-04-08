
from ld import glob

def applications():

	for item in [ glob.os.path.realpath(item) for item in glob.os.listdir(glob.appdir) ]:
		
		
		name, extension = glob.os.path.splitext(glob.os.path.basename(item))
		if ".desktop" != extension:
			continue
		
		glob.dictionary [name] = '%s/%s%s' % (glob.appdir, name, extension)
		""" 'path':'%s/%s%s' % (glob.appdir, exec, extension) """
		
	
	return glob.dictionary


