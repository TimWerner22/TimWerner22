#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcgui,requests

urls = ["HSK Server 1*http://hsk.goip.de/hsk-repo/de/repository.hsk.kodiaddons/repository.hsk.kodiaddons-1.0.1.zip"]
       ["Netzkino*http://www.netzkino.de/"]
	   
output = ''		
for url in urls:
    request = requests.get(url.split('*')[1])
    if request.status_code == 200:
        output += url.split('*')[0] + ' = online' + '\n'
    else:
        output += url.split('*')[0] + ' = offline'	 + '\n'

xbmcgui.Dialog().textviewer('SERVER TESTER', output.decode("iso-8859-1", "ignore"))
		
		
		

	