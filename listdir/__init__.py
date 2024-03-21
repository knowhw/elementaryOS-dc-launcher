
from listdir import glob
import time

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


class ardiff:
	
	before={}
	
	def __init__(self, before, watch=''):
		ardiff.before = before
		# before
		self.watch= watch

	
		# before = applications()
		# installed = ardiff(before, watch="installed").tolist
	
	@property
	def tolist(self) :
		if self.watch == 'installed':
			time.sleep(1.5)
	

			if len(applications()) > len(ardiff.before):
				for item in [  item for item in applications() if not item in ardiff.before   ]:
					yield item
					
				
			
		
		
		# [  item for item in self.after if not item in self.before   ]
		# Wed Mar  6 18:04:51 CST 2024
		# Wed Mar  6 18:30:53 CST 2024











