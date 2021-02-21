# WhatsappAuto
Auto WhatsApp sending messages in specific time by chrome and Firefox browsers 

# Requirmants
1. Python
https://www.python.org/downloads/ 
2. IDE for example VS Code
https://code.visualstudio.com/download
3. Broswer (Chrome or FireFox)
4. WhatsApp
https://www.whatsapp.com/ 
# Steps
Clone the files and run it by pip or in VS code , you need to download :
1. chromedriver.exe for chrome and locat it in rememmbering path
https://chromedriver.chromium.org/downloads
2. geckodriver.exe for FireFox and locat it in rememmbering path
https://github.com/mozilla/geckodriver/releases
# Import
import time
from selenium import webdriver
#from selenium.webdriver.Firefox.options import Options
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import random
