from selenium import webdriver
from selenium.webdriver.common.by import By

#these below imports are for awaits
#from selenium.webdriver.support.ui import WebDriverWait
#from  selenium.webdriver.support import expected_conditions as EC

#these below imports are required because these launches chrome browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#launching a browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#open website
driver.get("https://selenium1py.pythonanywhere.com/")
time.sleep(2)

#click on the first book
first_book=driver.find_element(By.CSS_SELECTOR,"article.product_pod h3 a")
first_book.click()
time.sleep(2)

#add to basket
add_button=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-lg.btn-primary.btn-add-to-basket")
add_button.click()
time.sleep(2)

#partial link text is mainly focused on hyperlink i.e <a 
view_basket = driver.find_element(By.PARTIAL_LINK_TEXT, "View basket")
view_basket.click()
time.sleep(2)

# 5. Take screenshot
driver.save_screenshot("bookstore_cart.png")

# 6. Close browser
driver.quit()






