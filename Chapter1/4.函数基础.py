#1.1 函数是组织好的,可重复使用的,用来实现特定功能的代码片段
# 函数定义时：只“记住”函数'不执行函数体里的代码
# 调用函数时：才真正执行函数体

#1.2 函数的定义与调用 : 必须先定义后调用
# #def 函数名(参数列表):    参数列表可有可无
#     函数体
#     return 返回值       有return,返回一个结果;没有return,返回None
def add(a, b):
    return a + b
result = add(3, 5)
print(result)   # 输出 8

def out_line():# 函数定义时：只记不执行;调用函数时：函数体的逻辑才会执行
    print("---------------")#通过缩进描述归属关系
    print("---------------")
out_line()#python从上往下执行代码

#1.21案例计算圆的面积
def circle_area(r):
    area = 3.14 * r * r  # *r ** 2
    return area
c_area = circle_area(10)#10 实际参数:函数在实际调用时传入的参数
print(c_area)

#1.22计算长方形的面积
def rectangle_area(l, w):# l,w 形式参数:函数定义时括号里的参数,只能在函数内使用(局部变量)
    '''根据长,宽计算长方形的面积
    :param l: 长方形的长
    :param w: 长方形的宽
    :return: 此长方形的面积
    '''
    area = l * w
    return area#return只返回不打印
r_area = rectangle_area(20, 10)#函数定义时如果有多个参数,参数之间用,分隔
print(r_area)

#1.23计算圆的面积,周长--->如果返回值有多个,多个返回值之间逗号分割
def circle_area_len(r):
    return round(3.14 * r * r ,1), round(2 * 3.14 *r ,1)#round(number,ndigits) 内置函数,需保留的位数,四舍五入
al = circle_area_len(10)
print(al)
print(type(al))#tuple 封装在元组中
area,length = circle_area_len(10)#元组解包
print(area)
print(length)

#1.3函数说明文档Docstring 写在函数开头,用三个引号包裹的字符串,用于解释函数的功能,参数,返回值
def circle_area_len(r):
    """根据圆的半径,计算圆的面积和周长
    :param r: 圆的半径
    :return: 圆的半径,圆的周长
    """
    return round(3.14 * r * r ,1), round(2 * 3.14 *r ,1)#round(number,ndigits) 内置函数,需保留的位数,四舍五入
al = circle_area_len(10)
print(al)
#1.31查看函数说明文档 使用help函数 help(circle_area_len)
#1.32鼠标悬浮在函数上,自动展示 ---->Consistency & Context
help(rectangle_area)

#1.4函数的嵌套调用---在一个函数中又调用了另外一个函数
#函数调用遵循栈结构,最后被调用的函数最先返回LIFO(Last in First Out,后进先出) 进入函数:压栈push;函数结束:出栈pop
def function_a():
    print(">> enter A")
    print("a...before")#a开始,还未调用b
    function_b()
    print("a...after")#调用b已经结束,继续执行a剩余操作
    print("<< leave A")

def function_b():
    print("  >> enter B")
    print("  b...before")#a已经调用b,b还未调用c
    function_c()
    print("  b...after")#b已经调用完c,执行剩余b
    print("  << leave B")

def function_c():
    print("    >> enter C")
    print("    c...")
    print("    << leave C")

function_a()
print("函数调用完成")

#1.51案例:定义一个根据底和高计算三角形面积的函数
def triangle_area(d,h):
    """
    根据传入的底和高计算三角形的面积
    :param d: 底
    :param h: 高
    :return: 三角形面积
    """
    return d * h /2
print('底为30,高为20的三角形面积:',triangle_area(30,20))

#1.52案例:定义一个计算传入字符串中元音字母数量的函数(AEIOUaeiou)
def count_vowel(s):
    """
    统计字符串中元音字母的个数
    :param s:字符串
    :return:元音字母个数
    """
    num=0
    for w in s:
        if w.lower() in 'aeiou':#.lower() 调用函数 把字符全部转成小写 括号()不能少
            num+=1
    return num#1for循环完成全部遍历后再return
