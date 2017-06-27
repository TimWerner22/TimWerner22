import xbmc,xbmcgui,time,os,shutil,re,urllib2
from libs import kodi
import xbmcaddon
import common as Common
import base64
import maintool
import plugintools
addon_id=kodi.addon_id
kodi.log('STARTING INDIGO SERVICE')


############################
addonPath=xbmcaddon.Addon(id=addon_id).getAddonInfo('path')
addonPath=xbmc.translatePath(addonPath)
xbmcPath=os.path.join(addonPath,"..","..")
xbmcPath=os.path.abspath(xbmcPath)
AddonTitle = 'Indigo'
addonpath = xbmcPath+'/addons/'
mediapath = xbmcPath+'/media/'
systempath = xbmcPath+'/system/'
userdatapath = xbmcPath+'/userdata/'
indisettingspath = xbmcPath+'/userdata/addon_data/plugin.program.indigo/settings.xml'
packagepath = xbmcPath+ '/addons/packages/'
##############################
##############################
oldinstaller =xbmc.translatePath(os.path.join('special://home','addons','plugin.program.addoninstaller'))
oldnotify = xbmc.translatePath(os.path.join('special://home','addons','plugin.program.xbmchub.notifications'))
oldmain = xbmc.translatePath(os.path.join('special://home','addons','plugin.video.xbmchubmaintool'))
oldwiz =  xbmc.translatePath(os.path.join('special://home','addons','plugin.video.hubwizard'))
oldfresh =  xbmc.translatePath(os.path.join('special://home','addons','plugin.video.freshstart'))
oldmain2 = xbmc.translatePath(os.path.join('special://home','addons','plugin.video.hubmaintool'))
##############################
##############################
check = plugintools.get_setting("checkupdates")
addonupdate = plugintools.get_setting("updaterepos")
autoclean = plugintools.get_setting("acstartup")
size_check = plugintools.get_setting("startupsize")
CLEAR_CACHE_SIZE = plugintools.get_setting("cachemb")
CLEAR_PACKAGES_SIZE = plugintools.get_setting("packagesmb")
CLEAR_THUMBS_SIZE = plugintools.get_setting("thumbsmb")

try:
    if os.path.exists(oldinstaller):
        shutil.rmtree(oldinstaller)
    if os.path.exists(oldnotify):
        shutil.rmtree(oldnotify)
    if os.path.exists(oldmain):
        shutil.rmtree(oldmain)
    if os.path.exists(oldwiz):
        shutil.rmtree(oldwiz)
    if os.path.exists(oldfresh):
        shutil.rmtree(oldfresh)
except:
    pass
##############################


if xbmc.getCondVisibility('System.HasAddon(script.service.twitter)'):
    search_string = xbmcaddon.Addon('script.service.twitter').getSetting('search_string')
    search_string = search_string.replace('from:@','from:')
    xbmcaddon.Addon('script.service.twitter').setSetting('search_string',search_string)
    xbmcaddon.Addon('script.service.twitter').setSetting('enable_service','false')

## Start of notifications
if kodi.get_setting('hasran')=='true':
    #kodi.log('Indigo has ran before')
    TypeOfMessage="t"
    (NewImage,NewMessage)=Common.FetchNews()
    Common.CheckNews(TypeOfMessage,NewImage,NewMessage,True)
else:
    kodi.log('Indigo has NOT ran before')

if autoclean == "true":
    maintool.Auto_Startup()

CACHE      =  xbmc.translatePath(os.path.join('special://home/cache',''))
PACKAGES   =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
THUMBS     =  xbmc.translatePath(os.path.join('special://home/userdata','Thumbnails'))

if not os.path.exists(CACHE):
    CACHE     =  xbmc.translatePath(os.path.join('special://home/temp',''))
if not os.path.exists(PACKAGES):
    os.makedirs(PACKAGES)
    
if not CLEAR_CACHE_SIZE == "0":
    if CLEAR_CACHE_SIZE == "1":
        CACHE_TO_CLEAR = 25000000
    if CLEAR_CACHE_SIZE == "2":
        CACHE_TO_CLEAR = 50000000
    if CLEAR_CACHE_SIZE == "3":
        CACHE_TO_CLEAR = 75000000
    if CLEAR_CACHE_SIZE == "4":
        CACHE_TO_CLEAR = 100000000

    CACHE_SIZE_BYTE    = maintool.get_size(CACHE)
    
    if  CACHE_SIZE_BYTE > CACHE_TO_CLEAR:
        maintool.AUTO_CLEAR_CACHE_MB()

