# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:43:26 2017

@author: FANG
"""



from selenium import webdriver
import  time  #调入time函数

browser = webdriver.Firefox()


browser.get("http://www.indeed.ca")
time.sleep(0.3)  #休眠0.3秒
browser.find_element_by_id("what").send_keys("analyst")
browser.find_element_by_id("where").clear()
browser.find_element_by_id("where").send_keys("Toronto,ON")
browser.find_element_by_id("fj").click()
time.sleep(1.0)
element=browser.find_elements_by_class_name("turnstileLink") #必须用elements

for i in range(10):
    element[i].click()
time.sleep(5.0)
handle=browser.window_handles
browser.switch_to_window(handle[1])
browser.close()
time.sleep(1.0)
browser.switch_to_window(handle[0])
browser.find_element_by_class_name("np").click()
print(browser.find_element_by_class_name("np"))
time.sleep(5.0)
browser.find_element_by_class_name("popover-close-link").click()