from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import csv
import json



with open('modified_json_dump.json') as json_file:
    data=json.load(json_file)

# print(data[482]['484'])




i=2
start=0
end=400

driver_path = r"C:/chromedriver"
opt = Options()
opt.add_argument("--disable-notifications")
ser = Service(driver_path)
driver = webdriver.Chrome(service=ser, options=opt)


driver.get("https://www.instagram.com/accounts/login/")
sleep(10)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("raju939521")
sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("@Sk@As1f@Iqba1@")
sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(20)
# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window 
driver.switch_to.window(driver.window_handles[1])
sleep(5)

new_data=[]
for item in data[start:end]:
    try:
        img_link=''
        yt_link=item[f"{i}"]
        driver.get(yt_link)
        sleep(5)
        image=driver.find_elements(By.XPATH,"//img[@class='_aadp']")#private   in public no
        # sleep(2)
        if image==[]:
            image=driver.find_elements(By.XPATH,"//img[@class='_aa8j']")[0]
            # sleep(2)
        else:
            image=image[0]
        sleep(1)
        img_link=image.get_attribute('src')   
    except:
        img_link='NA' 
    new_data.append({i:img_link})
    i+=1
    
    
with open('new_modified_json_dump.json','w') as modified_json_file:
    json.dump(new_data,modified_json_file,indent=2)

driver.close()
