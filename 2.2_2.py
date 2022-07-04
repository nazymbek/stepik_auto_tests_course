from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(3)").click()

button = browser.find_element_by_class_name("btn-default")
button.click()

time.sleep(5)
browser.quit()



