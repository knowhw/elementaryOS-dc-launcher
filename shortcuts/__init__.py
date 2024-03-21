# Thu Feb 29 13:59:50 CST 2024



# from au.shortcuts import glob
# from au.listdir import applications
from . import glob, temp
class test:	
	
	# head = 0
	
	class base:
		# testing
		
		def index(base):
			"""
			test.base.index('entry')
			
			"""
			
			index = [ index for index, item in enumerate(glob.context) 
					if item and getattr(glob, base)  == item [0] and item [1:] == [None] *4]
			
			return None if not index else index [-1]
			# 
		class key:
			# Name=Test
			# Icon=face-heart
			# Icon=geany
			
			def index(base, key, action_key=None):
				# its can check in action and entry\ 
				
			
				index = [ index for index, item in enumerate(glob.context) 
					if item and getattr(glob, base) == item [0] 
					and (item[1] == None if not action_key else action_key) and item [2] == glob.LANGUAGE  and item [-2] == key] 
				return index if index else None
					
				# index [-1]: ayni isimde iki (2) anahtar olabilir
					
		def append(base):
			exists = test.base.index('entry')

			if exists == None:
				glob.context.append( [glob.entry, None, None, None, None])
  

	
	def __translate(head, base, key, value, action_key=None):
		# Wed Feb 28 20:05:17 CST 2024
		
		for to in [ item.get(glob._) 
					for item in glob.lang.findall('name') 
					if item.get(glob._) ]: 
			
			
			
			googleapis = "/translate_a/single?client=gtx&dt=t&"
			query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, to, value)
		
	
			if not [ item for item in glob.context if item [0:4] == [ base, None, to, key ] ]:
				head+=1
				
				glob.insert( head, [ "%s" % base, None if base == glob.entry 
				else action_key, to, key, glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0] 
				if glob.check.i else value ])
		
				
	def group(key, value, base, action_key=None):
		
		
		
		
		base = getattr(glob, base.__name__)
		# Thu Feb 29 17:01:30 CST 2024
		
		print("----", base,1)
		
		
		if base == glob.entry:
		
			# print("---- index ", test.base.index('action'))
			# print("---- index ", test.base.key.index('entry', 'Icon'))
			
		
			base_exists = test.base.index('entry')
			# base isexists
			print("---- base.index", base_exists)

			
			if base_exists == None:
				# base not found
				glob.context.append( [glob.entry, None, None, None, None])
  


			index = test.base.key.index('entry', key)
			# base key isexists?
			print("---- base.key.index", index)
			
			
		
			if not index:
				index = test.base.index('entry')
				glob.context.insert(index+1, [glob.entry, None, glob.LANGUAGE, key, value])

			
			
			
			for lang in [ item.get(glob._) 
						for item in glob.lang.findall('name') 
						if item.get(glob._) ]: 
				
				googleapis = "/translate_a/single?client=gtx&dt=t&"
				query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, lang, value)

	
	
				
				index = test.base.key.index('entry', key)

				if not [ item for item in glob.context if item [0:4] == [ base, None, lang, key ] ]:
					#glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0]
					
					value = value if glob.check.i else value
					glob.context.insert(index [0], [ glob.entry, None, lang, key, value ])
					# Thu Feb 29 19:21:01 CST 2024

					
					# used was index [0] instead of [-1]
					
					"""
					
					Icon[yo]=Idanwo
					Icon[zu]=Hlola
					Icon=Test
					
					Name[yo]=Idanwo
					Name[zu]=Hlola
					Name=Test
					Name=Test

					
					"""

		elif base == glob.action:
		
			#index = [  index  for index, item in enumerate(glob.context )
			#if item and item [0] == "%s" % base  and item [3] == key ] 
			
			index = test.base.key.index('action', key, action_key="X")
			
			print("----2", index)
			
			# test.__translate(index[0], base, key, value, action_key)
			
	
				
		return glob
		
	def Global(key, value, base, action_key=None):
			return test.group(key, value, base, action_key)
		
	def index_tail(base):
	
		return [ index+1 for index in range(glob.context.index([ base ]+ [None] * 4), len(glob.context)) 
		if base in glob.context [index] ] [-1]
		# sadece entry icin 
		

	def string(key=None, value=None, base=None, index=None, action=None):


		action_key = action
		
		print("----", key, value, base, index, action)
		
		if action:
			
			
			# target = test.index_tail()
			""""""
			
			base_exists = [ index for index, item in enumerate(glob.context) 
			if glob.action  == item [0] and item [1:] == [None] *4]
			# base isexists?
			# print("base isexists ->", glob.action, base_exists)
			
			
			if not base_exists:
				# 'Desktop Action', None, None, None, None
				glob.context.append([glob.action, None, None, None, None])
				
				


			index = [ index for index, item in enumerate(glob.context) 
			if glob.action  == item [0] and item [1] == action_key and item [-2] == key]
			
			# index: base_key_exists
			# base key isexists?
			# print("base key isexists ->", action_key, base_key_exists)
			

			
			if not index:
				glob.context.append([glob.action, action_key, glob.LANGUAGE, key, value])
				
				# < TESTING >
				# desk.action.set(key="Name", value="Test1", action_key="X")
				# desk.action.set(key="Icon", value="Test2", action_key="X")
			
			
			else:
	
				glob.context [index [0]] [-1] = value
			
			
		else:
			

			
			if not glob.context:
				glob.context.append([glob.entry, None, None, None, None])
				# 'Desktop Entry', None, None, None, None
				
				
			
			if not index is not None:
				# Thu Feb 29 11:40:15 CST 2024

				# <tested>
				# call: desk.entry.set(key="Name", value="Test")
				
				
				print("---- index", index)
				
				# for index in range(glob.context.index([ glob.entry ]+ [None] * 4), 100):
					# max one double zero lines
					
				#	if not glob.entry in glob.context[index]:
				#		index = index -1
				#		break
				# tail = test.index_tail(glob.entry)
				
				
				# index+1 -> testing ...
				
				tail = [ index + 1 for index in range(glob.context.index([ glob.entry ]+ [None] * 4), len(glob.context)) 
		if base in glob.context [index] ] [-1]
				print("---- tail ", tail)
				
				glob.context.insert(tail, [ glob.entry, None, glob.LANGUAGE, key, value ] )
				# ['Desktop Entry', None, 'en_US', 'Exec', '/usr/share/myapp/test']

				""" not found key """
			
			else:
				

				glob.context[index][-1] = value
				""" found key """
				
				
		return test
	def file_update():
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					test.content+= "[%s]\n" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							test.content+= "%s=%s\n" % (key, value)
					else: 
						test.content+= "%s[%s]=%s\n" % (key, lang, value)

		tempfile, name = au.temp.filetouch(test.content)
		tempfile.pkexec.mv2(glob.path)
		
		return glob
		
