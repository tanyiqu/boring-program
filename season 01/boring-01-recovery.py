"""
删除被批量创建的文件夹
参考：https://blog.csdn.net/weixin_42320142/article/details/102638638
"""
import os


def clean_dir():
    for i in range(100000):
        path = "C:\\"
        filename = path + str(oct(i))
        print(i)
        try:
            os.removedirs(filename)
        except FileNotFoundError:
            pass


clean_dir()
input('清理完成！')