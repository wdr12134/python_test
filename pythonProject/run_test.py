import os
import unittest
from datetime import datetime

from common import HTMLTestRunnerNew

testloader = unittest.TestLoader()
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')

suite = testloader.discover(case_path)

# report
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)

time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = 'test_result_{}.html'.format(time_str)
file_path = os.path.join(report_path, file_name)

#TODO:一定要用二进制的方式打开
with open(file_path, 'wb') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f,
                                              title="自动化测试报告",
                                              tester='wdr')
    runner.run(suite)
