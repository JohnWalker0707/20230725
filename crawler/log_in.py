from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.add_experimental_option("detach", True)

options.chrome_executable_path='\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(options=options)
driver.get('https://www.pcschoolonline.com.tw/')

btn=driver.find_element(By.CSS_SELECTOR,'#aspnetForm > div.pcschoolonline-activity-2021 > nav > div > button')
btn.send_keys(Keys.ENTER)
time.sleep(1)
btn1=driver.find_element(By.ID,'navbarDropdown-2')
btn1.send_keys(Keys.ENTER)
time.sleep(3)

nameinput=driver.find_element(By.CSS_SELECTOR,'[title="帳號只允許英文字母及數字與『-』、『_』符號的組合，字數介於3到16個字。"]')
# passinput=driver.find_element(By.ID,"tboxPassword")
nameinput.send_keys('DB135132')
# passinput.send_keys('2060707')
# time.sleep(1)
# signinbtn=driver.find_element(By.ID,'LinkButton1')
# signinbtn.send_keys(Keys.ENTER)




time.sleep(1)