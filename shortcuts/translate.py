# https://youtu.be/IvXphJ9Ouxc?t=4110
# pip install translate


from deskop import glob
from itertools import chain



		
		
def __set(base, lang, key, value):
	# Mon Feb 12 01:59:13 CST 2024
	index = [  index for index, item in enumerate(glob.context) 
	if  item [0] == base and item [1] == glob.LANGUAGE and item [2] == key ]
	
	
	
	glob.insert(index [0],[base, lang, key, value])
	
	
	for item in glob.context:
		yield test.file_print(item)
	
	# return glob.context
	


def __translate(base, lang, key, value):
	
	
	googleapis = "/translate_a/single?client=gtx&dt=t&"
	test = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, lang, value)
	
	response = glob.loads(glob.urllib.request.urlopen(test) .read()) [-9][-1]
	# Merhaba', 'Hello', None, None, 10
	
	return __set (  base, lang, key, response [0] )  
	
	"""
	 
	[Desktop Entry]
	Type=Application
	Version=1.0
	Name=Geany
	Name[tr]=Geany
	Exec=geany %F
	Icon=geany
	Terminal=false
	Categories=GTK;Development;IDE;
	StartupNotify=true
	Keywords=Text;Editor;
	
	"""
def __getindex(index):
	return index[0:len(index)+1:len(index)-1]
	""" __getindex: return head-tail"""
	
def group(base, key, value):

	# print(base.__name__, key, value)
	
	"""
	
	[Desktop Entry]
	Type=Application
	Version=1.0
	Name=Geany
	Exec=geany %F
	Icon=geany
	Terminal=false
	Categories=GTK;Development;IDE;
	StartupNotify=true
	Keywords=Text;Editor;
	
	"""


	for lang in [ item.get(glob._) for item in glob.lang.findall('name') if item.get(glob._) ]:
		test = [getattr(glob, base.__name__), lang, key]
	
		
		exists = [  item for item in glob.context if item [0:3] == test ]
		
		if not exists:
			
			glob.items.append(test)
			
			"""
			
			Comment[az]=az-AUZEF
			Comment[ay]=ay-AUZEF
			Comment[as]=as-AUZEF
			Comment[hy]=hy-AUZEF
			Comment[mk]=ar-AUZEF
			Comment[tr]=Test
			
			"""
		
	return [ __translate(base, lang, key, value) for base, lang, key in glob.items ]
	# return glob.context



class language:
	
	def group(base, key, value):

		# print(base.__name__, key, value)
		
		"""
		
		[Desktop Entry]
		Type=Application
		Version=1.0
		Name=Geany
		Exec=geany %F
		Icon=geany
		Terminal=false
		Categories=GTK;Development;IDE;
		StartupNotify=true
		Keywords=Text;Editor;
		
		"""


		for lang in [ item.get(glob._) for item in glob.lang.findall('name') if item.get(glob._) ]:
			test = [getattr(glob, base.__name__), lang, key]
		
			
			exists = [  item for item in glob.context if item [0:3] == test ]
			
			if not exists:
				
				glob.items.append(test)
				
				"""
				
				Comment[az]=az-AUZEF
				Comment[ay]=ay-AUZEF
				Comment[as]=as-AUZEF
				Comment[hy]=hy-AUZEF
				Comment[mk]=ar-AUZEF
				Comment[tr]=Test
				
				"""


