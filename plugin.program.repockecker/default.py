#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcgui,requests

urls = ["synology*http://www.synology-forum.de", "chip*http://www.chip.de/"]#usw in der klammer

output = ''		
for url in urls:
    request = requests.get(url.split('*')[1])
    if request.status_code == 200:
        output += url.split('*')[0] + ' = online' + '\n'
    else:
        output += url.split('*')[0] + ' = offline'	 + '\n'

xbmcgui.Dialog().textviewer('SERVER TESTER', output.decode("iso-8859-1", "ignore"))
		
		
		

	