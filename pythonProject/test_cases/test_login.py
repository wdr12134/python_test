import os
import unittest
from libs import ddt
from common import excel_handler
from common import request_handler
import warnings

dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(dir_path,'data','cases.xlsx')
print(file_path)
test_data = excel_handler.ExcelHandler(file_path).read('Sheet1')
print(test_data)


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        print("用例执行完成")

    @ddt.data(*test_data)
    def test_login(self, data_info):
        pass
        res = request_handler.RequestsHandler().visit(data_info['method'],
                                                      data_info['url'],
                                                      headers=eval(data_info['headers']),
                                                      json=eval(data_info['json'])
                                                      )

        self.assertEqual(res['code'], data_info['expected'])