def applications():

	import os
	
	
	# global path_desktop_items
	path_desktop_items = [ os.path.realpath(item) 
	for item in os.listdir(glob.appdir) ]


	dictionary = {}
	
	for item in path_desktop_items:
		
		name, extension = os.path.splitext(os.path.basename(item))
		if ".desktop" != extension:
			continue
		
		dictionary [name] = '%s/%s%s' % (glob.appdir, name, extension)
		""" 'path':'%s/%s%s' % (glob.appdir, exec, extension) """
		
	
	return dictionary

	
class desktop:

	def path(name):
		
		appdir = applications()
		""" appdir: usr/share/applications """
		
		return appdir.get(name)
		
class desk:
	
	# content = ""
	
	class entry:
		
		def __getindex(key):
			try:
				return [ index for index, item in enumerate(glob.context) 
				if ["%s" % glob.entry, None, glob.LANGUAGE, key] == item [0:4] ] [0]
				""" group disinda kalan """
			except:
				return None
				
		
		def group(key, value):
			
			
			
			return test.group(key, value, desk.entry)
			
			# export.test.group(key, value, desk.entry)
			# key, value, base=None, index=None, action=None


		def set(key, value=None):
			index = desk.entry.__getindex(key)
			return test.string(key=key, value=value, index=index)

				
		def add(key, value):
			return desk.entry.set(key, value)
		def pop(key):
			
			index = [ index for index, item in enumerate(glob.context) 
			if item and glob.entry == item [0] and key == item [-2]  ]
			# ['Desktop Entry', None, 'en_US', 'Version', '1.0'], [], []
			# factoring: and not item
			# sugar: soldan saga dogru calisiyor
			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				

			return glob
			
		def popitem(key):
			return desk.entry.pop(key)
			
		def get(key):
			
			getext =  [ item for item in glob.context 
			if ["%s" % glob.entry, None, glob.LANGUAGE, key] == item [0:4]] 
			# ['Desktop Entry', 'en_US', 'Icon', 'bix']
			
			if getext:
			
				base, base_key, lang, key, value = getext [0]  if getext else [None]*4
				# [None]*4 -> defactoring
				# when not found key
			
				return value
	class action:
		
		def __getindex(key, action_key):
			# key: Name
			# action_key: X
			# 'Desktop Action', 'X', 'en_US', 'Name', 'deneme'
			# TESTING
			
			
			try:
				return [ index for index, item in enumerate(glob.context) 
				if ["%s" % glob.action, action_key, glob.LANGUAGE, key] == item [0:4] ] [0]
				""" group disinda kalan """
			except:
				return None
				
				
		def group(key, value, action_key):
			#(key, value, action_key)
			
			return test.group(key, value, desk.action, action_key)
			
			# export.test.group(key, value, desk.action)
			# key, value, base=None, index=None, action=None
			
			
		def set(key, value, action_key):
			
			index = desk.action.__getindex(key, action_key)
			print("__getindex", index)
			
			return test.string(key, value, base=None, index=index, action=action_key)
			# export.test.string(key, value, base=None, index=index, action=action)
			
			"""
			
			[Desktop Entry]
			Exec=/usr/share/myapp/test
			Name=myapp
			Icon=face-heart

			
			"""
			
			return glob
			
		def add(key, value, action_key):
			return desk.action.set(key, value, action_key)

		def pop(key, action_key):
			
			index = [ index for index, item in enumerate(glob.context) 
			if item and glob.action == item [0] and item [1] == action_key and key == item [-2]  ]
			# ['Desktop Entry', None, 'en_US', 'Version', '1.0'], [], []
			# defactoring: and not item
			# sugar: soldan saga dogru calisiyor
			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				

			return glob
		def popitem(key, action_key):
			return desk.action.pop(key, action_key)
			
		def getitem(key, action_key):
			# desk.action.get("Name", action_key="X")
			
			getext =  [ item for item in glob.context 
			if item and ["%s" % glob.action, action_key, glob.LANGUAGE, key] == item [0:4]] 
			# ['Desktop Action test', 'en_US', 'Icon', 'geany']
			
			return getext [0][-1] if getext else None
		def get(key, action_key):
			return desk.action.popitem(key, action_key)

