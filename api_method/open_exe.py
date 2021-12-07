import os

def open_app(app_dir):
    """打开软件"""
    try:
        os.startfile(app_dir)
        """打开失败抛出异常"""
    except app_dir.error as info:
        print("文件路径或文件错误： s%ds" % info)


if __name__ == '__main__':
    app_dir1 = r"C:\FeigeDownload\192.168.2.64\AGVS1.8.23.0\AGVS-1.8.23.0\SystemManager.exe"
    open_app(app_dir1)
