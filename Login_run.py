import unittest
import HTMLTestRunnerNew


suite=unittest.defaultTestLoader.discover("D:\pycharm2020\pycharm scripts\ceshiti",pattern="login.py") #用例文件的路径

with open("reports.html", "wb+")as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, 2, title="testlogin", tester="ylj", description="unittest")
    runner.run(suite)