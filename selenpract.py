# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:23:48 2017

@author: FANG
"""


from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get("https://reporting.recyclemyelectronics.ca/?process=login_frontoffice")
x=driver.find_element_by_id("example")
x.clear()
x.send_keys("example")
y=driver.find_element_by_class_name("example")
y.submit()


#find_element_by_css_selector('a').get_attribute('href')


driver.window_handles
driver.switch_to.window(driver.window_handles[number])


#in Webelement if <a target="_blank"> problem

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#driver = webdriver.Firefox()
#driver.get("http://somedomain/url_that_delays_loading")
#try:
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "myDynamicElement"))    )
#finally:
#    driver.quit()












def lookup(aword):
    global driver
    driver.find_element_by_class_name("search-input").send_keys(aword)
    driver.find_element_by_id("search-submit").click()
    t=driver.find_element_by_class_name("source-data").text
    return t
        

#driver.find_element_by_id("submit").click()
driver.find_element_by_link_text("Monthly Declarations").click()
driver.find_elements_by_class_name("group_name")[0].click()
T=driver.find_elements_by_class_name("period_category_header_in_top")
P=driver.find_elements_by_class_name("input_first")
d=dict(zip([i.text for i in T],[j.text for j in P]))
d1=DataFrame.from_dict(d,orient='index')
#d1.to_csv(r')