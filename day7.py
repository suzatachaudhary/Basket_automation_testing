from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import(
  NoSuchElementException,
  TimeoutException,
  ElementNotInteractableException,
  ElementClickInterceptedException
  
)
import time
import os

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://selenium1py.pythonanywhere.com/")

#we can also use assert but here we are validating home page with strong waits
WebDriverWait(driver,10).until(EC.title_contains("Oscar"))

#get list of books
books=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod h3 a")))

books_titles=[]
for i in range(3):
  book=books[i]
  title=book.get_attribute("title")
  books_titles.append(title)
  book.click()
  
  #product page validation
  book_title=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.product_main h1"))).text
  assert book_title==title,"product title mismatch"
  
  
  add_buuton=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.btn.btn-lg.btn-primary.btn-add-to-basket")))
  add_buuton.click()
  
  #success message validation
  success_message=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.alertinner"))).text
  assert title in success_message,"success message mismatched"
  
  #Handle any alert pop up
  try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert=driver.switch_to.alert()
    print("Alert text :",alert.text)
    alert.accept()
  except TimeoutException:
    print("No alert appeared")
    
  #Handle modal pop up -HTML based
  try:
    modal = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal"))
        )
    close_btn = modal.find_element(By.CSS_SELECTOR, "button.close")
    close_btn.click()
    print("Modal closed successfully.")

  except TimeoutException:
    print("No modal detected as expected")
    
 # Go back to homepage
    driver.get("https://selenium1py.pythonanywhere.com/")
    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")

# GO TO BASKET AND VALIDATE
try:
    basket_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "View basket"))
    )
    basket_link.click()
except (ElementClickInterceptedException, ElementNotInteractableException):
    print("Basket link not clickable!")

basket_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".basket-items h3 a"))
)

assert len(basket_items) == len(books_titles), "Basket item count mismatched!"

# MATCH TITLES IN ORDER
for i, item in enumerate(basket_items):
    assert item.text == books_titles[i], f"Title mismatch at item {i+1}"

# Screenshot
screenshot = "day7_sc.png"
driver.save_screenshot(screenshot)
assert os.path.exists(screenshot)

print("\n DAY 7 COMPLETED SUCCESSFULLY\n")

driver.quit()