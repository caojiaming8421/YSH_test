import time
import os

time_stamp = time.strftime('%Y%m%d_%H%M%S')
i=1

class time_test():

    def __init__(self,driver):
        self.driver = driver
        # self.time_stamp = time.strftime('%Y%m%d_%H%M%S')

    def process_after_loading(self,function):  #截图  日志  信息保存
        global i

        try:
            base_dir= r"C:\Users\Administrator\Desktop\自动化\YSH\自动化测试"
            sub_dir=f"自动化测试_{time_stamp}"  # 子目录（带时间戳避免重复）
            target_dir = os.path.join(base_dir, sub_dir)  # 完整子目录路径

            # 创建基础目录（若不存在）
            if not os.path.exists(base_dir):
                os.makedirs(base_dir, exist_ok=True)  # exist_ok=True 避免目录已存在时报错
            # 创建子目录（若不存在）
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)

            screenshot_path = os.path.join(target_dir, f"自动化测试_{time.strftime('%Y%m%d_%H%M%S')}.png")
            self.driver.save_screenshot(screenshot_path)  # 保存截图
            print(f"截图已保存至：{screenshot_path}")

            # 生成日志文件
            log_path = os.path.join(target_dir, f"操作日志_{time_stamp}.txt")
            file_mode = "a" if os.path.exists(log_path) else "w"

            # 写入日志内容
            with open(log_path, file_mode, encoding="utf-8") as f:
                f.write(f"操作时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"目标页面：{self.driver.current_url}\n")
                f.write(f"截图路径：{screenshot_path}\n")
                f.write(f"功能描述：{function}\n")
                f.write(f"*********************************************第{i}次调用*****************************************************\n")
            print(f"日志已{'追加' if file_mode == 'a' else '新建'}至：{log_path}")
            i += 1
        except Exception as e:
            print(f"执行操作时发生错误：{str(e)}")