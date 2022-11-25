import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options, service=service)
driver.get("https://rozetka.com.ua/ua")

input_search = driver.find_element(By.XPATH, "//input[@name='search']")
# input_search = driver.find_element(By.NAME, "search")
input_search.send_keys("Samsung Galaxy S22")
time.sleep(1)
input_search.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
time.sleep(1)
input_search.send_keys("Iphone")

time.sleep(1)
button_search = driver.find_element(By.CSS_SELECTOR,
                                    "body > app-root > div > div > rz-header > rz-main-header > header > div > div > div > form > button")
button_search.click()
time.sleep(3)

add_to_cart_buttons = driver.find_elements(By.XPATH,
                                           "//button[@class='buy-button goods-tile__buy-button ng-star-inserted']")

for i, button in enumerate(add_to_cart_buttons):
    if i % 2 == 0:
        button.click()

cart_button = driver.find_element(By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")
cart_button.click()
time.sleep(3)
to_order_button = driver.find_element(By.XPATH, "//a[contains(text(),'Оформити замовлення')]")

print(to_order_button.get_property("class"))

to_order_button.click()

time.sleep(20)
