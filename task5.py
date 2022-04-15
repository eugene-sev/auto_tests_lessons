from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = int(x_element.text)
    y = int(y_element.text)
    s = str(x+y)
    print (s)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s) 

    button = browser.find_element_by_class_name("btn-default")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
