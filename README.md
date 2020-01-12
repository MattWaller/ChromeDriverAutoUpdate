# ChromeDriverAutoUpdate
Automatically update and deploy chromedriver updates


Place files in os path that can run python for deployment of automated download of chromedriver.

Set up scheduler to run daily every hour slightly behind google update task machine. 

Must have a current version of chromedriver in order to set script up.

REQUIRED LIBRARIES: or Pip install from requirements.txt --> pip install -r requirements.txt
  pywin32
  selenium
  
  

Be sure to update the following variables in the scripts: 

Default downloads new versions to download dir --> if you change your default download dir, you will need to update line 80 of ChromeDriverAutomation.py


Easy run command (from python ide) --> from Driver import driver 




If you notice any errors please notify me and I will make the adjustments.

Cheers!
