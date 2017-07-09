#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcgui,requests

urls = ["HSK Server 1*http://hsk.goip.de/hsk-repo/de/repository.hsk.kodiaddons/repository.hsk.kodiaddons-1.0.1.zip", "HSK Server 2*http://v36557.1blu.de/files/public-docs/hsk/17/kodi_backup.zip","Kodiman Public*https://github.com/Kodiman1402/repository.kodiman.public-1.0.2/blob/master/repository.kodiman.public/repository.kodiman.public-1.0.2.zip"]#usw in der klammer

output = ''		
for url in urls:
    request = requests.get(url.split('*')[1])
    if request.status_code == 200:
        output += url.split('*')[0] + ' = online' + '\n'
    else:
        output += url.split('*')[0] + ' = offline'	 + '\n'

xbmcgui.Dialog().textviewer('SERVER TESTER', output.decode("iso-8859-1", "ignore"))
		
		
		

	