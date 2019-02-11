# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/30 21:48
@email:huimin0099@163.com
@function： 登录页面基本操作方法：如open，input_username，input_password，click_submit
"""

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

# 继承BasePage类
class LoginPage(BasePage):
    # 定位器，通过元素的各种定位方式，定位元素对象
    login_loc = (By.XPATH,'//a[@class="login"]') # 首页登录元素
    username_loc = (By.XPATH,'//input[@name="account"]') # 登录页用户名输入框
    pwd_loc = (By.XPATH,'//input[@name="pass"]') # 登录页密码输入框
    submit_loc = (By.XPATH,'//div[@class="padding-cont pt-login"]/a') # 登录页登录按钮

    # 页面操作
    # 打开网页
    #通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    def open(self):
        #调用page中的_open打开首页
        self._open(self.base_url,self.pagetitle)
        # 点击登录，跳转至登录页
        self.click(self.login_loc)

    # 输入用户名及密码
    def input_submit(self,username,pwd):
        try:
            self.send_keys(self.username_loc,username) # 输入用户名
            self.send_keys(self.pwd_loc,pwd) # 输入密码
            self.click(self.submit_loc) # 点击登录按钮

        except Exception as e:
            print("登录失败！")
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    login_page = LoginPage(driver=driver,base_url='https://www.ketangpai.com',pagetitle='课堂派-简单好用的互动课堂管理工具')
    login_page.open()
    time.sleep(5)
    login_page.input_submit('18602153084','huimin99')






