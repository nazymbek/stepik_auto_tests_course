from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    browser.execute_script("window.scrollBy(0, 150);")

    robotcheckbox = browser.find_element_by_id("robotCheckbox")
    robotcheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button = browser.find_element_by_class_name("btn-primary")
    button.click()
finally:
    time.sleep(5)
    browser.quit()










    






