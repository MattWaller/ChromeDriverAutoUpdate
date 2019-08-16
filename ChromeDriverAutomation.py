from ChromeVersion import chrome_browser_version, nextVersion, lastVersion


driverName = "\\chromedriver.exe"

# defining base file directory of chrome drivers
driver_loc = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\ChromeDriver\\"

currentPath = driver_loc + chrome_browser_version + driverName 

# check file directories to see if chrome drivers exist in nextVersion


import os.path

# check if new version of drive exists --> only continue if it doesn't
Newpath = driver_loc + nextVersion

newfileloc = Newpath + driverName
exists = os.path.exists(newfileloc)


print(exists)

if (exists == False):

	#open chrome driver and attempt to download new chrome driver exe file.

	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	import time
	chrome_options = Options()
	executable_path = currentPath
	driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)


	chromeDriverURL = 'https://chromedriver.storage.googleapis.com/index.html?path=' + nextVersion 

	driver.get(chromeDriverURL)

	time.sleep(5)
	# find records of table rows
	table = driver.find_elements_by_css_selector('tr')

	
	# check the length of the table
	Table_len = len(table)

	# ensure that table length is greater than 4, else fail. -- table length of 4 is default when there are no availble updates
	if (Table_len > 4 ):

		# define string value of link
		rowText = table[(len(table)-2)].text[:6]
		time.sleep(1)
		# select the value of the row
		driver.find_element_by_xpath('//*[contains(text(),' + '"' + str(rowText) + '"'+')]').click()
		time.sleep(1)
		#select chromedriver zip for windows 
		driver.find_element_by_xpath('//*[contains(text(),' + '"' + "win32" + '"'+')]').click()

		time.sleep(3)
		driver.quit()
		
		from zipfile import ZipFile
		import shutil


		fileName = r"C:\Users\Administrator\Downloads\chromedriver_win32.zip"


		

		# Create a ZipFile Object and load sample.zip in it
		with ZipFile(fileName, 'r') as zipObj:
		   # Extract all the contents of zip file in different directory
		   zipObj.extractall(Newpath)
		  
		
		# delete downloaded file
		os.remove(fileName)



		# defining old chrome driver location
		oldPath = driver_loc + lastVersion
		oldpathexists = os.path.exists(oldPath)

		if(oldpathexists == True):
			shutil.rmtree(oldPath, ignore_errors=True)


		
exit()