class setitem:

		
	def __setitem__(self, key,value):
		desk.entry.set(key=key, value=value) 
from shortcuts import Key
class getitem:

		
	def getitem( key):
		return Key.getitem(key).text
class Base(getitem):
	Entry = setitem()
	
	entry = desk.entry
	action = desk.action
	
	# FILO=FILO()
	
	# getitem=Key
	
	# xyz=[]
	# getitem =  lambda d : Key.getitem(d)


	def update_file():
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					test.content+= "[%s]\n" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							test.content+= "%s=%s\n" % (key, value)
					else: 
						test.content+= "%s[%s]=%s\n" % (key, lang, value)

		tempfile, name = au.temp.filetouch(test.content)
		tempfile.pkexec.mv2(glob.path)
		
		return glob
	
	# def set():
	#	for key, value in Base.Entry.items():
	#		desk.entry.set(key=key, value=value)
	#	return export.test
		
def create():
	""" calisma klasorunde kisayol olustur """

def __getitems(line):
	
	# line = line.strip()
	key, val = line.split(chr(61))
	
	if chr(91) in key :
		return [ key [key.index(chr(91))+1: key.index(chr(93)) ], key [0: key.index(chr(91))], val ] 
		# ['tr', 'Name', 'bix']
	else:
		return [ glob.LANGUAGE, key, val ]
		# ['en_US', 'Categories', 'GTK;GNOME;Utility;']

def Content(name):
	
	del glob.context [:]
	
	glob.path = desktop.path(name) 
	""" glob.path: /usr/share/applications/X.desktop """
	
	
	for line in open(glob.path) if glob.path else []:
		line = line.strip()
		
		if line:
	
			if line.startswith("#"):
				continue
		
			if line.startswith(chr(91)):
				
				item = chr(32).join(line [1: line.index(chr(93))].split())
				""" Desktop Entry """
				
				
				if item != glob.entry:
					x = item.split() 
					
					glob.select=chr(32).join(x[0:2])
					basekey = x [-1]
					
					
				else:
					glob.select=item
					
				glob.context.append([glob.select]+[None]*4)
				""" Desktop Action """
				
				
			else:
				
				item = __getitems(line)
				test = [ None if glob.select == glob.entry else basekey ]+item
				
				glob.context.append([ glob.select ] + test)
				
				if glob.select == glob.entry:
						setattr(glob.Key, test [2], test [3])
						
						
	return Base
	
def print_content():
	
	for items in glob.context:
	
		if items:
			
			print(chr(32).join([ str(item) for item in items ]))
		
			base, action_key, lang, key, value = items
			
			
			if action_key:
				

				if not "[%s %s]" % (base, action_key) in glob.content:
					glob.content += "[%s %s]\n" % (base, action_key)
				
				if lang == glob.LANGUAGE:
					glob.content += "%s=%s\n" % (key, value)
				else:
					glob.content += "%s[%s]=%s\n" % (key, lang, value)
				
				
			
			else:
				if items [1:] == [None] * 4:
					
					if base == glob.action:
						continue
					else:
					
						glob.content += "[%s]\n" % base

				else:
					if lang == glob.LANGUAGE:
						glob.content += "%s=%s\n" % (key, value)
					else:
						glob.content += "%s[%s]=%s\n" % (key, lang, value)
						
	return glob.content
	# Wed Feb 28 21:13:50 CST 2024

	

	
	
	
	
	
	
	
	
	
	
	
