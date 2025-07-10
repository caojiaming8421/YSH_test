import time

from ysh_system import time_test
from ysh_system.menu.customer.sales_management.Customer_Follow_Up import Customer_Follow_Up


class Sales_managment():

    def __init__(self,driver):
        self.driver = driver

    def customer_follow(self,name):  #客户列表
        customer_follow = Customer_Follow_Up(self.driver)
        customer_follow.customer_follow_up() #进入客户列表
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入客户跟单")
        customer_follow.add_follow(1,name) #添加客户信息，循环次数
        time.sleep(0.5)
        logs.process_after_loading("成功添加客户跟单")
        return name #返回姓名

    def sales_main_class(self,name):
        try:
            app = Sales_managment(self.driver)
            app.customer_follow(name)  #客户跟单

        except Exception as e:
            logs = time_test.time_test(app.driver)
            logs.process_after_loading(f"异常日志:{e}")
            print("异常",e)
            time.sleep(5)