# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/30 21:50
@email:huimin0099@163.com
@function： 所有页面的公共操作方法
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import win32gui
import win32con

class BasePage:
    '''

        Page基类，封装所有页面都公共的方法，如driver,url,findelement，wait,click,...
    '''
    # 初始化driver,url
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参
    # __init__方法不能有返回值，只能返回None
    # self是实例本身
    def __init__(self,driver,base_url,pagetitle):
        self.driver = driver
        self.base_url = base_url
        self.pagetitle = pagetitle


    # 通过title断言进入的页面是否正确
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果
    def on_page(self,pagetitle):
        return pagetitle in self.driver.title  # 返回值类型为Bool型

    # 打开页面，并检验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的
    def _open(self,url,pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window() # 最大化窗口
        # 使用assert进行校验，打开的窗口title是否与配置的title一致，调用on_page方法
        assert self.on_page(pagetitle),"打开页面失败{0}".format(url)

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url,self.pagetitle)

    # 重写元素定位方法
    def find_element(self,locator):
        try:
            # 确保元素是可见的
            # 注意：以下入参为元组的元素，需要加* -- 脱外套
            # python存在这种特性，就是将入参放在元组里。
            # 注意：以下入参本身是元组，不需要加* -- 不脱外套
            self.wait_ele_visible(locator)
            return self.driver.find_element(*locator)
        except Exception as e:
            print("页面中未找到{0}元素".format(locator))

    # 重写switch_frame方法
    def switch_frame(self,frame_reference):
        try:
            return WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))
        except Exception as e:
            raise e

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self,script):
        return self.driver.execute_script(script)

    # 重写send_keys方法
    def send_keys(self,locator,value):
        try:
            self.wait_ele_visible(locator)
            return self.driver.find_element(*locator).send_keys(value)
        except Exception as e:
            print("输入文本失败{0}".format(locator))

    # 重写点击方法
    def click(self,locator):
        try:
            self.wait_ele_visible(locator)
            return self.driver.find_element(*locator).click()
        except Exception as e:
            print("页面中未能找到{0}元素".format(locator))

    # 重写显示等待方法
    def wait_ele_visible(self,locator,wait_time=10,interval=1):
        try:
            return WebDriverWait(self.driver,wait_time,interval).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print("页面中未能找到{0}元素".format(locator))

    # 获取等待元素文本
    def get_text(self,locator):
        try:
            self.wait_ele_visible(locator)
            return self.find_element(locator).text
        except Exception as e:
            print("页面中未能找到{0}元素".format(locator))

    def upload(self,filepath):
        try:
            dialog = win32gui.FindWindow("#32770",'打开')
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)') # 确定按钮Button

            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath) # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
        except FileNotFoundError:
            print('cannot find the file'.format(filepath))

