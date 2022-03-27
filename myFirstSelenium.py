from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://goodinfo.tw/tw/index.asp")
#assert("Python" in driver.title)

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("2002")
elem.send_keys(Keys.RETURN)

assert("No results found." not in driver.page_source)
#driver.close() # 關閉browser

