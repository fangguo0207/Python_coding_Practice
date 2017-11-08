# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 00:10:19 2017

@author: FANG
"""


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import ctypes

train = input("您要乘坐的车:")
beginning = input("您的启程地点:")
arriving = input ("您的到达城市:")
leibie=input("购买类别码\n（商务座：TZ\n一等座：ZY\n二等座:ZE\n高级软卧:GR\n软卧:RW\n动卧:SRRB\n硬卧：YW\n软座：RZ\n硬座：YZ\n无座：WZ\n其他：QT）\n您选择：")
confirmation=input("确定嘛（Y/N):")

while confirmation not in  ["是", "Y", "y" ] :
    train = input("您要乘坐的车:")
    beginning = input("您的启程地点:")
    arriving = input ("您的到达城市:")
    leibie=input("购买类别码\n（商务座：TZ\n一等座：ZY\n二等座:ZE\n高级软卧:GR\n软卧:RW\n动卧:SRRB\n硬卧：YW\n软座：RZ\n硬座：YZ\n无座：WZ\n其他：QT）\n您选择：")
    confirmation=input("确定嘛（Y/N):")

try:
    def chapiao():
        global beginning, arriving, leibie 
        driver = webdriver.Chrome()
        driver.get("http://www.12306.cn/mormhweb/")
        driver.implicitly_wait(30)
        lookup=driver.find_elements_by_css_selector("a[class='k4']")
        lookup[0].click()
        driver.switch_to.window(driver.window_handles[1])

        global arriving
        driver.find_element_by_id("fromStationText").click()
        driver.find_element_by_id("fromStationText").clear()
        driver.find_element_by_id("fromStationText").send_keys(beginning)
        driver.find_element_by_id("fromStationText").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("fromStationText").click()
    
        driver.find_element_by_id("toStationText").click()
        driver.find_element_by_id("toStationText").clear()
        driver.find_element_by_id("toStationText").send_keys(arriving)
        driver.find_element_by_id("toStationText").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("toStationText").click()
    
        driver.find_element_by_id("query_ticket").click()

        ticket_there=''
        
        for i in driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr/td"):
            global train
            if (leibie in i.get_attribute("id")) and (train in i.get_attribute("id")):
                ticket_there=beginning + "开往" + arriving + "的列车" + train +'次当前余票为:'+i.text
        driver.quit()
        return ticket_there
except TypeError:
    ctypes.windll.user32.MessageBoxW(0, "请重运行程序","网站", 1) 
except AttributeError:
    ctypes.windll.user32.MessageBoxW(0, "请重运行程序","网站", 1) 


x=chapiao()   
while '无' in x or '--' in x:
    from time import sleep
    sleep(10)
    chapiao()
else:    
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, x, "Ticket", 1) 
#网站出错调整