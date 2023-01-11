import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('D:\\044\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://sc.npru.ac.th/")
time.sleep(10)
driver.close()