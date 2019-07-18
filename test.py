# -- coding: utf-8 --
from appium import webdriver
import time, os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'b43052abe230'
desired_caps['app'] = PATH(r"C:\test\com.rongjinsuo.android_v5.5.5_555.apk")
desired_caps['appPackage'] = 'com.rongjinsuo.android'
desired_caps['appActivity'] = 'com.rjs.rongjinsuo.android.splash.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
#print(driver.isAppInstalled())

print('---finished---')

'''
driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()
driver.quit()


from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
desired_caps = {
'platformName':'Android',
'platformVersion':'4.4.4',
'deviceName':'b43052abe230',
'appPackage':'com.huawei.android.launcher',
'appActivity':'com.huawei.android.launcher.splashscreen.StartActivity',
'appWaitActivity':'com.huawei.android.launcher/.splashscreen.activity.StartActivity',
'noReset':True,
}

driver=webdriver.Remote('b43052abe230',desired_caps)
'''