# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/31 17:14
@email:huimin0099@qq.com
@function： 加入班级页面基本操作方法：如加入班级，退出班级
"""

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class JoinPage(BasePage):

    # 定位器，通过元素的各种定位方式，定位元素对象
    join_loc = (By.XPATH,'//div[text()="加入班级"]')
    input_invite_code_loc = (By.XPATH,'//input[@type="text"]') # 输入邀请码
    submit_loc = (By.XPATH,'//a[text()="加入"]') # 加入按钮
    cancel_loc = (By.XPATH,'//li[@class="cjli1"]/a') # 取消按钮

    detail_loc = (By.XPATH,'//a[@class="kdmore"]') # 课堂详情...按钮
    exit_loc = (By.XPATH,'//a[text()="退课"]') # ...中退课按钮
    exit_pwd_loc = (By.XPATH,'//input[@type="password"]') # 退课弹窗中输入密码
    exit_submit_loc = (By.XPATH,'//li[@class="dli2"]/a') # 退课弹窗中退课按钮

    # 重写基类的初始化函数，不需再次入参url,pagetitle
    def __init__(self,driver):
        self.driver = driver

    # 点击加入班级，输入邀请码
    def joinClass(self,invite_code,button='加入'):
        try:
            # 1 点击加入班级
            self.click(locator=self.join_loc)
            # 2 输入邀请码
            self.send_keys(self.input_invite_code_loc,invite_code)
            # 3 点击加入/取消按钮
            if button == '加入':
                self.click(self.submit_loc)
                print('点击加入按钮')
            elif button == '取消':
                self.click(self.cancel_loc)
                print('点击取消按钮')
        except Exception as e:
            print('点击加入/取消按钮失败')
            raise e

    def exitClass(self,pwd):
        try:
            # 点击要退出班级详情按钮...
            self.click(self.detail_loc)
            # 点击退课按钮
            self.click(self.exit_loc)
            # 输入正确的密码
            self.send_keys(self.exit_pwd_loc,pwd)
            # 点击退出按钮
            self.click(self.exit_submit_loc)
            print('点击退课成功')
        except Exception as e:
            print('点击退课失败')
            raise e



