#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-09-20 17:00:47
# @Last Modified time: 2018-09-21 09:53:06
# @E-mail: 1370465454@qq.com
# @Description:

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from PIL import Image
import time
import re
import random
import os


class OpenHideLocators:
    """"隐藏的属性需要更改之后才能获取到"""
    display_block = "$('.geetest_canvas_fullbg').css('display','block');"
    display_none = "document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='none'"


class Crack():

    def __init__(self):
        """
        初始化
        """
        self.url = 'https://passport.cnblogs.com/user/signin'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10, 0.5)

    def mk_img_dir(self):
        """
        创建图片目录文件
        :return:
        """
        if not os.path.exists('Image'):
            os.mkdir('Image')

    def get_image(self, filename):
        """
        截图
        @filename 图片名称
        """
        img = self.driver.find_element_by_class_name('geetest_canvas_img')
        time.sleep(2)
        location = img.location
        size = img.size
        # print('大小'+str(size))

        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']

        page_snap_obj = self.get_snap(filename + '.png')
        image_obj = page_snap_obj.crop((left, top, right, bottom))
        # image_obj.show()
        return image_obj

    def get_snap(self, save_name):
        """
        保存图片
        """
        self.driver.save_screenshot('./Image/' + save_name)
        page_snap_obj = Image.open('./Image/' + save_name)
        return page_snap_obj

    def is_px_equal(self, img1, img2, x, y):
        """
        判断两个像素是否相同
        :param img1: 图片1
        :param img2:图片2
        :param x:位置1
        :param y:位置2
        :return:像素是否相同
        """
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        threshold = 60

        if abs(pix1[0] - pix2[0]) < threshold and abs(pix1[1] - pix2[1]) < threshold and abs(pix1[2] - pix2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获取缺口偏移量
        :param img1: 不带缺口图片
        :param img2: 带缺口图片
        :return:
        """
        left = 57
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_px_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        根据偏移量和手动操作模拟计算移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        tracks = []
        # 当前位移
        current = 60
        # 减速阈值
        mid = distance * 4 / 5

        # 时间间隔
        t = 0.2
        # 初始速度
        v = 0

        while current < distance:
            if current < mid:
                a = random.uniform(2, 5)
                print('当前距离'+str(current))
                print('距离'+str(distance))
                print('阈值'+str(mid))
            else:
                a = -(random.uniform(12.5, 13.5))
                print('当前距离1'+str(current))
                print('距离1'+str(distance))
                print('阈值1'+str(mid))
            v0 = v
            v = v0 + a * t
            print('v'+'='+str(v))
            x = v0 * t + 1 / 2 * a * t * t
            print('X'+'='+str(x))
            current += x

            if 0.6 < current - distance < 1:
                x = x - 0.50
                tracks.append(round(x, 2))

            elif 1 < current - distance < 1.5:
                x = x - 1.4
                tracks.append(round(x, 2))
            elif 1.5 < current - distance < 3:
                x = x - 1.8
                tracks.append(round(x, 2))

            else:
                tracks.append(round(x, 2))

        return tracks

    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """
        try:
            slider = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[2]')))
            return slider
        except TimeoutError:
            print('加载超时...')

    def move_to_gap(self, slider, tracks):
        """
        将滑块移动至偏移量处
        :param slider: 滑块
        :param tracks: 移动轨迹
        :return:
        """
        action = ActionChains(self.driver)
        action.click_and_hold(slider).perform()
        for x in tracks:
            action.move_by_offset(xoffset=x, yoffset=-1).perform()
            action = ActionChains(self.driver)
        time.sleep(1)
        action.release().perform()

    def success_check(self):
        """
        验证是否成功
        :return:
        """
        try:
            if re.findall('gt_success', self.browser.page_source, re.S):
                print('验证成功！')
                return True
            else:
                print('验证失败！')
                return False
        except TimeoutError:
            print('加载超时...')
        finally:
            pass

    def cnblog_crack(self):  # 破解滑动认证
        # 1.点击按钮，进入图片页面
        button = self.wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, 'geetest_radar_tip')))
        #self.driver.find_element_by_class_name('geetest_radar_tip')
        button.click()
        time.sleep(3)
        self.driver.execute_script(OpenHideLocators.display_block)
        time.sleep(5)
        # 2.获取没有缺口的图片
        image1 = self.get_image('full_image')
        time.sleep(2)
        self.driver.execute_script(OpenHideLocators.display_none)
        # 3.点击滑动按钮,得到有缺口的图片
        button = self.driver.find_element_by_class_name(
            'geetest_slider_button')
        button.click()

        # 4.获取有缺口的图片
        image2 = self.get_image('full_snap')

        # 5.对比两种图片的像素点,找出位移
        distance = self.get_gap(image1, image2) * 1.138
        print('对比' + str(distance))
        slider = self.get_slider()
        # 6.模拟人的行为习惯,根据总位移得到的行为轨迹
        tracks = self.get_track(distance)
        print(tracks)
        self.move_to_gap(slider, tracks)
    def login_cnblogs(self, username, password):
        # try:
        #     while True:
        self.driver.implicitly_wait(3)
        self.driver.get(self.url)
        self.mk_img_dir()
        input_username = self.driver.find_element_by_id('input1')
        input_pwd = self.driver.find_element_by_id('input2')
        signin = self.driver.find_element_by_id('signin')

        input_username.send_keys(username)
        input_pwd.send_keys(password)
        signin.click()

        # 2、破解滑动认证
        self.cnblog_crack()
        time.sleep(3)
        CHECK = check.success_check()
        #         if CHECK == True:
        #             break
        # except Exception:
        #     print('程序出错啦！')
if __name__ == '__main__':
    Cracks = Crack()
    Cracks.login_cnblogs(username='dangkai', password='dk137456..')
