from util.read_ini import ReadIni
from selenium import webdriver
import configparser
import os


class FindElement(object):
    def __init__(self, driver):
        # url = "file:///F:/workspace/Webtesting/register/jQueryReg/index.html"
        self.driver = driver
        # self.driver.get(url)
        # self.driver.get("http://www.5itest.cn/register")

    def get_element(self, key):
        # ri = ReadIni()
        # data = ri.get_value(key=key)
        cf = configparser.ConfigParser()
        # cf.read('../util/RegisterElement.ini')
        cf.read('../util/RegisterElement.ini')
        # data = cf.get('RegisterElement', key)
        data = cf.get('RegisterElement2', key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "class":
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            file_path = '../image/no_element.png'
            self.driver.save_screenshot(file_path)

    def get_error_msg(self, error_msg):
        str_all = []
        for error_msg in error_msg:
            str1 = error_msg[-1::-1]
            str2 = str1[0:5]
            str3 = str1.split(str2)[1]
            str_all.append(str3[-1::-1])
        return str_all

if __name__ == "__main__":
    driver = webdriver.Chrome()
    fe = FindElement(driver)
    # print(fe.get_element('reg_user'))
    # driver.find_elements_by_xpath()
    # print(fe.get_error_msg("手机格式不正确"))



