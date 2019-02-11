# -*- coding:utf-8 _*-
""" 
@author:Elena
@time: 2019/1/30 22:03
@email:huimin0099@163.com
@function： 
"""
import HTMLTestRunnerNew
import unittest
import os
import time

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
base_path = os.path.join(os.getcwd())
report_path = os.path.join(os.path.join(os.getcwd()),'testreport')
testcases_path = os.path.join(base_path,'testcases')
report = os.path.join(report_path, "HtmlReport_"+now+".html")
print(report_path)

# 自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(testcases_path, pattern="test*.py", top_level_dir=None)
#
with open(report, 'wb') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='WEB自动测试报告',
                                              tester='Elena')
    runner.run(discover)  # 执行查找到的用例
