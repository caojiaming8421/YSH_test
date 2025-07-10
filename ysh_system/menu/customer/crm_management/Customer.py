import time

from ysh_system import time_test

from ysh_system.menu.customer.crm_management.CustomerList import CustomerList
from ysh_system.menu.customer.crm_management.CustomerOpportunity import CustomerOpportunity
from ysh_system.menu.customer.crm_management.Customer_Public_Pool import Customer_Public_Pool
from ysh_system.menu.customer.crm_management.CustomerLead import CustomerLead


class Customer():

    def __init__(self,driver):
        self.driver = driver

    def customerList(self):  #客户列表
        customerList = CustomerList(self.driver)
        customerList.customerlist() #进入客户列表
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入客户列表")
        name=customerList.add_customer(1) #添加客户信息，循环次数  获取最后一位客户的姓名
        time.sleep(0.5)
        logs.process_after_loading("成功添加客户")
        return name #返回姓名

    def customeropportunity(self,name): #客户商机
        customeropportunity = CustomerOpportunity(self.driver)
        customeropportunity.customeropportunity() #进入客户商机
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入客户商机")
        customeropportunity.add_Opportunity(1,name) #添加商机信息，循环次数
        time.sleep(0.5)
        logs.process_after_loading("成功添加商机")

    def customer_public_pool(self):  #客户列表
        customer_public_pool = Customer_Public_Pool(self.driver)
        customer_public_pool.customer_public_pool() #进入客户公海
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入客户公海")
        name=customer_public_pool.add_customer_public_pool(1) #添加客户公海信息，循环次数  获取最后一位客户的姓名
        time.sleep(0.5)
        logs.process_after_loading("成功添加客户公海信息")
        return name #返回姓名

    def customerLead(self,name):  #客户线索
        customerLead = CustomerLead(self.driver)
        customerLead.customeropportunity() #进入客户线索
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进入客户线索")
        customerLead.add_Opportunity(1,name) #添加客户线索 信息，循环次数
        time.sleep(0.5)
        logs.process_after_loading("成功添加客户线索信息")

    def Customer_main_class(self):
        try:
            app = Customer(self.driver)
            name=app.customerList()  #客户列表  获取最后一位客户的姓名
            app.customeropportunity(str(name)) #客户商机
            name=app.customer_public_pool() #客户公海  获取最后一位客户的姓名
            app.customerLead(name) #客户线索
            return name

        except Exception as e:
            logs = time_test.time_test(app.driver)
            logs.process_after_loading(f"异常日志:{e}")
            print("异常",e)
            time.sleep(5)