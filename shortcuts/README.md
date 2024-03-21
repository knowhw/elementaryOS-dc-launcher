

## Installation
~~~bash
git clone https://github.com/knowhw/tool-desktop-shortcut.git
~~~

## Sample Work File [/usr/share/applications]
~~~
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

~~~


## #Tool usage

~~~python

~~~


```python

from desktop import content

# desk = content("myapp")

# solutions 1

# desk.Entry ["Icon"] = "face-heart"
# desk.Entry ["Name"] = "myapp"

# desk.Entry ["Exec"] = "/usr/share/myapp/test"

# test = desk.set()

# for item in test.print_file():
#		print(item)


# solutions 2

# desk.entry.set(key="Name", value="myapp")
# desk.entry.set(key="Exec", value="/usr/share/myapp/test")

# test = desk.action.set(key="Name", value="test", action="X")


# for item in test.print_file():
#	print(item)



# solutions 3

# desk.Entry ["Icon"] = "face-heart"
# desk.Entry ["Name"] = "myapp"

# desk.action.set(key="Name", value="test", action="X")

# test = desk.set()


# for item in test.print_file():
#		print(item)





# solutions 4

# desk.entry.set(key="Name", value="myapp")
# test = desk.action.set(key="Icon", value="myapp", action="X")

# desk.entry.pop("Name")


# for item in test.print_file():
#		print(item)












```



