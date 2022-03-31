from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# windows path
#driver = webdriver.Chrome(executable_path=r'C:\Users\linea\AppData\Local\Programs\Python\Python38\chromedriver.exe')
# linux path -- unidentified (2022.03.31) --
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get("https://goodinfo.tw/tw/index.asp")
#assert("Python" in driver.title)

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("2002")
elem.send_keys(Keys.RETURN)

assert("No results found." not in driver.page_source)
#driver.close() # 關閉browser

