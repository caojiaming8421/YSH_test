import random

from selenium.webdriver.common.by import By
import time
from ysh_system import time_test

class CustomerLead():
    def __init__(self, driver):
        self.driver = driver

    def customeropportunity(self):

        if self.driver.find_elements(By.XPATH, "//*[text()='客户线索']")[0] is None or not self.driver.find_elements(By.XPATH, "//*[text()='客户商机']")[0].is_displayed():

            self.driver.find_elements(By.XPATH, "//*[text()='客户']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='客资管理']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='客户线索']")[0].click()
            time.sleep(0.5)
        self.driver.find_elements(By.XPATH, "//*[text()='客户线索']")[0].click()

    def add_Opportunity(self, a ,name):

        for i in range(a):

            self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/section/div/div[1]/div[2]/div[1]/div/button[1]").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='线索名称 ']/../div/div/div/div/div/input").send_keys(f"客户线索{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='客户 ']/../div/div/div/div").click()
            time.sleep(0.5)
            if self.driver.find_elements(By.XPATH,f"//*[text()='{name}']")[0] is None:
                self.driver.find_element(By.XPATH,f"//*[text()='{name}']").click()
            else:
                self.driver.find_elements(By.XPATH, f"//*[text()='{name}']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH,"//*[text()='确定']")[1].click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='线索来源 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,f"//*/li/span[text()='熟人介绍']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='线索阶段 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH,f"//*/li/span[text()='探讨期']")[1].click()
            time.sleep(0.5)
            logs = time_test.time_test(self.driver)
            logs.process_after_loading(f"添加客户线索{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='确认']").click()
            time.sleep(0.5)