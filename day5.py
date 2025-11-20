from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

#launching a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open the website
driver.get("https://selenium1py.pythonanywhere.com/")

#Assertion of title
assert "Oscar" in driver.title, "Homepage title is incorrect"

#check for first book
first_book=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "article.product_pod h3 a")))
first_book_name=first_book.get_attribute("title")
first_book.click()

# Assertion 2: Confirm product page opened and title matches
product_title=driver.find_element(By.CSS_SELECTOR,"div.product_main h1").text
assert first_book_name==product_title, "product title doesn't match"

#Add to basket
add_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
add_button.click()

#assertion 3: check if success message appear
success_msg=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.alertinner")))
assert "has been added to your basket" in success_msg.text

#view basket
view_basket=driver.find_element(By.PARTIAL_LINK_TEXT,"View basket")
view_basket.click()

#assertions check if view basket url contains basket
assert "basket" in driver.current_url, "Basket page didnot match"

driver.save_screenshot("dayfive_screenshot.png")
assert os.path.exists("dayfive_screenshot.png"),"given screenshot path doesn't exist"

driver.quit()

