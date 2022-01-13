import requests

from common import excel_handler


class RequestsHandler():

    def __init__(self):
        self.session = requests.Session()

    def visit(self, method, url, **kwargs):

        res = self.session.request(method, url, **kwargs)

        try:
            return res.json()
        except ValueError:
            print("not json")


if __name__ == '__main__':
    test_data = excel_handler.ExcelHandler(r'e:\cases.xlsx').read('Sheet1')[0]
    print(test_data)

    res = RequestsHandler().visit(test_data['method'],
                                  test_data['url'],
                                  headers=eval(test_data['headers']),
                                  json=eval(test_data['json']))
    print(res['code'])
