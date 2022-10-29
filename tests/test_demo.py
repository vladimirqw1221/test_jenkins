import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages.autorization import Login


def test_demo_swag(set_up):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    a = Login(driver)
    a.autorez_met()

    time.sleep(5)




