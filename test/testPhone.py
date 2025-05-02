from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "NSXDU17627001880"
options.platform_version = "6.0"
options.app_package = "net.metaquotes.metatrader5"
options.app_activity = "net.metaquotes.metatrader5.ui.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
driver.implicitly_wait(10)

# Nuevo método correcto
driver.find_element(AppiumBy.ID, "net.metaquotes.metatrader5:id/symbol_view").click()

"""
1. Json
{
  "platformName": "Android",
  "appium:deviceName": "NSXDU17627001880",
  "appium:platformVersion": "6.0",
  "appium:appPackage": "net.metaquotes.metatrader5",
  "appium:appActivity": "net.metaquotes.metatrader5.ui.MainActivity",
  "appium:noReset": true
}
2. Json

3. Json
"""