import random

from selenium.webdriver.common.by import By
import time
from ysh_system import time_test

class Customer_Public_Pool():
    def __init__(self, driver):
        self.driver = driver

    def customer_public_pool(self):

        if self.driver.find_elements(By.XPATH, "//*[text()='客户公海']")[0] is None or not self.driver.find_elements(By.XPATH, "//*[text()='客户公海']")[0].is_displayed():

            self.driver.find_elements(By.XPATH, "//*[text()='客户']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='客资管理']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='客户公海']")[0].click()
            time.sleep(0.5)
        else:
            self.driver.find_elements(By.XPATH, "//*[text()='客户公海']")[0].click()

    def add_customer_public_pool(self, a):

        xing =["曹","柯","李","廖","张","肖","柳","欧阳","赖"]
        ming =["龙","虎","凤","天明","炎","梓涵","阳","月","星","燕","问天","子龙"]

        for i in range(a):
            name=random.choice(xing) + random.choice(ming) #随机姓名
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/section/div/div[1]/div[2]/div[1]/div/button[1]").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='客户 ']/../div/div/div/div/div/input").send_keys(
                f"{name}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='客户代码 ']/../div/div/div/div/div/input").send_keys(
                f"kh_{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='地址 ']/../div/div/div/div/div/input").send_keys("宝安中心")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='客户身份 ']/../div/div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*/ul/li/span[text()='客户']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='联系人 ']/../div/div/div/div/div/input").send_keys("小明")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,
                                     "//*[text()='电话 ']/../div/div/div/div/div/input").send_keys("18673332008")
            time.sleep(0.5)

            logs = time_test.time_test(self.driver)
            logs.process_after_loading(f"填充公海客户信息:{name}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='确认']").click()
            time.sleep(1.5)
            self.driver.find_elements(By.XPATH,"//*[text()='更多']")[0].click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='领用']").click()
            time.sleep(0.5)
            logs.process_after_loading(f"领用客户信息:{name}")
        return name