import os
import shutil
import PyInstaller.__main__
import sys


def build_executable():
    # 清理之前的构建文件
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')

    # 主脚本文件 - 使用绝对路径确保无误
    main_script = os.path.abspath('ysh_system/ysh_test.py')

    # PyInstaller 配置参数
    pyinstaller_args = [
        main_script,
        '--onefile',  # 打包成单个可执行文件
        '--console',  # 显示控制台窗口
        '--name=YSH_Automation',  # 生成的EXE文件名
        # '--icon=logo3.ico',  # 应用图标 - 暂时禁用
        '--add-data=chromedriver.exe;.',  # 添加chromedriver
        '--add-data=chrome-win64;chrome-win64',  # 添加Chrome浏览器
        '--paths=./',  # 添加项目根目录到搜索路径
        '--paths=./ysh_system',
        '--paths=./ysh_system/menu',
        '--paths=./ysh_system/menu/customer',
        '--paths=./ysh_system/menu/customer/crm_management',
        '--paths=./ysh_system/menu/customer/sales_management',
        '--paths=./ysh_system/menu/customer',
        '--paths=./ysh_system/menu/Service_Module/Work_Order_Center',
        '--hidden-import=time_test',  # 简化导入
        '--hidden-import=login_page',
        '--hidden-import=crm_management',
        '--hidden-import=CustomerList',
        '--hidden-import=Customer',
        '--hidden-import=CustomerLead',
        '--hidden-import=CustomerOpportunity',
        '--hidden-import=Customer_Public_Pool',
        '--hidden-import=sales_management',
        '--hidden-import=Customer_Follow_Up',
        '--hidden-import=Sales_managment',
        '--hidden-import=Work_Order_Center',
        '--hidden-import=WorkOrder',
        '--hidden-import=WorkOrderManager',
        '--clean',  # 清理临时文件
        '--noconfirm',  # 覆盖输出目录而不确认
        '--log-level=WARN'  # 减少日志输出
    ]

    # 执行打包
    try:
        PyInstaller.__main__.run(pyinstaller_args)
    except Exception as e:
        print(f"打包失败: {str(e)}")
        return

    print("\n" + "=" * 50)
    print("打包完成！EXE文件在 dist 目录下")
    print("=" * 50)

    # 复制资源文件到dist目录
    dist_dir = os.path.join('dist')
    if os.path.exists(dist_dir):
        try:
            # 复制chromedriver
            shutil.copy('chromedriver.exe', dist_dir)

            # 复制Chrome浏览器
            chrome_src = 'chrome-win64'
            chrome_dest = os.path.join(dist_dir, 'chrome-win64')
            if os.path.exists(chrome_src):
                # 使用 shutil.copytree 复制目录
                if os.path.exists(chrome_dest):
                    shutil.rmtree(chrome_dest)
                shutil.copytree(chrome_src, chrome_dest)

            # 尝试添加图标（如果存在）
            if os.path.exists('logo3.ico'):
                try:
                    # 使用 rcedit 添加图标
                    import subprocess
                    exe_path = os.path.join(dist_dir, 'YSH_Automation.exe')
                    if os.path.exists(exe_path):
                        subprocess.run([
                            'rcedit',
                            exe_path,
                            '--set-icon', 'logo3.ico'
                        ], check=True)
                        print("图标已添加到EXE文件")
                    else:
                        print("警告: EXE文件未找到")
                except Exception as e:
                    print(f"添加图标失败: {str(e)}")

            print("资源文件已复制到dist目录")
        except Exception as e:
            print(f"复制资源文件失败: {str(e)}")

    # 创建压缩包方便分发
    try:
        shutil.make_archive('YSH_Automation', 'zip', dist_dir)
        print("已创建压缩包: YSH_Automation.zip")
    except Exception as e:
        print(f"创建压缩包失败: {str(e)}")


if __name__ == "__main__":
    # 确保安装必要依赖
    try:
        import Pillow
    except:
        print("安装Pillow库...")
        os.system("pip install Pillow")

    build_executable()