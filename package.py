from selenium import webdriver
from time import sleep
from util.read_ini import ReadIni
from base.find_element import FindElement
import random
from PIL import Image,ImageEnhance
from pytesseract import image_to_string
import configparser
import os
import time


class Register(object):
    def __init__(self, url, browser):
        self.driver = self.get_driver(url, browser)

    # 启动浏览器
    def get_driver(self, url, browser):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 定位用户信息 获取元素
    def get_user_element(self, key):
        # find_element = FindElement(self.driver)
        # user_element = find_element.get_element(key=key)
        # return user_element
        cf = configparser.ConfigParser()
        cf.read('./util/RegisterElement.ini')
        data = cf.get('RegisterElement', key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_className(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            file_path = '../image/no_element.png'
            self.driver.save_screenshot(file_path)

    # 输入用户信息
    def send_user_info(self, key, value):
        self.get_user_element(key).send_keys(value)

    # 获取随机数
    def get_range(self):
        number = ''.join(random.sample('abcdefg123456', 8))
        return number

    # 获取验证码图片
    def get_captcha_image(self, file_name):
        self.driver.save_screenshot(file_name)
        captcha_element = self.get_user_element('getcode_num')
        left = captcha_element.location['x']
        top = captcha_element.location['y']
        right = captcha_element.size['width'] + left
        height = captcha_element.size['height'] + top
        image = Image.open(file_name)
        img = image.crop((left * 1.25, top * 1.25, right * 1.25, height * 1.25))
        img.save(file_name)
        # 转为灰度图
        imgsty = img.convert('L')
        imgsty.save(file_name)
        # enhancer = ImageEnhance.Color(img)
        # enhancer = enhancer.enhance(0)
        # enhancer = ImageEnhance.Brightness(enhancer)
        # enhancer = enhancer.enhance(2)
        # enhancer = ImageEnhance.Contrast(enhancer)
        # enhancer = enhancer.enhance(8)
        # enhancer = ImageEnhance.Sharpness(enhancer)
        # imgsty = enhancer.enhance(20)
        threshold = 200
        # table = []
        # for i in range(200):
        #     if i < threshold:
        #         table.append(0)
        #     else:
        #         table.append(1)
        filter_func = lambda x: 0 if x < threshold else 1
        photo = imgsty.point(filter_func, '1')
        photo.save(file_name)
        text = image_to_string(photo, config='eng')
        return text

    # 识别图片验证码
    def discern_captcha_image(self, file_name):
        self.get_captcha_image(file_name=file_name)
        # r = ShowapiRequest("http://route.showapi.com/184-4", "48120", "12c017278c0845c2bcda177212d2d2ac")
        # r.addBodyPara("img_base64", "")
        # r.addBodyPara("typeId", "35")
        # r.addBodyPara("convert_to_jpg", "0")
        # r.addBodyPara("needMorePrecise", "0")
        # r.addFilePara("image", file_name)  # 文件上传时设置
        # res = r.post()
        # text = res.json()["showapi_res_body"]["Result"]
        # text = image_to_string(, config='-1 eng')
        # return text

    # 主函数
    def main(self):
        register_nickname = self.get_range()
        register_email = self.get_range() + '@163.com'
        register_password = self.get_range() + '@123'
        file_name = './image/code_image.png'
        captcha_code = self.get_captcha_image(file_name)
        print(captcha_code)
        if captcha_code != '':
            self.send_user_info('register_nickname', register_nickname)
            self.send_user_info('register_email', register_email)
            self.send_user_info('register_password', register_password)
            self.send_user_info('captcha_code', captcha_code)
            self.get_user_element('register-btn').click()
            captcha_code_error = self.get_user_element('captcha_code-error')
            if captcha_code_error is None:
                print("注册成功")
                sleep(5)
                self.driver.close()
            else:
                self.driver.save_screenshot('./image/captcha_code_error.png')
        else:
            print("获取验证码失败")
            self.driver.close()


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    r = Register(register_url, 'chrome')
    r.main()



