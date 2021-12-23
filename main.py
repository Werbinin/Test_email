from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexAutomate:
    def __init__(self):
        self.brauser = webdriver.Chrome(executable_path="C:\\Users\\Littre\\AppData\\Local"
                                                        "\\chromedriver\\chromedriver.exe")

    def login(self,email,password):
        self.brauser.get('https://passport.yandex.ru/auth/add?from=mail&origin=hostroot_homer'
                         '_auth_L_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3'
                         'A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1')
        self.brauser.find_element_by_xpath(
            '//input[@data-t="field:input-login"]'
        ).send_keys(email)
        self.brauser.find_element_by_xpath(
            '//button[@data-t="button:action:passp:sign-in"]'
        ).click()

        WebDriverWait(self.brauser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-t="field:input-passwd"]'))
        )

        self.brauser.find_element_by_xpath(
            '//input[@data-t="field:input-passwd"]'
        ).send_keys(password)
        self.brauser.find_element_by_xpath(
            '//button[@data-t="button:action:passp:sign-in"]'
        ).click()

if __name__ == "__main__":
    yandex = YandexAutomate()
    yandex.login('L1ttre99@yandex.ru', 'Yfhenj_99')