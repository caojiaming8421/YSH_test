import time
from selenium.webdriver.common.by import By
from ysh_system import time_test


class Login_page():
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        name_input =self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div/input")
        name_input.send_keys("18673332009")
        time.sleep(0.5)

        pasw_input=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div[1]/div[2]/div/div/div/input")
        pasw_input.send_keys("123456")
        time.sleep(0.5)

        CAPTCHA_input=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div[1]/div[3]/div/div/div/input")
        CAPTCHA_input.send_keys("1")
        time.sleep(0.5)

        USER_PRIVACY_RADIO = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div[1]/div[4]/div/label/span[1]/span")
        USER_PRIVACY_RADIO.click()
        time.sleep(0.5)

        logs= time_test.time_test(self.driver)
        logs.process_after_loading("填充账号密码，勾选隐私保护")

        login_bt=self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/form/div[2]/div[1]/div[5]/div/button")
        login_bt.click()
        time.sleep(1)



