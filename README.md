# osplaces_geocoder
This plugin uses OS Places API to search for freetext in their AddessBase Premium product, more specifically Local Authority Based Addresses (LPI) stored in the AddressBase Premium. 
Bulk of the code is a sloppy lift and shift job of the Nominatmim Locator Filter Plugin Generated by Richard Duivenvoorde: https://qgis.nl/2018/05/16/english-coding-a-qgslocator-plugin/?lang=e. 
In fact, it includes some redundant code/comments that Richard had left behind. Note that only top 100 hits are returned so likelihood of satisfactory geocoding depends upon your search string. In other words, try a variety of combination..

**INSTALLATIONS:**

**Requirements:**
1. OS Data Hub API Key for OS Places API (https://osdatahub.os.uk/docs/places/overview)
2. [osplaces.zip](https://github.com/gitsnewbie/osplaces_geocoder/blob/main/osplaces.zip) - This is the "osplaces" geocoder plugin file
3. "Plugin Reloader" Plugin - This plugin will be needed to recompile the plugin once you have added the API Key

**Steps:**
1. Download the [osplaces.zip](https://github.com/gitsnewbie/osplaces_geocoder/blob/main/osplaces.zip) and Install the "osplaces" plugin in QGIS using the Zip option
2. Browse to the python\Plugins\osplaces folder, and update the osplaces_geocoder.py code by adding the API key in line 72, save the changes.
3. Recompile the "osplaces" using the "Plugin Reloader" in QGIS

**HOW TO USE:**
1. In the locator bar on the bottom left of QGIS, type osplaces followed by a space then search string, and then another space. If a search string successfully yields any hits, then a list of top 100 matching hits will appear. 
2. Select the desired address from the list, and double-click on the address.
3. Map would scale to 1:2500, and then pan to the location of the address, and a pin and annotation will indicate the location of the address.
