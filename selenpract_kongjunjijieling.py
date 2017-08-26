# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:23:48 2017

@author: FANG
"""


from selenium import webdriver
driver = webdriver.Chrome()
userlist=['casual_gambler']
textlist=[]
loglist=['2012-06-16 12:04:00']
for page in range(1,106):
    driver.get("http://bbs.tianya.cn/post-develop-1023408-{}.shtml".format(str(page)))
    trace=driver.find_elements_by_css_selector("div[class='atl-item']")
    contents=driver.find_elements_by_css_selector("div[class^='bbs-content']")
    for t in trace:
        userlist.append(t.get_attribute("js_username"))
    for c in contents:
        textlist.append(c.text)
    for t in trace:
        loglist.append(t.get_attribute("js_restime"))

from pandas import DataFrame
columnist=DataFrame(
    {'Username': userlist,
     'DT': loglist,
     'Content': textlist
    })







#get_attribute  Inner_HTML