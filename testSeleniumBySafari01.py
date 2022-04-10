from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://goodinfo.tw/tw/index.asp")
#assert("Python" in driver.title)

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("2002")
elem.send_keys(Keys.RETURN)

# 這種寫法，有時侯會因為網頁載入太慢(>10秒)而失敗
driver.implicitly_wait(10)
web_element=driver.find_element_by_link_text('股利政策')
web_element.click()

#assert("No results found." not in driver.page_source)

#driver.close() # 關閉browser

