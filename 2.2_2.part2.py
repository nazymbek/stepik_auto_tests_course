from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

"""browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(3)").click()"""

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("889")

button = browser.find_element_by_class_name("btn-default")
button.click()

time.sleep(5)
browser.quit()



