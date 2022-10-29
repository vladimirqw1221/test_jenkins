import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages.autorization import Login
from pages.negativ_autorization import Negativ


def test_demo_swag(set_up):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    n = Negativ(driver)
    n.negativ_test_case()

    time.sleep(5)




