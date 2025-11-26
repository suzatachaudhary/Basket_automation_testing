#today here we are learning about multiple window handling .so the book store app doesn't have multiple window links so here we are going to use a different open demo website.
#lets start.
'''so we have to store the main window then open a link then switch to new window after then close new  window and switch back to main window.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

main_window=driver.current_window_handle
link=driver.find_element(By.LINK_TEXT,"Click Here")
link.click()

for win in driver.window_handles:
  if win != main_window:
    driver.switch_to.window(win)
    break
  
print(driver.title)
driver.close()
driver.switch_to.window(main_window)
print(f"Back to main {driver.title}")



