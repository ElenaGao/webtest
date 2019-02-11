# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/31 17:30
@email:huimin0099@qq.com
@function： 测试加入班级页面
前置条件：1）用户登录成功
后置条件：1）用户退出该课堂
正向用例：加入成功
反向用例：1）错误的邀请码 2）邀请码为空加入不可点击 3）取消加入
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.JoinPage import JoinPage
import time
import unittest

class TestJoinClass(unittest.TestCase):

    def setUp(self):
        # 基础测试数据
        global url,username,pwd,invite_code
        url = 'https://www.ketangpai.com'
        username = '18602153084'
        pwd = 'huimin99'
        invite_code = '29942D'
        # 开启会话
        self.driver = webdriver.Chrome()
        # 登录进入首页
        self.login = LoginPage(driver=self.driver,base_url=url,pagetitle='课堂派-简单好用的互动课堂管理工具')
        self.login.open()
        self.login.input_submit(username=username,pwd=pwd)
        self.join = JoinPage(driver=self.driver)

    def test_joinClass_success(self):
        print('----成功加入班级用例-----')
        # 点击加入班级，输入邀请码
        self.join.joinClass(invite_code=invite_code,button='加入')
        # 校验是否加入成功
        try:
            check_loc = (By.XPATH,'//a[text()="python-WEB实战考核项目"]') # 加入成功检查元素
            actual = self.join.get_text(check_loc)
            expected = 'python-WEB实战考核项目'
            self.assertEqual(expected,actual)
            print('成功加入班级测试成功')
        except AssertionError as e:
            print('成功加入班级测试失败')
            raise e

    def test_joinClass_with_wrong_inviteCode(self):
         print('----错误邀请码用例-----')
         # 点击加入班级，输入错误邀请码
         self.join.joinClass(invite_code='djjkadjkd',button='加入')
         time.sleep(0.1) # 等待吐司弹出
         # 校验提示吐司内容
         try:
             toast_loc = (By.XPATH,'//span[text()="该加课码不存在或者已经失效"]')
             actual = self.join.get_text(toast_loc)
             expected = '该加课码不存在或者已经失效'
             self.assertEqual(expected,actual)
             print('错误邀请码测试成功')
         except AssertionError as e:
             print('错误邀请码测试失败')
             raise e

    def test_joinClass_cancel(self):
        print('----取消加入班级用例-----')
        # 点击加入班级，输入邀请码,点击取消按钮
        self.join.joinClass(invite_code=invite_code,button='取消')
        # 校验是否取消加入成功
        check_loc = (By.XPATH,'//a[text()="python-WEB实战考核项目"]') # 加入成功检查元素
        expected = 'python-WEB实战考核项目'
        try:
            actual = self.join.get_text(check_loc)
            self.assertIn(expected,actual)
            print('取消加入班级测试失败')
        except Exception as e:
            print('取消加入班级测试成功')


    def tearDown(self):
        # 进行退课操作
        print('----判断是否要退课-----')
        exit_loc = (By.XPATH,'//a[text()="python-WEB实战考核项目"]')
        # img_loc = (By.XPATH,'//img[@class="img1"]') # 空页面提示图片
        try:
            # 如果是web实战课，则进行退课
            if self.join.find_element(exit_loc):
                detail_loc = (By.XPATH,'//a[@class="kdmore"]') # 课堂详情...按钮
                self.join.wait_ele_visible(detail_loc)
                self.join.exitClass(pwd=pwd)
                time.sleep(1)
        except Exception as e:
            # 如果未找到web实战课，则不进行退课
            print('没有web实战考核项目课程，不退课')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
