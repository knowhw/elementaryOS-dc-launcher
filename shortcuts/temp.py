

import tempfile


from os import fdopen, system
from os import remove
from os import system as create_save
from os import path
from os import getenv


_name, _pkexec = "name of the file is: %s","pkexec %s %s %s "

_save_directory='cache.save'
_save='cp %s /tmp/%s/%s'

class temp:
	
	def __create_savefile():
		
		tmp_dir, temp_file = path.split(filename)
		create_save (_save % (filename,_save_directory, '%s.save' % temp_file))
	
	
	
	
	def mv2(path, deleted='true', user=''):
	
		proc= 'cp' if deleted == 'false' else 'mv' 
		
		system ('cd /tmp && mkdir %s > /dev/null 2>1' % _save_directory)
		"""setapp: kurtarma dizini /tmp/cache.save """
		system (_pkexec % (proc, filename, path) if user == 'root' else "%s %s %s" % (proc, filename, path))
		"""path: usr/share/applications/test.desktop"""



		if proc == "cp":
			temp.__create_savefile()
	def delete(filename): 
		
		base = path.basename(filename)
		base = chr(47).join(['/tmp', _save_directory, '%s.save' % base])
		
		
		[ remove('%s' % item) for item in ( filename, base ) ]
		

	class pkexec:
		def mv2(path, deleted='true', user='root'): temp.mv2(path, deleted='true', user='root')
			
			
			
			
def filetouch(content):
	global filename
	 
	tmp, filename = tempfile.mkstemp()
	with fdopen(tmp, 'w') as tmp: tmp.write(content)

	return temp, filename


