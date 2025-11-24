'''Multiple books → add 2–3 books in a loop instead of just one.

Dynamic selection → pick books based on category, price, or availability.

Mouse interactions → hover menus to select category/subcategory.

Basket validation → verify all added books and total price.

Optional pop-ups or edge cases → like removing a book, or checking empty basket messages.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

#launching the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#opening the website
driver.get("https://selenium1py.pythonanywhere.com/")

#homepage validation
assert "Oscar" in driver.title,"Homepage title is incorrect"

#Select Multiple books dynamically
books=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod h3 a")))

# We'll add first 2 books to basket
#so let's use for loop
book_titles=[]

for i in range(2):
  book=books[i]
  book_title=book.get_attribute("title")
  book_titles.append(book_title)
  book.click()
  
  # 4️⃣ Validate product page
  product_title=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.product_main h1"))).text

  assert book_title==product_title,f"product title doesn't match {book_title} vs {product_title}"

  #Add to Basket
  add_basket=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.btn.btn-lg.btn-primary.btn-add-to-basket")))
  add_basket.click()

  #confirmation message
  success_msg=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.alertinner")))
  assert book_title in success_msg.text,"Success message doen't contain book detail"

  #go back to home page
  driver.get("https://selenium1py.pythonanywhere.com/")
  books=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod h3 a")))
  
#Go to basket and validate
view_basket=driver.find_element(By.PARTIAL_LINK_TEXT,"View basket")
view_basket.click()

basket_elements=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".basket-items h3 a")))
assert len(basket_elements)==2,f"expected 2 items in basket ,got {len(basket_elements)} in basket"

#validate title of elements in basket
for i, item in enumerate(basket_elements):
    assert item.text.strip() == book_titles[i].strip(), f"basket title mismatched for item {i+1}"

  
Screenshot_path="day6_sc.png"
driver.save_screenshot(Screenshot_path)
assert os.path.exists(Screenshot_path),"given path is not correct"
print("Everything is working fine")

driver.quit()
  
  





  