print(count_vowel('Hello Python haha wow'))

#1.53案例:定义一个函数,计算传入的班级学院高考成绩的列表来计算最高分,最低分,平均分(保留一位小数),并返回
def calculate_score(score_list):
    """
    计算传入成绩的最高分,最低分,平均分
    :param score_list: 分数列表
    :return: 最高分,最低分,平均分
    """
    max_s = max(score_list)#内置函数
    min_score = min(score_list)
    avg_s = round(sum(score_list) / len(score_list),1)#禁止把sum,len等内置函数设置为变量名,否则后续报错很难回溯
    return max_s, min_score, avg_s

s_list=[589,605,609,643,677,455,477,489,503]
max_score, min_score, avg_score = calculate_score(s_list)
print('最高分',max_score)
print('最低分',min_score)
print('平均分',avg_score)

#1.54作业:定义一个函数:完成时间转换功能,将传入的秒转换为小时,分钟,秒
def time_converter():
    """
    此函数用于将秒数转换为小时,分钟,秒
    :return: 小时,分钟,秒
    """
    seconds = 36657
    hours = seconds // 3600#整除
    minutes = (seconds % 3600) // 60#算完小时后所得余数再除60算分钟
    seconds = seconds % 60
    print('result')
    print ('hours:',hours,'minutes:',minutes,'seconds:',seconds)
time_converter()

#1.55作业:定义一个函数:根据传入的分数判断对应等级并返回 >=90-A;>=75-B;>=60-C;<60-DA
def grade_level(score):
    """
    输入一个分数 score，返回对应等级：
    >=90: A
    >=75: B
    >=60: C
    <60 : D
    :param score: 分数
    :return: 对应等级
    """
    try:
        score = float(score)#将字符串转为数字
    except (TypeError, ValueError):
        raise ValueError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError

    if score >= 90:
        return "A"
    elif score >= 75:#elif 否则如果 确保结果只会命中一个分支
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

for s in [95, 80.7, 60, 59, "88"]:
    print(s, "->", grade_level(s))

#1.6 变量作用域
#全局变量:在函数之外定义的变量,在整个文件中(包括函数内)都可以使用,通常定义在文件顶部
#局部变量:在函数内部定义的变量,只能在该函数内部使用
num = 100
def circle_area(r):
    """Return the area of a circle with radius r."""
    pi = 3.14          # 局部变量：只在函数内部有效
    area = pi * r * r  # 局部变量：只在函数内部有效
    num = 10000
    print('num =', num)
    return area

c_area = circle_area(10)
print("circle_area(10) =", c_area)
print('num =', num)#函数运行结束后局部变量失效

#1.61 global关键字 在函数中需使用全局变量,允许在函数内部修改全局变量的值
def function_nb():
    global num
    num = 999
    return num
print('before num',num)
function_nb()
print('after call the function',num)
#注:尽量避免在函数中使用全局变量,会使代码难以维护和调试//考虑使用函数参数和返回值传递数据,不依赖全局变量

#1.62
"""global 的应用场景 —— 调试开关 debug_mode

核心思想：
- debug_mode 是“全局状态/开关”，希望多个函数都能读到它的最新值
- 在函数内部如果要“修改”全局变量，必须用 global 声明
  否则会创建同名的“局部变量”，全局变量不会变

应用场景：
- 调试模式开关（是否打印调试信息）
- 全局配置、程序状态（例如 verbose、is_login 等）
"""
# 1) 调试开关（全局变量）
debug_mode = False  # 默认关闭调试模式

# 2) 开启调试模式：需要修改全局变量 => 必须使用 global
def enable_debug_mode():
    global debug_mode       # 声明：下面操作的是“全局 debug_mode”
    debug_mode = True
    print("调试模式已开启")

# 3) 关闭调试模式：同样需要 global
def disable_debug_mode():
    global debug_mode
    debug_mode = False
    print("调试模式已关闭")

