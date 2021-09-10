import ctypes
import sys
import os
import getpass
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():


    # pip加速代码
    file_data = """[global]
    trusted-host=mirrors.aliyun.com
    index-url=http://mirrors.aliyun.com/pypi/simple/
    """
    # 获取当前时间
    atime = time.time()
    # 开始
    print("开始进行pip加速...")
    # 等待两秒
    time.sleep(2)
    # 判断文件是否已存在，如果已存在就删除文件
    if os.path.exists(f"C://Users//{getpass.getuser()}//pip//pip.ini"):
        # 创建文件并打开
        f = open(f"C://Users//{getpass.getuser()}//pip//pip.ini", "w")
        # 写入文件
        f.write(file_data)
        # 关闭文件
        f.close()
        # 结束
        print(f"pip加速成功，你的pip将会很快（本次耗时：{time.time() - atime}秒）")
        # 按任意键继续
        os.system("pause")
    elif os.path.exists(f"C://Users//{getpass.getuser()}//pip"):
        os.rmdir(f"C://Users//{getpass.getuser()}//pip")

    else:
        # 创建目录
        os.mkdir(f"C://Users//{getpass.getuser()}//pip")
        # 创建文件并打开
        f = open(f"C://Users//{getpass.getuser()}//pip//pip.ini", "w")
        # 写入文件
        f.write(file_data)
        # 关闭文件
        f.close()
        # 结束
        print(f"pip加速成功，你的pip将会很快（本次耗时：{time.time() - atime}秒）")
        # 按任意键继续
        os.system("pause")
else:
    # Re-run the program with admin rights

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



