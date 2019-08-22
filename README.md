# ChromeDriverAutoUpdate
Automatically update and deploy chromedriver updates


Place files in os path that can run python for deployment of automated download of chromedriver.

Set up scheduler to run daily every hour stagged slightly behind google update task machine. 

Must have a current version of chromedriver in order to set script up.

REQUIRED LIBRARIES: 
  pywin32
  selenium
  
  

Be sure to update the following variables in the scripts: 

chrome_browser --> location where your normal chromebrowser exists [ChromeVersion.py] -- line 3

# for organizational purposes I set up a folder named ChromeDriver in my python directory.
driver_loc --> file location where you wish to store all your new versions of chromedriver [ChromeDriverAutomation.py] -- line 10


fileName --> your file download path [ChromeDriverAutomation.py] -- line 72

If you notice any errors please notify me and I will make the adjustments.

Cheers!
