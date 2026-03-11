#此需求仅供开发人员
print('hell no');print('donot follow')
# print just like a simple directory .idea保存项目配置信 .vemv虚拟环境，保存项目的环境信息
print('##白日依山尽,黄河入海流###');
print('##欲穷千里目,更上一层楼###')
print('the different input method but the same result')

# bool类型 基于基本算数逻辑的True or False
print(10<0) #布尔类型
print(3.14) #小数类型float
#字面量的写法
print(True)#bool类型
print(False)
print(None)#空值 None type
print(True +1)#2
print(False -1)#-1

#变量:程序中用来存储单个数据的容器,通常把经常发生变化的数据存在其中 python是动态语言 一个变量可存储多类型数据,但实地开发中只用它一次存储一种数据
num = 114.1
print(num)
num = num +1
print(num)

#案例
base = 20.7#basic views
incr = 50
print('the first month in the future',base + incr)#ctrl + D 快速复制第一行
print('the first month in the future',base + incr + incr)#变量定义后必须赋值才能使用
#标识符 是代码中为变量,函数,类等元素起的名字
#命名规则 只能包含字母,数字,下划线_,不能以数字开头,不能使用关键字 True,False,None,and,or,if,else,while,且严格区分大小写
#命名规范 1.见名知意 2.多个部分使用下划线连接(蛇形命名法) 3.英文字母全小写

#案例 a=10,b=20,把两个变量值交换后输出
a=10
b=20
c = a #引入新变量(空杯)
a = b
b = c
print(a,b)

#练习 三个变量a=100,b=200,c=300,现需要将a,b,c的值分别赋给c,a,b
a=100
b=200
c=300
d=c
c=a
a=b
b=d
print(a,b,c) #success 逻辑问题

#通过type()语句得到数据的类型 本质是函数
print(type('hello'))#str
print(type(3.14))#float
num=110
print(type(num))#因为已经给num赋值,实际显示的是变量对应的值的数据类型
print(type(False))#bool

#isinstance(数据,类型)检查数据是否属于指定的类型,返回的是一个bool值
print(isinstance('simultaneously',str))#True
print(isinstance(num,str))#False

#字符串 三种定义 单,双,三引号 三引号用于定义多行字符串
s1 = "LOL"#双
s2 = 'Jinchanchan'#单
s3 = """Hello:
    嘻嘻哈哈
    七七八八"""#三,多行字符串,Tab首行缩进
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))

s4 = 'It\'s very ridiculous' #\' \" \n \t  转义字符 或者用"规避掉'与缩写'的配对
print(s4)
s5 = '"Merry Christmas"' #用'规避两个"
print(s5)
s6 = '学\npython'
print(s6)
s7 = '\t我试一下 \n\t缩进'  #\n 换行 \t 按了Tab缩进 制表符
print(s7)
lyrics = "谁又骑着那鹿车飞过" '忘记投下个礼物给我'
print(lyrics)
lyrics = "谁又骑着那鹿车飞过"+'忘记投下个礼物给我' # + 用来拼接两个字符串 但无法把非字符串和字符串进行拼接
print(lyrics)
msg1="人生苦短"
msg2="我用python"
print("龟叔说: "+msg1 + ","+msg2)

#案例
name = "zza"
age = 20
pro = "Engine and Power Engineering"
hobby = "sleep"
print('大家好,我是'+name+',今年'+str(age)+'岁,学习'+pro +',爱好'+ hobby)#''+  ''+ ''+ 多字段连接

#字符串格式化 方式1:通过 % 占位符,%_表示将变量_转为字符串放在%处
s = "back"
print("I'm %s" % s)
name = ("zza")
age = 20
pro = "Engine and Power Engineering"
hobby = "sleep"
print('大家好,我是%s,今年%s岁,学习%s,爱好%s'%(name,age,pro,hobby))#%将数据自动转为字符串

#字符串格式化 方式2:f"....{变量,表达式}...."
name = ("zza")
age = 20
pro = "Engine and Power Engineering"
hobby = "sleep"
print(f'大家好,我是{name},今年{age}岁,学习{pro},爱好{hobby}')#主流应用方式
#输入与输出 input语句(函数)的功能就是获取键盘输入的数据,具体用法为s = input(提示信息) ;语句(函数)的功能就是将数据输出到控制台,具体用法为print(数据)
# name1 = input("请输入您的姓名:")#需要在控制台界面输入内容 再执行
# print(f'欢迎您,{name1}')

#案例 模拟ATM取款
# total = 10000 #总金额
# #1.输入密码
# password = input("请输入您的银行卡密码")
# print(f'密码正确,{password}')
# # #2.输入取款金额
# num = input("请输入您的取款金额")
# #3.计算余额并输出---->num转为int类型---->int(...)
# print(f"取款后银行卡余额为:{total - int(num)}") # ------>其他类型转为int类型:int(...);转为str类型:str(...),float类型,bool类型
print('input语句影响程序继续,故标灰')

