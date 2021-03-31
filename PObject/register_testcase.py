from PObject.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import ddt
import warnings
from HTMLTestRunner import HTMLTestRunner
from base.read_excel import ReadExcel
from time import sleep


@ddt.ddt
class RegisterTT(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.reg_url = "file:///F:/Pworkspace\Webtesting/register/jQueryReg/index.html"
        self.driver = webdriver.Chrome()
        self.driver.get(self.reg_url)
        # self.driver.maximize_window()
        self.rb = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    @ddt.data(
        # 邮箱 用户名 密码 手机号码
        ['zwjzsq@qq.com', 'zwjzsq', '123456', '13800138000'],
        ['zwjzsq@qq.com', 'zwjzsq', '12345', '13800138000'],
        ['zwjzsq@qq.com', 'zwjzsq', '123456', '1380013800']
    )
    @ddt.unpack
    def test_001(self, email, name, password, mobile):
        self.rb.common_register(email, name, password, mobile)

    def get_excel_data(self):
        handle_excel = ReadExcel(self.Excel_path)

        # 获取测试用例条数
        cases_num = handle_excel.get_lines()
        print("测试用例条数:%s" % cases_num)

        # 循环遍历测试用例
        if cases_num:
            for i in range(1, cases_num):
                testcase_name = handle_excel.get_cell(i, 0)  # 获取测试用例名称
                is_run = handle_excel.get_cell(i, 1)
                if is_run == 'yes':
                    email = handle_excel.get_cell(i, 2)
                    name = handle_excel.get_cell(i, 3)
                    password = handle_excel.get_cell(i, 4)
                    mobile = handle_excel.get_cell(i, 5)
                    self.rb.common_register(email, name, password, mobile)
        else:
            print("测试用例为空")


if __name__ == '__main__':
    # unittest.main()
    # suit = unittest.TestSuite()  # 创建测试套件
    # test_list = ['test_register']  # 定义一个测试用例列表
    # for case in test_list:
    #     suit.addTest(RegisterTT(case))  # 添加测试用例
    # 运行测试用例， verbosity=2 为每个测试用例生成 测试报告
    # unittest.TextTestRunner(verbosity=2).run(suit)
    cases = unittest.TestLoader().loadTestsFromTestCase(RegisterTT)
    suite = unittest.TestSuite([cases])
    with open('../test_report/report.html', 'wb') as f:
        HTMLTestRunner(
            stream=f,  # 指定测试数据写入哪个文件
            title='测试报告',  # 测试报告的标题
            description='zwj编写',  # 描述
            verbosity=2
        ).run(suite)


