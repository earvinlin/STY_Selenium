from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
#profile.set_preference("browser.download.dir", 'PATH TO DESKTOP')
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(firefox_profile=profile)
#driver = webdriver.Firefox()

driver.get("https://goodinfo.tw/tw/index.asp")
#assert("Python" in driver.title)

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("5388")
elem.send_keys(Keys.RETURN)

#assert("No results found." not in driver.page_source)
"""
### 下面寫的不能用…不知為何??
try:
#   如果驗證任何元素的存在，檢查元素期望
#    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()
    element = WebDriverWait(driver, 20, 0.5).until(
        EC.presence_of_element_located(By.LINK_TEXT('股利政策'))
    )
    print("here")
    web_element=driver.find_element_by_link_text('股利政策')
    web_element.click()
finally:
#    driver.quit()
    web_element=driver.find_element_by_link_text('股利政策')
    web_element.click()
    print("Finished!!")
"""
# Can work
driver.implicitly_wait(10) # seconds
web_element=driver.find_element_by_link_text('股利政策')
web_element.click()

driver.implicitly_wait(15) # seconds
#elem2 = driver.find_element_by_xpath("//button[text()='匯出XLS']")
button = driver.find_element_by_xpath("//input[@type='button' and @value='匯出XLS']")
driver.execute_script("arguments[0].click();", button)
#button.click()

#driver.close() # 關閉browser

