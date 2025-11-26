'''so here we are going to learn about the Iframe there are some methods of iframe driver.switch_to.frame
the most imp An iframe is an HTML element that embeds another webpage inside the current webpage, creating a separate document that Selenium must switch into before interacting with its elements.''' 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

##first switch to iframe, locate editor clear it and type then switch back to default.
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)

editor=driver.find_element(By.ID,"tinymce")
editor.clear()
editor.send_keys("hey my name is kabeeta chaudhary. Today i am learning iframe selenium")

driver.switch_to.default_content()







