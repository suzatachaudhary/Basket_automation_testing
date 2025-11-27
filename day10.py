#multiple nested iframe
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")


# Switch to top frame
driver.switch_to.frame("frame-top")

# Switch to middle frame
driver.switch_to.frame("frame-middle")

middle_text = driver.find_element(By.ID, "content").text
print("Middle frame text:", middle_text)

driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
bottom = driver.find_element(By.TAG_NAME, "body").text
print("Bottom frame text:", bottom)

driver.switch_to.default_content()

#Automatically detect which iframe contains an element

iframes = driver.find_elements(By.TAG_NAME, "iframe")

for index, frame in enumerate(iframes):
    driver.switch_to.frame(frame)
    try:
        driver.find_element(By.ID, "tinymce")
        print(f"Found tinymce inside iframe index {index}")
        break
    except:
        driver.switch_to.default_content()
