from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://goodinfo.tw/tw/index.asp")
#assert("Python" in driver.title)

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("2002")
elem.send_keys(Keys.RETURN)

assert("No results found." not in driver.page_source)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='link_blue']"))
    )
    print("here")
finally:
#    driver.quit()
    web_element=driver.find_element_by_link_text("股利政策")
    web_element.click()


#driver.close() # 關閉browser

