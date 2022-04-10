import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設定broser profile(這支程式以firefox為範例，故只適用firefox browser)
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.getcwd())
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

# firefox
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://goodinfo.tw/tw/index.asp")

elem = driver.find_element_by_id("txtStockCode")
#elem.clear()
elem.send_keys("2002")
elem.send_keys(Keys.RETURN)


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
try:
    # 這種寫法，有時侯會因為網頁載入太慢(>10秒)而失敗
    driver.implicitly_wait(10)
    web_element=driver.find_element_by_link_text('股利政策')
    web_element.click()

<<<<<<< HEAD
# 這種寫法，有時侯會因為網頁載入太慢(>10秒)而失敗
driver.implicitly_wait(10)
web_element=driver.find_element_by_link_text('股利政策')
web_element.click()

# 這種寫法，有時侯會因為網頁載入太慢(>15秒)而失敗
# https://stackoverflow.com/questions/57741875/selenium-common-exceptions-elementclickinterceptedexception-message-element-cl
driver.implicitly_wait(15)
button = driver.find_element_by_xpath("//input[@type='button' and @value='匯出XLS']")
driver.execute_script("arguments[0].click();", button)

# 關閉browser
driver.close() 

=======
    # 這種寫法，有時侯會因為網頁載入太慢(>15秒)而失敗
    driver.implicitly_wait(15)
    button = driver.find_element_by_xpath("//input[@type='button' and @value='匯出XLS']")
    driver.execute_script("arguments[0].click();", button)
finally:
    # 關閉browser
    driver.close() 
    #os.rename('/Users/earvin/Downloads/DividendDetail.xls', '/Users/earvin/Downloads/5388.xls')
    os.rename('DividendDetail.xls', '2002.xls')
>>>>>>> d89be31ed5ade55f461957938a34edae12aaf21f
