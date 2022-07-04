from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)

    imRobot = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    imRobot.click()

    robotsRule = browser.find_element_by_xpath("//label[@for='robotsRule']")
    robotsRule.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()