from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Stepan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Bandra")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Baderlyandiya@gg.com")
   
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

