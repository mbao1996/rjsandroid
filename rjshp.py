# -- coding: utf-8 --
from mblib import *
import os

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'b43052abe230'
desired_caps['appPackage'] = 'com.rongjinsuo.android'
desired_caps['appActivity'] = 'com.rjs.rongjinsuo.android.splash.SplashActivity'
#desired_caps['unicodeKeyboard'] = True
#desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(getSize(driver))
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
time.sleep(1)
#  选择产品
el = driver.find_element_by_id('com.rongjinsuo.android:id/main_tabs_btn2')
el.click()
time.sleep(1)
'''
#  选择优选
el = driver.find_element_by_name(u'鲸粉优选')
el.click()
time.sleep(2)
'''
xpath = '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]'
xpath_check = xpath + '/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]'
xpath_check = xpath_check + '/android.widget.LinearLayout/android.widget.TextView'
refresh = True
while(refresh):
    swipeUpDown(driver, 0.25, 0.75, 100)
    el_check = driver.find_element_by_xpath(xpath_check)
    if( el_check.text[0:2] == u'剩余' ):
        refresh = False
    else:
        print(el_check.text[0:2], '---', el_check.text)
        upto_time()
#        time.sleep(1)
print(el_check.text)
el = driver.find_element_by_xpath(xpath)
el.click()
#  点击立即加入
flag = False
while( not flag ):
    flag, el = isElement(driver, 'id', 'com.rongjinsuo.android:id/monthMore_btn_invest')
    if( not flag ):
        time.sleep(0.3)
#el = driver.find_element_by_id('com.rongjinsuo.android:id/monthMore_btn_invest')
el.click()
# 填入金额
flag = False
while( not flag ):
    flag, el = isElement(driver, 'id', 'com.rongjinsuo.android:id/normal_purchase_edit_money')
    if( not flag ):
        time.sleep(0.3)
#el = driver.find_element_by_id('com.rongjinsuo.android:id/normal_purchase_edit_money')
el.click()
#el.send_keys('8866.42')
driver.press_keycode(KEYCODE_8)
driver.press_keycode(KEYCODE_8)
driver.press_keycode(KEYCODE_6)
driver.press_keycode(KEYCODE_6)
driver.press_keycode(KEYCODE_PERIOD)
driver.press_keycode(KEYCODE_4)
driver.press_keycode(KEYCODE_2)
driver.press_keycode(KEYCODE_ESCAPE)
#swipeUpDown(driver, 0.3, 0.2, 100)

# 取红包
el = driver.find_element_by_id('com.rongjinsuo.android:id/normal_purchase_btn_redpacket')
el.click()
# 选红包
xpath = '//android.widget.ListView/android.widget.LinearLayout[2]'
el = driver.find_element_by_xpath(xpath)
el.click()
# 确认
el = driver.find_element_by_id('com.rongjinsuo.android:id/btn_set')
el.click()
# 确认加入
el = driver.find_element_by_id('com.rongjinsuo.android:id/btn_goinvest')
el.click()

'''
#  登录
el = driver.find_element_by_id('com.rongjinsuo.android:id/myFragment_login')
el.click()
time.sleep(6)

# click confirm
el = driver.find_element_by_id('com.rongjinsuo.android:id/confirm')
el.click()

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
# 点击产品
'''

print('---finished---')