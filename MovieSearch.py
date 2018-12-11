from selenium import webdriver
import time
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

gekoPath = dir_path + "\\geckodriver.exe"
br = webdriver.Firefox(executable_path=gekoPath)

br.implicitly_wait(15)

br.get('http://www.google.com/')

search = br.find_element_by_name('q')
search.send_keys('blade runner')
search.submit()
time.sleep(5)
print(br.title)