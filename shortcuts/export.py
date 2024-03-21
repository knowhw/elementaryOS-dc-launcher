
from au.desktop import glob
import au.temp

class test:		
	
	content = ""
	
	
	def print_file():
		
		arr = []
		
		"""
		
		[Desktop Entry]
		
		Name=Discord
		Exec=/usr/share/discord/Discord
		Icon=discord
		Type=Application
		Categories=Network;InstantMessaging;
		Path=/usr/bin
		
		[Desktop Action X]
		Name=test
		
		"""
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					yield "[%s]" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							yield "%s=%s" % (key, value)
					else: yield "%s[%s]=%s" % (key, lang, value)
				
	def group(key, value, base):
		
		
		base = getattr(glob, base.__name__)
		
		
		gl = [  item  for item in glob.context 
		if item [0:3] == [ base, glob.LANGUAGE, key ] ]
		# glob.LANGUAGE isExists
		
		
		
		if not gl: glob.insert( glob.index.entry+1, [ base, glob.LANGUAGE, key, value ])
		# glob.LANGUAGE not Exists
		
		"""
		
		[Desktop Entry]
		Categories=Network;InstantMessaging;
		Type=Application
		Path=/usr/bin
		Icon=test
		Name[yo]=test
		Name[zu]=myapp
		Name[yi]=מיין אַפּ
		Name[xh]=myapp
		Name=test

		[Desktop Action X]
		name=test
		
		
		"""
		
		index = [  index for index, item in enumerate(glob.context) 
		if  item [0] == base and item [1] == glob.LANGUAGE and item [2] == key ] [0]
		# index: gl.index


		
		langs = [ item.get(glob._) 
		for item in glob.lang.findall('name') 
		if item.get(glob._) ]
		

		for lang in langs: 
			
			# 132 world languages
			
			"""
			
			[mk]=test
			[hi]=test
			[lb]=test
			[lg]=test
			[lt]=test
			[ln]=test
			[lv]=test
			[la]=test
			[lo]=test
			[ky]=test
			
			..
			..
			..
			
			"""
			
			items = [  item for item in glob.context 
			if item [0:3] == [ base, lang, key ] ]
			
			
			if not items:
					
				googleapis = "/translate_a/single?client=gtx&dt=t&"
				query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, lang, value)
				
				res = glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0]
				# res: value
				
				print(lang, key, res)
				
				glob.insert( index, [ base, lang, key, res ])
				

				
		return test

	def string(key=None, value=None, base=None, index=None, action=None):

		if action:
			
			action = "%s %s" % (glob.action, action)
			
			
			if not index:
				
				
				base = [action, None, None, None]
				# base: Desktop Action test None None None
				glob.extend([base, ["%s" % action, glob.LANGUAGE, key, value]])
				# base yok
			else:

				
				exists = [ index for index, item in enumerate(glob.context) 
				if action  == item [0] and item[2] == key ]
				# base var mi?
				
				
				
				if exists:
					glob.context [exists [0]] [-1] = value
					# base var, key var
				else:

					# head, tail = min(index), max(index)
					glob.insert(min(index)+1, [action, glob.LANGUAGE, key, value])
					# base var key yok
					
				
		else:
			
			if not index is not None:
				items = glob.entry, glob.LANGUAGE, key, value
				
				glob.context.insert(glob.index.entry + 1, list(items) )
				# tuple: [['Desktop Entry', None, None, None], ('Desktop Entry', 'en_US', 'Name', 'myapp')]
				# list: defactoring
				
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
		