# 4) 日志函数：只读取全局变量（读取不需要 global）
def log(msg):
    if debug_mode:#暗含条件判断 if debug_mode = True
        print("[DEBUG]", msg)#告诉用户现在 是/不是 在调试模式

enable_debug_mode()
log("hello")#返回值,证明现在是调试阶段
disable_debug_mode()
log("hello")#不返回值

#1.7 函数参数详解
#1.71函数的传参方式(实参)

#1.711位置参数:调用函数时根据函数定义时的位置来传递参数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名:{name}，年龄:{age}，性别:{gender}，城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

stu = reg_stu("张三", 18, "男", "北京")
print(stu)#要求:调用函数时参数顺序与定义函数时参数顺序完全一致

#1.712关键字参数:调用函数时以函数定义时形参名称作为关键字,以"键-值"形式来传递参数(不要求顺序)
stu2 = reg_stu(gender = "男",age = 19, city = '上海', name = "小刺老")
print(stu2)
stu3 = reg_stu("洋芋粑", 20, city = '贵阳', gender = "男")#若位置参数和关键字参数混用,关键字参数必须在位置参数之后(关键字参数间无位置要求)
print(stu3)

#1.713位置参数 VS 关键字参数
#位置参数----简洁,但可读性差,易出错,难维护>>>参数少,顺序自然
#关键字参数----可读性强,易于维护和扩展,但代码繁琐>>>参数多,易混淆
#黄金法则:半年后再看此代码能否快速看出参数对应的含义,如果不能,应使用关键字参数

#1.72 默认参数 也称 缺省参数,在定义函数时,为参数提供默认值,调用函数时,可以不传递有默认值的参数
def greet(name, city="北京"):
    print(f"你好，{name}，来自{city}")

greet("张三")          # 使用默认参数   不说就当没改
greet("李四", "上海")  # 覆盖默认参数

#1.73 不定长参数 也称可变参数,定义及调用函数时参数个数不确定时使用
#1.731 *基于位置参数的不定参数,args--arguments 参数
def calc_data(*args):
    return sum(args)
data = calc_data(10,20,30,40,50,60,70,80,90,100)
print(data)
data = calc_data(100,200,300,400,500)#传递的所有匹配的位置参数都被args收集,合并封装为元组tuple
print(data)

#1.732 ** 基于关键字传递的不定长参数 kwargs--key-word arguments
def calc_data(*args, **kwargs):
    """
    根据传入的这批数据,计算最小值,最大值,平均值
    :param args: 不定长位置参数
    :param kwargs:不定长关键字参数
        round:保留的小数位数
        print:是否打印输出
    :return:
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get('round') is not None:# 如果传入了 round 这个关键字参数，就对平均值进行四舍五入
        avg_data = round(avg_data, kwargs.get('round'))
    if kwargs.get('print') :
        print("计算出的值分别为")
    return min_data, max_data, avg_data

data = calc_data(79, 38, 300, 400, round=2, print = True)#参数是以"键-值"形式传递的关键字参数,它们被kwargs接受,封装为一个字典类型dict
print(data)#除不尽保留两位小数,打印计算结果

data = calc_data(33, 11, 28, 91, 32, 75, 49,round=4,print = False)#除不尽时保留4位
print(data)#False后 不打印'计算出的值分别为', 仍会打印返回的元组 round=4执行了

"""
小结： *args：
   - 不定长位置参数
   - 函数调用时，通过位置参数传递多个参数
   - 会将多个参数封装到一个元组（tuple）中

     **kwargs：
   - 不定长关键字参数
   - 函数调用时，通过关键字参数传递多个参数
   - 会将多个参数封装到一个字典（dict）中

   *args：适用于处理数量不确定的 数据 (要什么 要奶茶)
   **kwargs：适用于处理数量不确定的 选项(甜度,温度,杯型) ; 常作为函数的配置参数，用来定制函数的行为

    同时存在时要先写位置参数再写关键字参数
