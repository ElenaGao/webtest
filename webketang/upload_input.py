# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/25 13:05
@email:huimin0099@qq.com
@function： input类型的文件上传  -- sendkeys
"""
from selenium import webdriver
import win32gui
import win32con
import time

def upload(filepath):
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

upload(filepath='C:\\Users\\admin\\Desktop\\test.text')



