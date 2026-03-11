# 【新建文件夹并同时创建 Python 文件】
# 1) 在项目目录（Project 视图）中选中要创建的位置
# 2) 按快捷键 Ctrl + Shift + N（或右键 New）
# 3) 在弹出的“新建”菜单中选择 Python File
# 4) 输入路径形式的文件名：文件夹名/文件名.py
#    例如：module01/my_fun.py
# 5) 回车后会自动：新建文件夹 module01，并在其中创建 01_导入模块.py

#1.导入模块--->调用方式:模块名.功能名/别名.功能名

import random as rd
for i in range(4):
    print(rd.randint(3,3))#a>b会报错  a=b时就返回那个数本身

print('--------')

#2.导入模块中的功能 from...import..-->调用方式:功能名/别名
from random import randint as rint
for i in range(5):
    print(rint(5,10))

def log_666888():
    print("666888"*3)

PI = 3.1415926 #常量(不会发生变化的数据) 全大写定义常量
NAME = "zza"
print("-" * 30)# " - " 重复输出30次
__all__ = ['log_666888','NAME','PI']#如果用from 模块名 import* 只会调用被列出的功能

#测试函数
#__name__ : Python中的内置变量,表示当前模块的名字(直接运行当前模块,__name__的值为"__main__";当该模块被导入时,__name__的值就是模块名称
print(__name__)
if __name__ == '__main__':
    log_666888()