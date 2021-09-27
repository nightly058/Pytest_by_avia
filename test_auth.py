import time
from selenium import webdriver
from datetime import datetime
from datetime import timedelta
#from selenium.webdriver.support.ui import WebDriverWait
# Github credentials
class TestPageSearch:
    def setup (self):
        self.driver = webdriver.Chrome("chromedriver")
    def test_search (self):
        username = "a.kalyamin@smartway.today"
        password = "58SdjWerPoz"
        city1 = "Moscow"
        city2 = "Samara"
        # initialize the Chrome driver
        self.driver.get("https://rc.gospodaprogrammisty.ru/login")
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1920,1080)
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_css_selector("[data-qa='sign-in-form-button']").click()

        time.sleep(10)
        #Вводим города вылета прилета, прокликиваем
        self.driver.get("https://wp.rc.gospodaprogrammisty.ru/search/airline")
        time.sleep(10)
        self.driver.find_element_by_css_selector("[placeholder='Город вылета']").send_keys(city1)
        time.sleep(2)
        self.driver.find_element_by_css_selector("[class='item_3rli focus_1ueU']").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("[placeholder='Город прилета']").send_keys(city2)
        time.sleep(2)
        self.driver.find_element_by_css_selector("[class='item_3rli focus_1ueU']").click()

        #Выбираем текущую дату
        self.driver.find_element_by_css_selector("[placeholder='Туда']").click()
        self.driver.find_element_by_xpath("//*[@id=\"search-box\"]/div[2]/div/div[2]/div/div[1]/div[2]/button").click()
        time.sleep(30)

        #Выбераем первый результат поиска
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/button").click()
        time.sleep(5)
        #Переходим в корзину
        self.driver.find_element_by_xpath("//*[@id=\"main-header-items-wrapper\"]/div/div[2]/div/div/a/div[2]").click()
        time.sleep(5)
        #Берем справку
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/label/div[2]/div").click()
        time.sleep(5)
        #Выпалающий список сотрудников
        self.driver.find_element_by_xpath("//*[@id=\"main-header-items-wrapper\"]/div/div[2]/div/div/a/div[2]").click()
        time.sleep(5)
        #Берем первого сотрудника
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/button").click()
        time.sleep(5)
        #Чек бокс подтверждения оплаты
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]").click()
        time.sleep(2)
        #Оплата
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[1]/div/div[5]/div[2]/div/button").click()
        time.sleep(2)
        #Чек бокс оплаты
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[4]/div[2]/div[3]/label/div[2]").click()
        time.sleep(2)
        #Оплата
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/div/div[4]/div[2]/div[4]/button").click()
        time.sleep(20)
        #Попадаем на страницу после оплаты (берем данные с блока справки)
        element = self.driver.find_element_by_xpath ("//*[@id=\"root\"]/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div[1]")
       # Проверяем текст о наличии справки
        assert element.text == 'Справка о совершенном перелете'