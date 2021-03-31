from PIL import Image
from pytesseract import image_to_string
from base.find_element import FindElement


class Getimage(object):
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
        threshold = 200
        # 匿名函数
        filter_func = lambda x: 0 if x < threshold else 1
        photo = imgsty.point(filter_func, '1')
        photo.save(file_name)
        text = image_to_string(photo, config='eng')
        if text == "" or text is None:
            self.discern_captcha_image(file_name)
            print("未获取到验证码")
        else:
            captcha_error = FindElement().get_element('captcha_code-error')
            if captcha_error is not None:
                print("验证码错误")
                self.discern_captcha_image(file_name)
            else:
                return text

    # 识别图片验证码
    def discern_captcha_image(self, file_name):
        self.get_captcha_image(file_name=file_name)


