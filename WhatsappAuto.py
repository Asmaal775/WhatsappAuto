
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
while True :
    print('Teeest Looop')
    CurrentTime = datetime.now().time()
    Actual_Time = CurrentTime.strftime("%H:%M:%S")
    Static_Time = '09:27:00'
    if (Actual_Time == Static_Time) :
        print('Teeest')
        options = Options()
        #options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        #options.add_argument("user-data-dir=C:\\Users\\AsmaAlghamdi\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\b720wnma.default-release\\cache2\\entries")
        #PATH = "C:/Users/AsmaAlghamdi/Downloads/geckodriver-v0.29.0-win32/geckodriver.exe"
        #driver = webdriver.Firefox(options=options,executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
        options.add_argument("--user-data-dir=chrome-data")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome('C:\\Users\\AsmaAlghamdi\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)
        driver.maximize_window()
        driver.get('https://web.whatsapp.com')
        time.sleep(20)
        driver.find_element_by_xpath("//*[@title='Mom']").click()
        #driver.find_element_by_class_name('_1awRl')
        excuse = ['هلا يمه أنا تمام انتي كيفك', 'هلا والله', 'هلا أنا في الدوام', 'هلا بكلمك اذا خلصت', 'صباح الخير انا في الدوام']
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))).send_keys(random.choice(excuse))
        #driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_2Ujuu']"))).click()
        time.sleep(10)
        driver.close()
        continue      
    else :
        print('Not lucky time')
        continue   
