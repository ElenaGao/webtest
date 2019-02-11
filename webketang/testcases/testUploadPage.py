# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/2/1 13:30
@email:huimin0099@qq.com
@function： 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.JoinPage import JoinPage
from pages.UploadPage import UploadPage
import time
import unittest

class TestUpload(unittest.TestCase):
    # 定位器
    toast_loc = (By.XPATH,'//div[@class="weui_dialog_bd"]')
    submit_loc = (By.XPATH,'//div[@class="weui_dialog_ft"]/a') # 知道了按钮
    comments_loc = (By.XPATH,'//span[text()="作业留言："]/following-sibling::span')

    @classmethod
    def setUpClass(cls):
        # 基础测试数据
        global driver,upload,text
        url = 'https://www.ketangpai.com'
        username = '18602153084'
        pwd = 'huimin99'
        invite_code = '29942D'
        text = "自动添加私信"
        # 开启会话
        driver = webdriver.Chrome()
        # 登录进入首页
        login = LoginPage(driver=driver,base_url=url,pagetitle='课堂派-简单好用的互动课堂管理工具')
        login.open()
        # 登录
        login.input_submit(username=username,pwd=pwd)
        # 添加课程
        join = JoinPage(driver=driver)
        check_loc = (By.XPATH,'//a[text()="python-WEB实战考核项目"]') # 加入成功检查元素
        try:
            if join.find_element(check_loc):
                print('已有该课程')
        except Exception:
            join.joinClass(invite_code=invite_code)

        # 实例化上传类
        upload = UploadPage(driver=driver)

    def test_upload_success(self):
        upload.submit('D:\\baidu.txt')
        print('执行上传文件操作')
        try:
            # 如果上传成功，弹出系统提示，点击知道了
            # 等待系统提示弹出
            if  upload.wait_ele_visible(self.toast_loc):
                upload.click(self.submit_loc) #
            print('上传文件成功')
        except Exception:
            print('上传文件测试失败')

    def test_comments(self):
        # 调用添加私信方法
        upload.comments(text)
        # 等待更新系统提示，点击知道了按钮
        if upload.wait_ele_visible(self.toast_loc):
            upload.click(self.submit_loc)
        # 比对私信是否添加成功
        try:
            actual = upload.get_text(self.comments_loc)
            self.assertEqual(text,actual)
            print('添加私信测试成功')
        except AssertionError:
            print('添加私信测试失败，实际添加内容为{0}'.format(actual))

    @classmethod
    def tearDownClass(cls):
        driver.quit()
