# -- coding: utf-8 --
from appium import webdriver
import time
import subprocess

KEYCODE_0 = '7'
KEYCODE_1 = '8'
KEYCODE_2 = '9'
KEYCODE_3 = '10'
KEYCODE_4 = '11'
KEYCODE_5 = '12'
KEYCODE_6 = '13'
KEYCODE_7 = '14'
KEYCODE_8 = '15'
KEYCODE_9 = '16'
KEYCODE_PERIOD = '56'
#KEYCODE_ENTER = '66'
KEYCODE_ESCAPE = '111'

def upto_time():
    time_now = time.strftime('%H:%M:%S', time.localtime(time.time()))
    if( time_now < "09:58:00" ):
        time.sleep(30)
        print('--- nap ---', time_now)
    elif(time_now < "09:59:00" ):
        time.sleep(15)
        print('--- wait ---', time_now)
    elif(time_now < "09:59:30" ):
        time.sleep(5)
        print('--- long ---', time_now)
    elif(time_now < "09:59:50" ):
        time.sleep(1.5)
        print('--- medium ---', time_now)
    else:
        time.sleep(0.6)
        print('--- short ---', time_now)
    return(time_now)
def getSize(dr):
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)
#屏幕向上滑动
def swipeUpDown(dr, ry1, ry2, t):
    sz = getSize(dr)
    x1 = int(sz[0] * 0.5)  #x坐标
    y1 = int(sz[1] * ry1)   #起始y坐标
    y2 = int(sz[1] * ry2)   #终点y坐标
    dr.swipe(x1, y1, x1, y2, t)
def fast_input(str,element):
    element.click()
    cmd = "adb -s b43052abe230 shell input text " + str
    time.sleep(0.3)
    subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    time.sleep(0.5)

def isElement(driver, identifyBy, c):
    flag = None
    el = driver
    try:
        if identifyBy == "id":
            el = driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            el = driver.find_element_by_xpath(c)
        flag = True
    except Exception as e:
        flag = False
    return(flag, el)

def getElement(driver, identifyBy, c):
    flag = False
    while( not flag ):
        flag, el = isElement(driver, identifyBy, c)
        if( not flag ):
            time.sleep(0.1)
    return(el)
