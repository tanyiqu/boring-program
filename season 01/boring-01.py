"""
在C盘不断创建文件夹的小程序，如果不关闭的话，最多创建10w个
不会对电脑有任何的损害
就是比较考验友情
参考：https://blog.csdn.net/weixin_42320142/article/details/102638638
改进：tanyiqu
"""
import os
import sys


def mkdir():
    path = 'C:\\'  # 创建文件路径
    i = 1
    while i < 100000:  # 创建文件个数
        try:
            file_name = path + str(oct(i))
            os.mkdir(file_name)
            print(i)
            pass
        except Exception:
            pass
        finally:
            i = i+1
            pass
        pass
    pass


mkdir()
input('你竟然看完了没有关掉！恭喜你的C盘喜提100,000个文件夹！！')
input('谁让你运行这个的，你就找谁要删除工具去吧！')