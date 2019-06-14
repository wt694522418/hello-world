from time import sleep

from appium import webdriver


# 配置信息
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.25.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 解决中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 创建驱动
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# wlan = driver.find_element_by_xpath("//*[contains(@text, 'WL')]")

# 按下 #等待 # 松开
TouchAction(driver).press(x=342,  y=944).wait(10000).release().perform()


driver.quit()
#haha
