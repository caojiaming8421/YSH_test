import time

from ysh_system import time_test
from ysh_system.menu.customer.crm_management.CustomerList import CustomerList
from ysh_system.menu.Service_Module.Work_Order_Center.WorkOrderManager import WorkOrderManager



class Work_Order():

    def __init__(self,driver):
        self.driver = driver

    def workOrdermanager(self):  #工单管理
        workOrdermanager = WorkOrderManager(self.driver)
        workOrdermanager.workOrdermanager()#进入工单管理
        time.sleep(0.5)
        logs = time_test.time_test(self.driver)
        logs.process_after_loading("进工单管理")
        name=workOrdermanager.add_workOrdermanager(1) #添加工单信息
        time.sleep(0.5)
        logs.process_after_loading("成功添加工单数据")
        return name #返回姓名

    def Work_Order_main_class(self):
        try:
            app = Work_Order(self.driver)
            name=app.workOrdermanager()  #工单中心
            return name

        except Exception as e:
            logs = time_test.time_test(app.driver)
            logs.process_after_loading(f"异常日志:{e}")
            print("异常",e)
            time.sleep(5)