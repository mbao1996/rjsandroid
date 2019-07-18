# -- coding: utf-8 --
from appium import webdriver
import time, os

#PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'b43052abe230'
#desired_caps['app'] = PATH(r"C:\test\com.rongjinsuo.android_v5.5.5_555.apk")
#desired_caps['app'] = r"C:\test\com.rongjinsuo.android_v5.5.5_555.apk"
desired_caps['appPackage'] = 'com.rongjinsuo.android'
desired_caps['appActivity'] = 'com.rjs.rongjinsuo.android.splash.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
'''
# exit from welcome page
el = driver.find_element_by_id('com.rongjinsuo.android:id/btn_ljty')
el.click()
# exit from get bonus
el = driver.find_element_by_id('com.rongjinsuo.android:id/to_register_dialog_close_btn')
el.click()
'''
#  选择我的
el = driver.find_element_by_id('com.rongjinsuo.android:id/main_tabs_btn3')
el.click()
#  登录
el = driver.find_element_by_id('com.rongjinsuo.android:id/myFragment_login')
el.click()
time.sleep(6)
'''
# click confirm
el = driver.find_element_by_id('com.rongjinsuo.android:id/confirm')
el.click()
'''
# input username
el = driver.find_element_by_id('com.rongjinsuo.android:id/edit_phone_account')
el.send_keys('Groningen')
# input pwd
el = driver.find_element_by_id('com.rongjinsuo.android:id/edit_pwd')
el.send_keys('zpl177l36h')
# confirm login
el = driver.find_element_by_id('com.rongjinsuo.android:id/btn_login_account')
el.click()
time.sleep(1)
#  选择产品
el = driver.find_element_by_id('com.rongjinsuo.android:id/main_tabs_btn2')
el.click()
time.sleep(2)


'''
#  选择优选
el = driver.find_element_by_name(u'鲸粉优选')
el.click()
time.sleep(2)
# 点击产品

el = driver.find_element_by_id('')
el.click()
time.sleep(2)
'''

print('---finished---')