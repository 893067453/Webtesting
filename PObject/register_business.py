from PObject.register_handle import RegisterHandle
from base.find_element import FindElement
from selenium import webdriver
from time import sleep
from base.record_log import RecordLog


# 业务层
class RegisterBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.rh = RegisterHandle(driver)
        self.fe = FindElement(driver)
        self.logger = RecordLog().get_log()

    # 正常注册
    def common_register(self, email, nickname, password, num):
        self.rh.send_email(email)
        self.rh.send_nickname(nickname)
        self.rh.send_password(password)
        self.rh.send_num(num)
        self.rh.click_btn()
        if self.success_or_fail():
            print("注册成功")
            # self.logger.info("注册成功")
            sleep(5)
            # self.driver.quit()
        else:   # 注册失败
            error_msg = ''
            if len(self.fe.get_error_msg(self.rh.get_error_msg())) != 0:
                for str in self.fe.get_error_msg(self.rh.get_error_msg()):
                    error_msg = error_msg + str + " "
                print(error_msg,"输入有误")
                # self.logger.debug(error_msg,"输入有误")
            # self.driver.quit()

    # 判断是否注册成功
    def success_or_fail(self):
        if len(self.rh.get_error_msg()) == 0:  # 注册成功
            return True  # 注册成功
        else:
            return False  # 注册失败

    # 邮箱错误
    def register_email_fail(self, email, nickname, password, num):
        self.common_register(email, nickname, password, num)
        if self.success_or_fail():
            return False
        else:
            return True

    # 用户名错误
    def register_nickname_fail(self, email, nickname, password, num):
        self.common_register( email, nickname, password, num)
        if self.success_or_fail():
            return False
        else:
            return True

    # 密码错误
    def register_password_fail(self, email, nickname, password, num):
        self.common_register(email, nickname, password, num)
        if self.success_or_fail():
            return False
        else:
            return True

    # 手机号码错误
    def register_num_fail(self, email, nickname, password, num):
        self.common_register(email, nickname, password, num)
        if self.success_or_fail():
            return False
        else:
            return True

    # # 验证码错误
    #     # def register_captcha_fail(self, email, nickname, password, captcha):
    #     #     self.common_register(email, nickname, password, captcha)
    #     #     if self.success_or_fail("captcha_code-error"):
    #     #         return False
    #     #     else:
    #     #         return True


if __name__ == "__main__":
    driver = webdriver.Chrome()
    ob = RegisterBusiness(driver)
    ob.common_register('zwjzsq@qq.com', 'zwjzsq', '123456', '13800138000')


