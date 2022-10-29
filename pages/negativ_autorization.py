import allure

from buse_page.buse import Buse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Negativ(Buse):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS

    user_name  = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"
    assert_negativ = "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out')]"


    # GETTERS

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_assert_negativ(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.assert_negativ)))


    # ACTIONS

    def input_user_name(self , user_name):
        self.get_user_name().send_keys(user_name)
        print("input loggin")

    def input_password(self,password):
        self.get_password().send_keys(password)
        print("input passord")

    def click_login_btn(self):
        self.get_login_btn().click()
        print("click login button")


    # METHOID

    def negativ_test_case(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("locked_out_user")
        self.input_password("secret_sauce")
        self.click_login_btn()
        self.check_asser_world(self.get_assert_negativ(),"Epic sadface: Sorry, this user has been locked out.")





