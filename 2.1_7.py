from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_xpath("//img[@id = 'treasure']")

    x = chest.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_xpath("//input[@id = 'answer']")
    input1.send_keys(y)

    robotcheckbox = browser.find_element_by_id("robotCheckbox")
    robotcheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

    









    
    