"""

#1.74 函数的参数类型
#普通参数:数字,布尔,字符串,列表,元组,集合,字典    特殊参数:函数
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def calculate(x,y,oper):
    return oper(x,y)
result = calculate(10,20,multiply)#10,20 实际要计算的数据  ;  add 函数中封装的加法逻辑
print(result)

#1.8 匿名函数
#定义匿名函数    lambda 参数:函数体逻辑
adds = lambda x,y: x + y#匿名函数无法直接通过函数名调用 需赋给变量使用
result = adds(99,11)
print(result)#匿名函数中可自定是否返回结果 返回结果时不需要写return 表达式运行的结果就是要返回的结果
#使用场景:函数逻辑比较简单,且只在一个地方使用时,考虑使用匿名函数 (通常作为高阶函数的参数使用)

#1.81需求:打印分割线
out_line = lambda : print("---------------------------------")
out_line()

#1.82需求:计算两个数之和
ADD = lambda x,y : x+y
print(ADD(66,88))

#1.83需求:按照每个元素的字符个数,从小到大排序
data_list = ['C++','C,''Python','Java','JavaScript','PHP','GO','Rust']
data_list.sort(key = lambda item : len(item))#依据元素字符个数排序
# sort() 排序列表；key 指定排序依据；lambda item: len(item) 用元素长度作为排序键，默认升序（短→长）
print(data_list)

#1.91 案例1:f(n) = n * f(n-1)
#递归 recursion :函数中,自己调用自己--->需要有终结点
def jc(n):
    '''
    此函数用于计算n的阶乘
    :return: 阶乘的结果
    '''
    if n == 1:
        return 1
    else:
        return n * jc(n-1)

result = jc(10)
print(result)

#1.92 案例2 定义一个函数,用于根据传入的一批商品信息(商品名,价格,数量),优惠(券,积分抵扣),运费信息计算总金额
#具体规则:优惠券,积分都需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价,100积分抵扣1元(只能整百抵扣)
def cacl_order_cost(*args,coupon,score,express):
    '''
    :param args: 商品信息(名称,价格.数量)--->('鼠标',188,2) ('键盘',599,1)
    :param coupon:优惠劵
    :param score:积分
    :param express:运费
    :return:订单总金额
    '''
    #订单总金额=原价-优惠券-积分抵扣+运费(验证条件)

    #1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    #2.扣减优惠券,积分
    if total_cost > coupon and total_cost > 5000:
        total_cost = total_cost - coupon
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    #3.加运费
    total_cost = total_cost + express

    return total_cost

print(cacl_order_cost(('鼠标',188,2),('键盘',599,1),('手机',7999,1),coupon = 500 ,score = 4000,express = 25))

#2.01 类型注解:python中的一种语法特性,用于明确标识变量,函数参数和返回值的数据类型--->变量 : 数据类型(a : int)
#特点:让代码结构更清晰,易维护,更准确的代码自动提示
a2: int =596
a1 = 332#类型推断:python解释器自动推断出变量,表达式或函数返回值的数据类型的能力,无需开发者显式声明
score2: float = 98.5#悬浮可视
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str] = ["A", "C", "E"]#只能添加同类型的数据
phones2: set[str|int] = {"13309091111", "1520910902", "18809019201"}#用 | 分割可接受的多种数据类型
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 7999, 1)
phones2.add(100)     #类型注解只起到语法提示作用,并不影响程序运行结果
print(phones2)

#2.02 函数类型注解
# 函数定义（带类型注解）
'''
参数用 : 数据类型  的方式注解;返回值 在def后的参数括号()后用 -> 数据类型 注解
def cacl_order_cost(*args : tuple[str,float,int],coupon : int = 0,score : int = 0,express : int =0)->float
'''

#2.1 Python模块(module)
#定义:一个.py文件就是一个模块,模块是Python程序的基本组织单位.在模块中可以定义变量,函数, 类, 以及可执行的代码
#作用:提高代码复用性,便于真实工程项目scaling up,拆分功能,协作分工
#e.g. 4.函数基础.py为自定义模块 Python有许多内置模块 如 math(数学计算),os(操作系统),random(随机数),sys(系统参数).datetime(日期时间)

#2.11 需求 随机点名器
import random
names = ['zrh','zsj','hhd','xyf','ydm','tyz','ysp','lyh','hhr','lym',None]#None会被等概率抽到并返回
print(random.choice(names))#独立同分布,有放回抽样

#2.12 模块导入方式
''''| 导入形式 | 代码样例 | 调用方式 | 调用示例 |
    | import 模块名                    | `import random, os`                   | 模块名.功能名 | `random.randint(10, 100)` 
    | import 模块名 as 别名             | `import random as rd`                 | 别名.功能名  | `rd.randint(10, 100)`       
    | from 模块名 import 功能名          | `from random import randint, choice` | 功能名  | `randint(10, 100)`              
    | from 模块名 import 功能名 as 别名   | `from random import randint as rint` | 别名  | `rint(10, 100)`                  
    | from 模块名 import *              | `from random import *`               |  功能名 | `randint(10, 100)`          '''
#randint:用来生成随机整数   random.randint(a,b) 返回a~b之间的随机整数,包含a,b 闭区间 a>b时报错 a=b时返回数本身

#2.13 调用内置模块
from random import randint as rint
for i in range(5):
    print(rint(5,10))

#2.14 调用自定义模块 -->规范命名模块名(即文件名)
NAME = "zza"#常量(不会发生变化),定义全大写
#__all__ 是一个模块级别的特殊变量,用于指定from 模块名 import * 时会导入哪些功能
#__name__ : Python中的内置变量,表示当前模块的名字(直接运行当前模块,__name__的值为"__main__";当该模块被导入时,__name__的值就是模块名称


from module01 import my_fun
#导入路径不在搜索范围里 my_fun.py在module01下 不和4.函数基础同级 它只会在Chapter1找 不会自动查找module01的子文件
my_fun.log_666888()# Ctrl+Y 快速删行

#2.15 Python Package 软件包
#定义:package本质就是一个文件夹,该文件夹中可以包含若干.py文件,文件夹下必须包含一个__init__.py
#作用:模块文件较多时,用来管理多个模块(package的本质也是一个模块)
'''' 前三个导入模块,后两个导入模块中的功能
  | 导入形式                     | 代码样例                              | 调用方式(规则)          | 调用方式(示例)                   |
 |------------------------------|---------------------------------------|-------------------------|-----------------------------|
 | import 包名.模块名            | import utils.my_fun                   | 包名.模块名.功能名      | utils.my_fun.log_separator1()   |
 | from 包名 import 模块名       | from utils import my_fun              | 模块名.功能名           | my_fun.log_separator1()        |
 | from 包名 import *            | from utils import *                   | 模块名.功能名           | my_fun.log_separator1()       |
 | from 包名.模块名 import 功能名 | from utils.my_fun import log_separator1 | 功能名                 | log_separator1()             |
 | from 包名.模块名 import *     | from utils.my_fun import *            | 功能名                  | log_separator1()              |
 '''

#2.16 案例:
#2.161 导入模块
import utils.my_separator

utils.my_separator.log_separator1()
utils.my_separator.log_separator2()

from utils import my_separator
my_separator.log_separator1()
my_separator.log_separator3()

#注意:如果要通过from utils import*导入package下所有模块,需要在__init__.py 文件中添加__all__ = []标明*到底包括哪些模块
from utils import *
my_separator.log_separator2()
print(constant.NAME)

#2.162 导入功能
#相对路径:从当前文件所在目录开始查找
from utils.my_separator import log_separator3 #utils.my_separator 是路径表达

#绝对路径:,从项目的根目录下开始查找
#from PythonProject.utils.my_separator import

log_separator3()