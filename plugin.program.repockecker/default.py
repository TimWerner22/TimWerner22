#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcgui,requests

urls = ["HSK Server 1*http://hsk.goip.de/hsk-repo/de/repository.hsk.kodiaddons/repository.hsk.kodiaddons-1.0.1.zip",
        "HSK Server 2*http://v36557.1blu.de/files/public-docs/hsk/17/kodi_backup.zip",
	    "Kodimans Public Repo*https://github.com/Kodiman1402/repository.kodiman.public-1.0.2",
		"Guidos SkinBase16*https://github.com/kaffepausse71/skinbase16/",
		"Guidos SkinBase17*https://github.com/kaffepausse71/skinbase17/",
		"Guidos SkinBase18*https://github.com/kaffepausse71/skinbase18/",
		"Exodus Repo*https://github.com/lastship/ExodusRepo/raw/master/addons.xml",
		"Superrepo*http://srp.nu",
		"Membrane Repo*https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/membrane-xbmc-repo/repository.membrane.xbmc-plugins.zip",
		"Metal Kettles Repo*http://kodi.metalkettle.co/"]
	   
output = ''		
for url in urls:
    request = requests.get(url.split('*')[1])
    if request.status_code == 200:
        output += url.split('*')[0] + ' = [COLOR green]online[/COLOR]' + '\n'
    else:
        output += url.split('*')[0] + ' = [COLOR red]offline[/COLOR]' + '\n'

xbmcgui.Dialog().textviewer('SERVER TESTER', output.decode("iso-8859-1", "ignore"))
		
		
		

	