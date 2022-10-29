import allure

from buse_page.buse import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilites.logger import Logger


class Login(Buse):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.saucedemo.com/"

    # LOCATORS

    user_name = "//input[@id='user-name']"
    passsword =  "//input[@id='password']"
    ligin_btn = "//input[@id='login-button']"
    asert_check = "//span[@class='title']"

    # GETTERS

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.passsword)))

    def get_ligin_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ligin_btn)))

    def get_asert_check(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.asert_check)))



    # ACTIONS


    def input_user_name(self , user_name):
        self.get_user_name().send_keys(user_name)
        print(" Имя пользователя введено")



    def input_passsword(self , passsword):
        self.get_password().send_keys(passsword)
        print("Пароль введен")

    def click_ligin_btn(self):
        self.get_ligin_btn().click()
        print("Кнопка нажата ")

    # METHOD

    def autorez_met(self):
        with allure.step("autorez_met"):
            Logger.add_start_step(method="autorez_met")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_passsword("secret_sauce")
            self.click_ligin_btn()
            self.check_asser_world(self.get_asert_check(), "PRODUCTS")
            self.get_screenshot()
            Logger.add_end_step(url=self.get_current_url(),method="autorez_met")