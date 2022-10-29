import datetime


class Buse():
    def __init__(self , driver):
        self.driver = driver



    """CURRENT URL"""
    def get_current_url(self):
       get_utl =  self.driver.current_url
       print("Получаем путь к " + get_utl)

    """ASSERT WORLD"""
    def check_asser_world(self , world, result):
        value_world = world.text
        assert value_world == result
        print(" Проверка ключевого слова  пройдена  ")


    """SCREENSHOT MRTHOD"""

    def get_screenshot(self):
        new_date = datetime.datetime.utcnow().strftime("%Y, %m , %d , %H, %M , %S")
        name_screenshot = "screenshot " + new_date + ".png"
        self.driver.save_screenshot("/Users/user/Desktop/test_com_saucedemo_htts/screenshot/" + name_screenshot)
        print("Скриншот добавлен")









