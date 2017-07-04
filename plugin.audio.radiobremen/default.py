#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')

def add_item(url,infolabels,img=''):
    listitem = xbmcgui.ListItem(infolabels['title'],iconImage=img,thumbnailImage=img)
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('http://rb-bremeneins-live.cast.addradio.de/rb/bremeneins/live/mp3/128/stream.mp3',{"title":'Bremen Eins'},os.path.join(addon_path,'resources','icons','20.png'))
add_item('http://rb-bremenvier-live.cast.addradio.de/rb/bremenvier/live/mp3/128/stream.mp3',{"title":'Bremen Vier'},os.path.join(addon_path,'resources','icons','21.png'))
add_item('http://rb-bremennext-live.cast.addradio.de/rb/bremennext/live/mp3/128/stream.mp3',{"title":'Bremen Next'},os.path.join(addon_path,'resources','icons','16.png'))
add_item('http://138.201.251.246/energybremen_192',{"title":'Radio Energy'},os.path.join(addon_path,'resources','icons','22.png'))
add_item('http://rb-bremenzwei-live.cast.addradio.de/rb/bremenzwei/live/mp3/128/stream.mp3',{"title":'Nordwestradio'},os.path.join(addon_path,'resources','icons','23.png'))

xbmc.executebuiltin('Container.SetViewMode(100)')
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#Radio Bremen