#运算符 四类:算术,赋值,比较.逻辑
#算术运算符: + ;- ; *乘 ;/除, 结果为小数; //整除,结果为整数; %求模,取余数; **幂函数
print('10 // 4 = ',10 // 4 )
print('10 % 3=',10 % 3)
print('2 ** 8',2 ** 8)

#算术运算符的优先级----> ** >* / // % > + -
print('0.1 + 10 / 4 ** 2 =',0.1 + 10 / 4 ** 2 )#加()更改运算顺序
#案例 输入两数x,y,输出x+y,x-y,xy,x/y,x//y,x%y.x**y
# x = float(input("请输入x的值"))#转为字符串才能运算,用float避免int只能识别整数,忽略了小数情况
# y = float(input ("请输入y的值"))
# print('x+y = ' ,x + y)
# print('x-y = ' ,x - y)
#x-y =  0.09999999999999998精度损失  当x=0.5,y=0,4时 由于计算机基于二进制进行数据存储与处理,二进制无法准确表示所有小数,涉及到浮点数运算时可能存在精度损失
# print('x*y = ' ,x * y)
# print('x/y = ' ,x / y)
# print('x//y = ' ,x // y)
# print('x%y = ' ,x % y)
# print('x**y = ' ,x ** y)

#练习1 计算输入三个整数的平均数
# a=int(input("请输入第一个整数:"))
# b=int(input("请输入第二个整数:"))
# c=int(input("请输入第三个整数:"))
# average=(a+b+c)/3
# print('三个整数的平均数是:',average)

#练习2 要求输入梯形的上底,下底,高,然后计算梯型的面积
# top=float(input('请输入梯形的上底:'))
# bottom=float(input('请输入梯形的下底:'))
# height=float(input('请输入梯形的高:'))
# area=(top*bottom)*height/2
# print('梯形的面积是:',area)

#练习3 输入圆的半径,计算周长及面积

import math #导入数学模块，用于用Pi计算圆的周长和面积 math是python自带的数据库

# r = float(input("请输入圆的半径："))
# circumference = 2 * math.pi * r
# area = math.pi * r ** 2
# print("圆的周长是：", circumference)
# print("圆的面积是：", area)

print(abs(-5))#abs 求绝对值 支持int,float 不用import
#案例 求两数之差的绝对值
# a = float(input("请输入第一个数："))
# b = float(input("请输入第二个数："))
# result = abs(a - b)
# print("差的绝对值是：", result)

#练习4 BMI指数的计算(带单位m,kg)
# weight = float(input("请输入体重（kg）："))
# height = float(input("请输入身高（m）："))
# bmi = weight / (height ** 2)
# print("你的 BMI 指数是：", bmi)

#赋值运算符 1."=" 把=右边的结果赋值给左边的变量 2."+="加法赋值运算符 num+=2等效于num=num+2 3.'-=';'*=";'/=';'%=';'//=';'**='
#两符号间不能加任何字符或空格 需看成一个整体
num=85
num += 10
print("num += 10 后,num= ",num)
num -= 10
print("num -= 10 后,num= ",num)
num *=10
print("num *= 10 后,num= ",num)
num /= 10
print("num /= 10 后,num= ",num)#除法运算的结果是小数float
num //= 10
print("num //= 10 后,num= ",num)
num %= 3
print("num %= 10 后,num= ",num)
num **= 3
print("num **= 10 后,num= ",num)

#比较运算符 也叫关系运算符,用于比较两个值之间的关系.会计算运算符两边的表达式,然后返回一个 布尔值 作为结果(True-表示成立,False-表示不成立)
#a == b 判断a是否等于b; a != b 判断a是否不等于b; a > b (a < b) 判断a是否大(小)于b;a >= b (a <= b)判断a是否大于等于(小于等于)b
print("100<=100 吗 :",100 <= 100)
print("100<100 吗 :",100 < 100)
#案例 1.数学计算中,判断一个数是否为偶数,使用哪个关系运算符
num = 5
print(num % 2 == 0)#5不为偶数

#逻辑运算符 是用于连接多个条件(布尔)表达式(其值为True 或 False),并返回一个最终 布尔结果 的运算符
#1.and 与 同时成立才符合条件(左右都为True,结果才为True);
#2. or 或 只要有一个符合要求的即可(只要左右两边有一个为True,结果就为True;
#3. not 非 取反操作,True变为False,False变为True

#案例1:判断输入的数是否在10-20之间 数轴
# num = int(input('请输入一个整数:'))
# print(f'{num}在10-20之间:',num >= 10 and num <= 20)#and连接的条件是并列关系,两条件同时成立(True),结果才是True

#案例2:判断输入的整数是否不在10-20之间
n = int(input('请输入一个整数:'))
print(f'{n}不在10-20之间:',n < 10 or n > 20)#or 连接的条件是或者的关系,只要其中一个成立,结果就是True,全部不成立结果才是False
#登录app 用户名匹配密码才正确 and ;扫码,短信,密码任意一种正确都成立,or