if not CLEAR_PACKAGES_SIZE == "0":
    if CLEAR_PACKAGES_SIZE == "1":
        PACKAGES_TO_CLEAR = 25000000
    if CLEAR_PACKAGES_SIZE == "2":
        PACKAGES_TO_CLEAR = 50000000
    if CLEAR_PACKAGES_SIZE == "3":
        PACKAGES_TO_CLEAR = 75000000
    if CLEAR_PACKAGES_SIZE == "4":
        PACKAGES_TO_CLEAR = 100000000

    PACKAGES_SIZE_BYTE    = maintool.get_size(PACKAGES)
    
    if PACKAGES_SIZE_BYTE > PACKAGES_TO_CLEAR:
        if not xbmc.getCondVisibility("Window.isVisible(ProgressDialog)"):
            maintool.AUTO_CLEAR_PACKAGES_MB()

if not CLEAR_THUMBS_SIZE == "0":
    if CLEAR_THUMBS_SIZE == "1":
        THUMBS_TO_CLEAR = 25000000
    if CLEAR_THUMBS_SIZE == "2":
        THUMBS_TO_CLEAR = 50000000
    if CLEAR_THUMBS_SIZE == "3":
        THUMBS_TO_CLEAR = 75000000
    if CLEAR_THUMBS_SIZE == "4":
        THUMBS_TO_CLEAR = 100000000

    THUMBS_SIZE_BYTE    = maintool.get_size(THUMBS)

    if  THUMBS_SIZE_BYTE > THUMBS_TO_CLEAR:
            maintool.AUTO_CLEAR_THUMBS_MB()

if size_check == "true":

    CACHE_SIZE_BYTE    = maintool.get_size(CACHE)
    PACKAGES_SIZE_BYTE    = maintool.get_size(PACKAGES)
    THUMBS_SIZE_BYTE    = maintool.get_size(THUMBS)
    
    if CACHE_SIZE_BYTE >= 100000000:
        choice = xbmcgui.Dialog().yesno(AddonTitle, 'Your Cache is now over 100 MB','This is high and we recommend you clear it now.','Would you like to clear the cache now?', yeslabel='Yes',nolabel='No')
        if choice == 1: 
            xbmc.executebuiltin( "ActivateWindow(busydialog)" )
            maintool.AUTO_CLEAR_CACHE_MB()
            xbmc.executebuiltin( "Dialog.Close(busydialog)" )
            dialog = xbmcgui.Dialog()
            dialog.ok(AddonTitle, "Your cache has been successfully cleared.")                          

    if PACKAGES_SIZE_BYTE >= 1000000000:
        if not xbmc.getCondVisibility("Window.isVisible(ProgressDialog)"):
            choice = xbmcgui.Dialog().yesno(AddonTitle, 'Your Packages folder is now over 1 GB','This is high and we recommend you clear it now.','Would you like to clear the packages now?', yeslabel='Yes',nolabel='No')
            if choice == 1:
                xbmc.executebuiltin( "ActivateWindow(busydialog)" )
                maintool.AUTO_CLEAR_PACKAGES_MB()
                xbmc.executebuiltin( "Dialog.Close(busydialog)" )
                dialog = xbmcgui.Dialog()
                dialog.ok(AddonTitle, "Your packages have been successfully purged.")                           

    if THUMBS_SIZE_BYTE >= 300000000:
        choice = xbmcgui.Dialog().yesno(AddonTitle, 'Your Thumbnails are now over 300 MB','This is high and we recommend you clear it now.','Would you like to clear the thumbnails now?', yeslabel='Yes',nolabel='No')
        if choice == 1: 
            xbmc.executebuiltin( "ActivateWindow(busydialog)" )
            maintool.AUTO_CLEAR_THUMBS_MB()
            xbmc.executebuiltin( "Dialog.Close(busydialog)" )
            dialog = xbmcgui.Dialog()
            dialog.ok(AddonTitle, "Your thumbnails have been successfully cleared.")                            

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds 12 hours is 43200   1 hours is 3600
        if monitor.waitForAbort(1800):
            # Abort was requested while waiting. We should exit
            kodi.log('CLOSING INDIGO SERVICES')
            break