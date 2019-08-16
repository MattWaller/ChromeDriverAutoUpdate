from getFileProperties import *

chrome_browser = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'


cb_dictionary = getFileProperties(chrome_browser)

chrome_browser_version = cb_dictionary['FileVersion'][:2] 


nextVersion = str(int(chrome_browser_version) +1)

lastVersion = str(int(chrome_browser_version) -1)
