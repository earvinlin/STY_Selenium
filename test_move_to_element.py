from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#driver= webdriver.Firefox(executable_path=r'C:\Users\ADMIN\Desktop\geckodriver.exe')
driver= webdriver.Firefox()
driver.get("http://www.apress.com")
main_menu=driver.find_element_by_link_text("CATEGORIES")
ActionChains(driver)\
.move_to_element(main_menu)\
.perform()
# Wait for sub menu to be displayed
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Python")))
sub_menu=driver.find_element_by_link_text("Python")
sub_menu.click()