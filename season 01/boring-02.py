"""
不断弹出窗口的小程序，如果没有结束进程的话，最多显示100个
不会对电脑有任何的损害
就是比较考验友情
参考：https://mp.weixin.qq.com/s/zIwGnevNiHlgmkeI2XVwXA
改进：tanyiqu
"""

import tkinter as tk
import random
import threading
import time


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('你是一个傻狍子')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='你是一个傻狍子', bg='green',
             font=('宋体', 17), width=20, height=4).pack()
    window.mainloop()
    pass


threads = []
for i in range(100):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
    pass
