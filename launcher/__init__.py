

import temp

from launcher import glob
from listdir import applications
import os
import time


	
class dock(list):
	
	
	def __init__(self):
		self.content = """
[PlankDockItemPreferences]
Launcher=file:///usr/share/applications/%s.desktop
"""
	def add_toDock(self, item, wait=None):
		
		apps = applications()
		
			
		if item in apps:
			
			
			path = '%s/%s.dockitem' % (glob.dockdir, item)
			# /home/linux/.config/plank/dock1/launchers/spyder3.dockitem
			
			tempfile, name = temp.filetouch(self.content % item)
			tempfile.mv2(path)
			
			return "Done"
			
			
		else:
			return 
			
	def remove_from_dock(self,item):
		glob.os.system(glob.null % (glob.dockdir, item))
		# rm %s/%s.dockitem > /dev/null 2>&1

	@property
	def ls(self):


		for item in [ os.path.realpath(item) for item in os.listdir(glob.dockdir) ]:
			

			name, extension = os.path.splitext(os.path.basename(item))
			if ".dockitem" == extension:
				glob.dockitems.append(name)
			

		return glob
		



		





