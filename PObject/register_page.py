from base.find_element import FindElement
from selenium import webdriver
import configparser


# 获取元素
class RegisterPage(object):
    def __init__(self, driver):
        # self.fl = FindElement(self.get_driver(wtype, url))
        self.fl = FindElement(driver)

    # 多个浏览器
    # def get_driver(self, wtype, url):
    #     if wtype == "chrome":
    #         driver = webdriver.Chrome()
    #     elif wtype == "firefox":
    #         driver = webdriver.Firefox()
    #     driver.get(url)
    #     driver.maximize_window()
    #     return driver

    # 邮箱
    def get_register_email(self):
        return self.fl.get_element("reg_email")

    # 用户名
    def get_register_nickname(self):
        return self.fl.get_element("reg_user")

    # 密码
    def get_register_password(self):
        return self.fl.get_element("reg_password")

    # 手机号
    def get_register_num(self):
        return self.fl.get_element("reg_mobile")

    # # 验证码输入框
    # def get_captcha_num(self):
    #     return self.fl.get_element("getcode_num")

    # # 验证码图片
    # def get_captcha_code(self):
    #     return self.fl.get_element("captcha_code")

    # 邮箱提示
    def get_email_placeholder(self):
        return self.fl.get_element("reg_email").get_attribute("placeholder")

    # 用户名提示
    def get_nickname_placeholder(self):
        return self.fl.get_element("reg_user").get_attribute("placeholder")

    # 密码提示
    def get_password_placeholder(self):
        return self.fl.get_element("reg_password").get_attribute("placeholder")

    # 手机号码提示
    def get_num_placeholder(self):
        return self.fl.get_element("reg_mobile").get_attribute("placeholder")

    # 邮箱错误
    def get_email_error(self):
        return self.fl.get_element("email_hint")

    # 用户名错误
    def get_nickname_error(self):
        return self.fl.get_element("user_hint")

    # 密码错误
    def get_password_error(self):
        return self.fl.get_element("password_hint")

    # 手机号码错误
    def get_num_error(self):
        return self.fl.get_element("mobile_hint")

    # # 验证码错误
    # def get_captcha_error(self):
    #     return self.fl.get_element("captcha_code-error")

    # 注册按钮
    def get_register_btn(self):
        return self.fl.get_element("red_button")
