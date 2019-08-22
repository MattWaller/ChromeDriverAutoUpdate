from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options -- OPTIONAL
#from selenium.common.exceptions import NoSuchElementException -- OPTIONAL
from ChromeVersion import chrome_browser_version

driverName = "\\chromedriver.exe"

# defining base file directory of chrome drivers
driver_loc = # enter your file path here PATH

currentPath = driver_loc + chrome_browser_version + driverName 



executable_path = currentPath
chrome_options = Options()

#chrome_options.add_argument("--incognito") -- OPTIONAL

driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
