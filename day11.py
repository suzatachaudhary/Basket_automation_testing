#this is just an example of code as i didn't find any website to perform these logic on.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 
import os

driver=webdriver.Chrome()
driver.get("url link")

#dropdown using select class but it is only for html based
dropdown = Select(driver.find_element(By.ID,"country"))
dropdown.select_by_visible_text("Nepal")
dropdown.select_by_value("2")
dropdown.select_by_index(0)

#dropdown for js,react,bootsrap should be particulary element based find element click again click inside it.
driver.find_element(By.CSS_SELECTOR, ".dropdown").click()
driver.find_element(By.XPATH, "//li[text()='Nepal']").click()

##keyboard Actions
from selenium.webdriver.common.keys import Keys

search = driver.find_element(By.ID,"search")
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)

search.send_keys(Keys.ENTER)
search.send_keys(Keys.TAB)
search.send_keys(Keys.CONTROL, "a")
search.send_keys(Keys.CONTROL, "v")
search.send_keys(Keys.PAGE_DOWN)

##Scrolling 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #bottom
element = driver.find_element(By.ID,"footer")
driver.execute_script("arguments[0].scrollIntoView()", element) #specific element
driver.execute_script("window.scrollBy(0, -500);") #scroll up

#upload file <input type="file">
driver.find_element(By.ID,"fileUpload").send_keys("C:/path/file.png")

#download verification
assert os.path.exists("C:/Downloads/book.pdf")

#drag and drop
from selenium.webdriver import ActionChains

source = driver.find_element(By.ID,"drag")
target = driver.find_element(By.ID,"drop")

ActionChains(driver).drag_and_drop(source, target).perform()



