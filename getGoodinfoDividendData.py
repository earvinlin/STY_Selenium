from genericpath import isfile
import os
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import false

if len(sys.argv) < 2 :
    print("You need input one parameter(fmt : 2022) ")
    print("syntax : C:\python getGoodinfoDividenData.py 2022 ")
    sys.exit()

maxRetryCnt = 3
stockCode = sys.argv[1]
stockFilename = stockCode + ".xls"
dividendFilename = "DividendDetail.xls"

# 設定broser profile(這支程式以firefox為範例，故只適用firefox browser)
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.getcwd())
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

isFinished = False
retryCnt = 0

while (not isFinished):
    # firefox
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("https://goodinfo.tw/tw/index.asp")

    elem = driver.find_element_by_id("txtStockCode")
    elem.send_keys(stockCode)
    elem.send_keys(Keys.RETURN)

    try:
        # 這種寫法，有時侯會因為網頁載入太慢(>10秒)而失敗
        driver.implicitly_wait(10)
        web_element=driver.find_element_by_link_text('股利政策')
        web_element.click()

        # 這種寫法，有時侯會因為網頁載入太慢(>15秒)而失敗
        driver.implicitly_wait(15)
        button = driver.find_element_by_xpath("//input[@type='button' and @value='匯出XLS']")
        driver.execute_script("arguments[0].click();", button)
    finally:
        # 關閉browser
        driver.close() 
        #os.rename('/Users/earvin/Downloads/DividendDetail.xls', '/Users/earvin/Downloads/5388.xls')
        if os.path.isfile(dividendFilename):
            os.rename(dividendFilename, stockFilename)
            isFinished = True
        else:
            retryCnt += 1
            if retryCnt >= maxRetryCnt:
                isFinished = True
                # out errorfile
                with open("_errorlog.txt", "a") as logFile:
                     logFile.write(stockFilename + " failure.\n")
                logFile.close() 
