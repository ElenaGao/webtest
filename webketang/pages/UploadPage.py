# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/2/1 13:29
@email:huimin0099@qq.com
@function：上传页面基本操作

5. 验证系统提示信息，判断是否上传成功
6. 若是更新提交，点击更新提交按钮>上传文件>选择文件>点击更新提交>判断是否上传成功
"""
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class UploadPage(BasePage):
    # 定位器
    homework_loc =(By.XPATH,'//a[text()="2019-0105 -web阶段思维导图"]') # 作业题目
    check_loc = (By.XPATH,'//div[@class="status fr"]/span') # 已完成/未完成
    submit_loc = (By.XPATH,'//a[@class="tj-btn"]') # 首次提交按钮
    resubmit_loc = (By.XPATH,'//a[@class="new-tj1"]') # 更新提交按钮
    sure_loc = (By.XPATH,'//a[text()="确定"]') # 更新提示弹窗的确定按钮
    cancel_loc = (By.XPATH,'//a[text()="取消"]')

    upload_loc = (By.XPATH,'//a[@class="sc-btn webuploader-container"]') # 上传文件按钮
    resubmit_loc2 = (By.XPATH,'//a[@class="new-tj2 active"]') # 更新提交后的更新提交按钮
    check_upload_loc = (By.XPATH,'//a[text()="已上传"]') # 上传成功状态标识

    # 私信定位器
    comments_loc = (By.XPATH,'//span[text()="作业留言："]/following-sibling::span')
    input_loc = (By.XPATH,'//textarea[@id="comment"]')
    save_loc = (By.XPATH,'//a[text()="保存"]')

    # 重写基类的初始化函数，不需再次入参url,pagetitle
    def __init__(self,driver):
        self.driver = driver

    # 上传文件
    def submit(self,filepath,button='确定'):
        try:
            # 1. 点击近期作业
            self.click(self.homework_loc)
            # 进入提交页面
            self.wait_ele_visible(self.resubmit_loc)
            # 2. 根据完成状态判断是提交/更新提交
            if self.find_element(self.submit_loc):
                # 首次提交
                self.click(self.upload_loc)
                self.upload(filepath=filepath) # 上传文件
                self.wait_ele_visible(self.check_upload_loc,wait_time=20) # 等待上传成功标识
                self.click(self.submit_loc) # 点击提交
                print('首次上传文件')
            elif self.find_element(self.resubmit_loc):
                # 更新提交
                self.click(self.resubmit_loc)
                time.sleep(1)
                if button == '确定':
                    self.click(self.sure_loc) # 点击确定
                    self.click(self.upload_loc) # 点击上传文件
                    time.sleep(1)
                    self.upload(filepath=filepath)
                    self.wait_ele_visible(self.check_upload_loc,wait_time=20)
                    self.click(self.resubmit_loc2) # 点击更新提交
                elif button == '取消':
                    self.click(self.cancel_loc)
        except Exception:
            print('上传文件失败')


    def comments(self,text):
        try:
            # 1. 点击近期作业
            self.click(self.homework_loc)
            # 进入提交页面
            self.wait_ele_visible(self.resubmit_loc)
            # 2. 根据完成状态判断是提交/更新提交
            if self.find_element(self.submit_loc):
                # 首次提交
                self.click(self.upload_loc)
                self.click(self.comments_loc)
                self.send_keys(locator=self.input_loc,value=text)
                self.click(self.save_loc)
            elif self.find_element(self.resubmit_loc):
                # 更新提交
                self.click(self.resubmit_loc)
                self.click(self.sure_loc)
                self.click(self.comments_loc)
                self.send_keys(locator=self.input_loc,value=text)
                self.click(self.save_loc)
                self.click(self.resubmit_loc2)
        except Exception:
            print('添加私信失败')




