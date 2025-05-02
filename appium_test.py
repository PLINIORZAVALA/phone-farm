from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "NSXDU17627001880"
options.app_package = "net.metaquotes.metatrader5"
options.app_activity = "net.metaquotes.metatrader5.ui.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(5)

try:
    # Cambio aquí: usamos AppiumBy
    trade_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trade")')
    trade_button.click()
    print("[INFO] Botón 'Trade' presionado.")
except Exception as e:
    print(f"[ERROR] No se encontró el botón 'Trade'. {e}")

driver.quit()

"""
Inspecionar la aplicaion que queramos abrir
 - adb shell "dumpsys window windows | grep -E 'mFocusedApp'"
 Configuración básica para el dispositivo en Appium Inspector:

 data para App Inspector:
  - Colocar el servidor local: 127.0.0.1
  - Colacar el puerto del servidor: 4723
  - Colocar la ruta: /wd/hub
JSON:
{
  "platformName": "Android",
  "appium:deviceName": "NSXDU17627001880",
  "appium:platformVersion": "6.0",
  "appium:appPackage": "net.metaquotes.metatrader5",
  "appium:appActivity": "net.metaquotes.metatrader5.ui.MainActivity",
  "appium:noReset": true
}

"""

