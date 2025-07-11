import random
import pyautogui
from selenium.webdriver.common.by import By
import time
from ysh_system import time_test

class WorkOrderManager():
    def __init__(self, driver):
        self.driver = driver

    def workOrdermanager(self):

        if self.driver.find_elements(By.XPATH, "//*[text()='工单管理']")[0] is None or not self.driver.find_elements(By.XPATH, "//*[text()='工单管理']")[0].is_displayed():

            self.driver.find_elements(By.XPATH, "//*[text()='服务']")[0].click()
            time.sleep(0.5)
            self.driver.find_elements(By.XPATH, "//*[text()='工单中心']")[0].click()
            time.sleep(0.5)
            # self.driver.find_elements(By.XPATH, "//*[text()='工单管理']")[0].click()
            time.sleep(0.5)
        else:
            self.driver.find_elements(By.XPATH, "//*[text()='工单管理']")[0].click()

    def add_workOrdermanager(self, a):

        for i in range(a):
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[2]/section/div/div[1]/div/div[5]/div/div[1]/button").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*/li[text()='场地勘测']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='员工 ']/../div/div/div/div").click()
            time.sleep(1)

            self.driver.find_element(By.XPATH, f"//div[div[text()='小明2009']and div[text()='18673332009']]").click()

            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='客户 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='工单编号 ']/../div/div/div/div/div/input").send_keys(f"GD{time.strftime('%Y%m%d_%H%M%S')}")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, f"//*/span[text()='请选择客户']/../../div/div/div[2]/div[5]/div[2]/div").click()
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='地区 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='广东省']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='深圳市']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='宝安区']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='商品 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*/span[text()='请选择商品']/../../div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div").click()
            time.sleep(0.5)
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            self.driver.find_element(By.XPATH, "//*[text()='产品 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*/label/span[text()='全部']").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*/span[text()='请选择产品']/../../div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div").click()
            time.sleep(0.5)
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            self.driver.find_element(By.XPATH, "//*[text()='服务报价 ']/../div/div/div/div").click()
            time.sleep(0.5)
            try:
                self.driver.find_element(By.XPATH,
                                         "//*/span[text()='请选择服务报价']/../../div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div").click()
                time.sleep(0.5)
            except Exception as e:
                print("没有服务报价")
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                print(btn.is_displayed)
                if btn.is_displayed():
                    btn.click()
            self.driver.find_element(By.XPATH, "//*[text()='故障类型 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*/span[text()='安装问题']/../../label/span").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='优先级 ']/../div/div/div/div").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*/li/span[text()='优先']/..").click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='故障描述 ']/../div/div/div/div/textarea").send_keys("快来啊，机器滴滴的响个不停")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='点击上传文件 ']/..").click()
            # 等待窗口出现
            time.sleep(1)
            pyautogui.write(r"C:\Users\Administrator\Pictures\test.jpg")
            time.sleep(1)
            pyautogui.hotkey("enter")
            time.sleep(0.5)
            pyautogui.hotkey('alt', 'o')
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[text()='服务车辆 ']/../div/div/div/div").click()
            time.sleep(0.5)
            try:
                self.driver.find_element(By.XPATH,
                                         "//*/span[text()='请选择服务车辆']/../../div/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div").click()
                time.sleep(0.5)
            except Exception as e:
                print("没有服务车辆")
            time.sleep(0.5)
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    print(btn.is_displayed())
                    btn.click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='预期服务时间 ']/../div/div/div/div").click()
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//*[text()='预期结束时间 ']/../div/div/div/div").click()
            for btn in self.driver.find_elements(By.XPATH, "//*[text()='确定']"):
                if btn.is_displayed():
                    btn.click()
            time.sleep(0.5)
            logs = time_test.time_test(self.driver)
            logs.process_after_loading(f"填充工单信息:")
            time.sleep(0.5)
            self.driver.find_element(By.XPATH,"//*[text()='确认']").click()
            time.sleep(1)
