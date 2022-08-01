try:
    from ctypes import *
except:
    libs = {'ctypes', \
            'beautifulsoup4'}
    for lib in libs:
        # 阿里云：http://mirrors.aliyun.com/pypi/simple/
        cmd = os.system('E:\python3.8.5\Scripts\pip.exe install -i https://pypi.tuna.tsinghua.edu.cn/simple ' + lib)
        #返回0表示成功，1则失败
        # os.system乱码的情况，在设置-编辑器-文件编码-设置全局UTF-8，两个编辑模式为GBK
        if(cmd == 1):
            print("PIP失效，请检查Python环境。\n未配置环境，程序无法运行")
            sys.exit(0)
        else:
            print("已使用PIP安装了所需的环境。")


dll = CDLL("D://Dll1//x64//Debug//Dll1.dll")
print(dll.myAdd(1, 102))