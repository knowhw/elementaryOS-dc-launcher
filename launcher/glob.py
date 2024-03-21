
import os
HOME=os.getenv("HOME")
# glob.LANGUAGE


null="rm %s/%s.dockitem > /dev/null 2>&1"
# glob.null

dockdir='%s/.config/plank/dock1/launchers' % HOME
# glob.dockdir


dockitems=[]
push=dockitems.append
# glob.dockitems

diff=[]

appdir='/usr/share/applications'
