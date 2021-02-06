"""
弹出 “你的电脑正在被攻击” 提示的窗口，关闭后会再次显示。如果不会结束进程的话，那友尽程度可想而知！
不会对电脑有任何的损害
就是比较考验友情
参考：https://mp.weixin.qq.com/s/zIwGnevNiHlgmkeI2XVwXA
"""

import tkinter.messagebox

while True:
    tkinter.messagebox.showerror('Windows 错误', '你的电脑正在被攻击！')
