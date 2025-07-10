import time
import time_test
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from ysh_system.login_page.Login_page import Login_page
from ysh_system.menu.customer.crm_management.CustomerList import CustomerList
from ysh_system.menu.customer.crm_management.CustomerOpportunity import CustomerOpportunity
from ysh_system.menu.customer.crm_management.Customer_Public_Pool import Customer_Public_Pool
from ysh_system.menu.customer.crm_management.Customer import Customer
from ysh_system.menu.customer.sales_management.Sales_managment import Sales_managment


def resource_path(relative_path):
    """获取资源文件的绝对路径（支持打包环境）"""
    try:
        # PyInstaller创建的临时文件夹
        base_path = sys._MEIPASS
        print(f"资源基础路径 (打包环境): {base_path}")
    except AttributeError:
        # 在开发环境中，我们使用项目根目录（上一级目录）
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        print(f"资源基础路径 (开发环境): {base_path}")

    # 使用正确的路径分隔符
    full_path = os.path.join(base_path, *relative_path.split('/'))
    print(f"资源完整路径: {full_path}")

    # 验证路径是否存在
    if not os.path.exists(full_path):
        print(f"警告：资源文件不存在: {full_path}")

    return full_path

class ysh_main():

    def __init__(self):
        self.driver = None

    def open_browser(self): #打开浏览器
        chrome_options = Options()

        chrome_path = resource_path("chrome-win64/chrome.exe")
        chromedriver_path = resource_path("chromedriver.exe")

        # chrome_options.binary_location = r"C:\Users\Administrator\Desktop\自动化\YSH\chrome-win64\chrome.exe"  # 替换为你的 Chrome 实际路径
        # service = Service(
        #     executable_path=r'C:\Users\Administrator\Desktop\自动化\YSH\自动化工作流脚本\自动化工作流脚本\chromedriver.exe')
        chrome_options.binary_location = chrome_path
        service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://t1.ysh.ltd/pc/#/login")  # 打开目标页面
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入登录界面")

    def ysh(self): #进入登录页面
        login_page = Login_page(self.driver)
        login_page.login()
        time.sleep(0.5)

    def main_class(self):
        try:
            app = ysh_main()
            app.open_browser()
            app.ysh()
            logs = time_test.time_test(app.driver)
            logs.process_after_loading("登录成功")
            time.sleep(0.5)
            customer =Customer(app.driver) #客资管理
            name=customer.Customer_main_class()

            sales_managment = Sales_managment(app.driver)
            sales_managment.sales_main_class(name)

        except Exception as e:
            logs = time_test.time_test(app.driver)
            logs.process_after_loading(f"异常日志:{e}")
            print("异常",e)

if __name__ == "__main__":
    # 打印当前工作目录，帮助诊断问题
    print(f"当前工作目录: {os.getcwd()}")

    # 测试资源路径函数
    print("\n测试资源路径:")
    test_path = resource_path("chrome-win64/chrome.exe")
    app=ysh_main()
    app.main_class()
