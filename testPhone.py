from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from time import sleep

# Configuración de Appium
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "NSXDU17627001880"
options.platform_version = "6.0"
options.app_package = "net.metaquotes.metatrader5"
options.app_activity = "net.metaquotes.metatrader5.ui.MainActivity"
options.no_reset = True

# Conexión con Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
driver.implicitly_wait(1)

# Función para hacer clic con reintento
def safe_click(by, locator, retries=3, wait_time=2):
    for _ in range(retries):
        try:
            el = driver.find_element(by, locator)
            el.click()
            return True
        except (StaleElementReferenceException, NoSuchElementException):
            sleep(wait_time)
    raise Exception(f"No se pudo hacer clic en el elemento: {locator}")

# Función para esperar y hacer clic, evitando referencias obsoletas
def wait_and_click(by, locator, timeout=10, retries=3):
    for _ in range(retries):
        try:
            el = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            el.click()
            return True
        except (StaleElementReferenceException, TimeoutException):
            sleep(1)
    raise Exception(f"No se pudo hacer clic tras esperar: {locator}")

# 1️⃣ Clic en symbol_view
safe_click(AppiumBy.ID, "net.metaquotes.metatrader5:id/symbol_view")

# 2️⃣ Esperar y hacer clic en content
wait_and_click(AppiumBy.ID, "net.metaquotes.metatrader5:id/content")

# 3️⃣ Finalmente hacer clic en button_buy
wait_and_click(AppiumBy.ID, "net.metaquotes.metatrader5:id/button_buy")

# 4️⃣ Esperar y hacer clic para ver los parámetros de la entrada
wait_and_click(AppiumBy.ID, "net.metaquotes.metatrader5:id/trade_record")

# 5️⃣ Esperar un momento antes de cerrar o continuar
sleep(2)


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