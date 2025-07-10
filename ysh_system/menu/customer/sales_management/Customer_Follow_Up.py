
import time

from selenium.webdriver.common.by import By
from ysh_system import time_test

class Customer_Follow_Up():
    def __init__(self, driver):
        self.driver = driver

    def customer_follow_up(self):

        if self.driver.find_elements(By.XPATH, "//*[text()='客户跟单']")[0] is None or not self.driver.find_elements(By.XPATH, "//*[text()='客户跟单']")[0].is_displayed():

            self.driver.find_element(By.XPATH, "//*/div/span[text()='客户']").click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='销售管理']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='客户跟单']")[0].click()
            time.sleep(0.5)
        self.driver.find_elements(By.XPATH, "//*[text()='客户跟单']")[0].click()

    def add_follow(self, a ,name):

        for i in range(a):

            self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/section/div/div[1]/div[2]/div[1]/div/button[1]").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='标题 ']/../div/div/div/div/div/input").send_keys(f"客户跟单{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='客户 ']/../div/div/div/div").click()
            time.sleep(0.5)
            if self.driver.find_elements(By.XPATH,f"//*[text()='{name}']")[0] is None:
                self.driver.find_element(By.XPATH,f"//*[text()='{name}']").click()
            else:
                self.driver.find_elements(By.XPATH, f"//*[text()='{name}']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH,"//*[text()='确定']")[2].click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='联系人 ']/../div/div/div/div/div/input").send_keys(f"小明")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='跟单内容 ']/../div/div/div/div/textarea").send_keys(f"18673332008")
            time.sleep(0.5)
            logs = time_test.time_test(self.driver)
            logs.process_after_loading(f"添加客户跟单{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='确认']").click()
            time.sleep(0.5)