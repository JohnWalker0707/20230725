from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path='\chromedriver-win64\chromedriver.exe'


driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com.tw/')




driver.close()