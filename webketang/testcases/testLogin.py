# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/30 22:02
@email:huimin0099@163.com
@function： 测试登录页面
正向用例：登录成功
反向用例：1）用户名/密码为空 2）错误密码 3）错误用户名
"""
from selenium import webdriver
from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import unittest

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        # 基础测试数据
        global url,username,pwd,wrong_pwd,wrong_username
        url = 'https://www.ketangpai.com'
        username = '18602153084'
        pwd = 'huimin99'
        wrong_pwd = 'huimin'
        wrong_username = '186021530845'

        # 开启浏览器会话
        self.driver = webdriver.Chrome()
        # 1 进入课堂派首页,点击登录跳转至登录页
        self.login = LoginPage(driver=self.driver,base_url=url,pagetitle='课堂派-简单好用的互动课堂管理工具')
        self.login.open()

    # 正确用户名和密码 > 登录成功
    def test_login_success(self):
        # 2 输入正确的用户名和密码,点击登录按钮
        self.login.input_submit(username=username,pwd=pwd)
        # 3 验证是否登录成功
        try:
            expected = '加入班级'
            joinclass_loc = (By.XPATH,'//div[text()="加入班级"]')
            actual = self.login.get_text(joinclass_loc)
            self.assertEqual(expected,actual)
            print('登录成功测试通过')
        except AssertionError as e:
            print('登录出错')
            raise e
    # 用户名/密码为空 > 登录失败
    def test_login_with_null(self):
        self.login.input_submit(username="",pwd="")
        try:
            expected = '账号不能为空'
            toast_loc = (By.XPATH,'//p[text()="账号不能为空"]')
            actual = self.login.get_text(toast_loc)
            self.assertEqual(expected,actual)
            print('账号不能为空测试通过')
        except AssertionError as e:
            print('账号不能为空测试失败')
            raise e

    # 用户名/密码错误 > 登录失败
    def test_login_with_wrong_pwd(self):
        self.login.input_submit(username=username,pwd=wrong_pwd)
        try:
            toast_loc = (By.XPATH,'//p[text()="密码错误, 你还可以尝试4次"]')
            actual = self.login.get_text(toast_loc)
            expected = '密码错误, 你还可以尝试4次'
            self.assertEqual(expected,actual)
            print('密码错误测试通过')
        except AssertionError as e:
            print('密码错误测试失败')
            raise e

    def test_login_with_wrong_username(self):
        self.login.input_submit(username=wrong_username,pwd=pwd)
        try:
            toast_loc = (By.XPATH,'//p[text()="用户不存在"]')
            actual = self.login.get_text(toast_loc)
            expected = '用户不存在'
            self.assertEqual(expected,actual)
            print('用户名错误测试通过')
        except AssertionError as e:
            print('用户名错误测试失败')
            raise e


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
