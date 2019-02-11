# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/31 11:30
@email:huimin0099@qq.com
@function： 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 定位器，通过元素的各种定位方式，定位元素对象
login_loc = (By.XPATH,'//a[@class="login"]') # 首页登录元素
username_loc = (By.XPATH,'//input[@name="account"]') # 登录页用户名输入框
pwd_loc = (By.XPATH,'//input[@name="pass"]') # 登录页密码输入框
submit_loc = (By.XPATH,'//div[@class="padding-cont pt-login"]/a') # 登录页登录按钮

driver = webdriver.Chrome()
driver.get('https://www.ketangpai.com')
driver.find_element(*login_loc).click()
print('跳转登录页')
windows = driver.window_handles
driver.find_element(*username_loc).send_keys('18602153084')
driver.find_element(*pwd_loc).send_keys('huimin99')
driver.find_element(*submit_loc).click()
time.sleep(5)
# # 成功登录，等待新窗口出现
# WebDriverWait(driver,10).until(EC.new_window_is_opened(windows))
# # 切换窗口
# windows_new = driver.window_handles
# driver.switch_to.window(windows_new[-1])
# # driver.switch_to.window()
# joinclass_loc = (By.XPATH,'//div[text()="加入班级"]')
# text = driver.find_element(*joinclass_loc).text
# print(text)
# driver.quit()

homework_loc =(By.XPATH,'//a[text()="2019-0105 -web阶段思维导图"]') # 作业题目
driver.find_element(*homework_loc).click()
time.sleep(3)
resubmit_loc = (By.XPATH,'//a[@class="new-tj1"]') # 更新提交按钮
driver.find_element(*resubmit_loc).click()
