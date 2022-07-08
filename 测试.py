import os,sys
try:
    import platform
    import requests
except:
    print("over")
    sys.exit(0)
    libs = {'requests', \
            'beautifulsoup4'}
    for lib in libs:
        #'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ' + lib
        cmd = os.system('E:\python3.8.5\Scripts\pip.exe install -i https://pypi.tuna.tsinghua.edu.cn/simple ' + lib)
        #返回0表示成功，1则失败

        if(cmd == 1):
            print("PIP失效，请检查Python环境。\n未配置环境，程序无法运行")
            sys.exit(0)
        else:
            pass
        #os.system乱码的情况，在设置-编辑器-文件编码-设置全局UTF-8，两个编辑模式为GBK
        #阿里云：http://mirrors.aliyun.com/pypi/simple/
sys.exit(0)
url = "https://www.bing.com/"
requests.get(url)

if __name__ == '__main__':
    sys = platform.system()
    if sys == "Windows":
        print("OS is Windows!!!")
    elif sys == "Linux":
        print("OS is Linux!!!")
        pass
    else:
        print("非Windows和Linux的系统暂不支持，程序退出！")
        sys.exit(0)