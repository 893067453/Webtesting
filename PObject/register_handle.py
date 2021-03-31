from PObject.register_page import RegisterPage
from selenium import webdriver
from time import sleep


# 操作层
class RegisterHandle(object):
    def __init__(self, driver):
        self.hint_list = []
        self.driver = driver
        self.rp = RegisterPage(driver)

    # 输入邮箱
    def send_email(self, email):
        self.rp.get_register_email().send_keys(email)

    # 输入用户名
    def send_nickname(self, nickname):
        self.rp.get_register_nickname().send_keys(nickname)

    # 输入密码
    def send_password(self, password):
        self.rp.get_register_password().send_keys(password)

    # 输入验证码
    # def send_captcha(self, captcha):
    #     self.rp.get_captcha_num().send_key(captcha)

    # 输入手机号码
    def send_num(self, phone):
        self.rp.get_register_num().send_keys(phone)

    # 点击注册
    def click_btn(self):
        # 获取每个span
        self.rp.get_register_btn().click()
        hint_info = self.driver.find_elements_by_xpath("/html/body/div/ul/li/span[2]")
        # print(len(hint_info))
        # body > div > ul > li:nth-child(4) > span.mobile_hint
        # self.driver.find_elements_by_class_name()
        for error_info1 in hint_info:
            # if '不正确' in error_info1.text :
            if len(error_info1.text) !=0:
                self.hint_list.append(error_info1)
        # print(len(self.hint_list))

    # 获取错误信息
    def get_error_msg(self):
        info_text = []
        for error_info in self.hint_list:
            if error_info.text == "邮箱格式不正确":
                info_text.append(self.rp.get_email_error().text)
            if error_info.text == '用户名格式不正确':
                info_text.append(self.rp.get_nickname_error().text)
            if error_info.text == '密码格式不正确':
                info_text.append(self.rp.get_password_error().text)
            # elif error_info == 'captcha_code_error':
            #     text = self.rp.get_captcha_error().text
            if error_info.text == "手机格式不正确":
                info_text.append(self.rp.get_num_error().text)
            else:
                pass
        return info_text