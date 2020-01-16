from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #-- OPTIONAL
#from selenium.common.exceptions import NoSuchElementException -- OPTIONAL

if __package__ is None or __package__ == '':
    from ChromeVersion import chromeVersion
else:
	from .ChromeVersion import chromeVersion
	
chrome_browser_version = chromeVersion()[0]
driverName = "\\chromedriver.exe"

# defining base file directory of chrome drivers
driver_loc = "ChromeDriver\\" #-- ENTER the file path of your exe
# -- I created a separate folder to house the versions of chromedriver, previous versions will be deleted after downloading the newest version.
# ie. version 75 will be deleted after 77 has been downloaded.


currentPath = driver_loc + chrome_browser_version + driverName 



executable_path = currentPath
chrome_options = Options()

#chrome_options.add_argument("--incognito") -- OPTIONAL

driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
