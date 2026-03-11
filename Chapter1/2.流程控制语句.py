#app登录 如果账号密码正确,则登陆成功,进入首页;否则,登陆失败,提示错误信息--->流程控制语句
'''条件判断 if 满足指定条件,执行对应程序--->判断语句的结果必须是布尔类型(True or False)'''
#归属于if代码块的语句,需要在前方缩进4个空格(按Tab键Pycharm会自动转为空格)

#if条件判断:如果分数超过680,我就去读清华
score = 700
if score > 680:#判断条件后要加:
    print('欢迎来到清华')
    print('开启清华园生活')#缩进不能多也不能少
print('------')#未缩进的语句不受if模块控制

#if案例:如果账号密码正确,则登陆成功,进入首页;否则,登陆失败,提示错误信息(正确账号密码 zza 0701)
ok_account = 'zza'
ok_password = '0701'
#1.接受用户输入的账号和密码
# account = input('请输入您的账号')
# password = input('请输入您的密码')
#2.判断账号和密码是否全部正确,如果都正确,则登陆成功,进入首页
# if account == ok_account and password == ok_password:
#       print('登录成功')
#       print('进入首页~')
#3.判断账号和密码是否有误,若任何一个有误,登陆失败,提示错误信息
 # if account != ok_account or password != ok_password:
 #     print('Log in unsuccessful')
 #     print('账号或密码错误')

#if进阶 if..else
correct_account = 'zza'
correct_password = '0701'
# account = input('请输入您的账号')
# password = input('请输入您的密码')
# if account == correct_account and password == correct_password:
#     print('登录成功')
#     print('进入首页~')
# else:
#     print('Log in unsuccessful')
#     print('账号或密码错误')

#案例 根据输入的年份,判断是闰年还是平年 (非整百年份且能被4整除的是闰年;整百年份必须能被400整除才是闰年)
# year = int(input('请输入需要判定的年份:'))#int把字符串转成整数 只有整数才能做 % 取余运算
# #如果是 非整百年份,能被4整除就是闰年;整百年份必须被400整除,才是闰年
# if (year %  100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f'{year}是闰年')
# else:
#     print(f'{year}是平年')

#练习1:根据用户输入数字,判断是奇数还是偶数
# num = int (input('请输入一个整数:'))
# if num %2 == 0:
#     print('此为偶数')
# else:
#     print('此为奇数')

#练习2:根据用户输入年龄,判断用户是否成年(>=18)
# age = int(input('请输入您的年龄:'))
# if age < 18:
#     print('您还未成年')
# else:
#     print('您已经成年')

#案例:根据用户输入的数字,判断这个数是正数还是负数,或者是0
#if...elif...else   if 判断条件1 条件成立时 执行操作1 elif 判断条件2 条件2成立时 执行操作2 else 条件1,2均不成立,执行操作3
#按顺序判断,满足条件1,不会进入后续判断,第1个条件不成立,才会判断第2个条件,1,2都不成立,才会进入else
# num = int(input('请输入数字:'))
# if num > 0:
#     print(f'{num}是 正数')
# elif num < 0:
#     print(f'{num}是 负数')
# else:
#     print(f'{num}为零')

#练习1:根据输入的用户名和密码进行系统登录
# username = input('请输入用户名:')
# password = input('请输入密码:')
# if username == "admin" and password == "<666888>":
#     print('登录成功')
# elif username == "root" and password == "555777":  #实际需要时elif可以出现多次
#     print('登录成功')
# elif username == "zhangsan" and password == "123456":
#     print('Log in successfully')
# else:
#     print('登录失败,用户名或密码错误')

# 练习2:根据输入的成绩,判断成绩等级 大于等于85分为良好,60-85分为及格,否则不及格
# grade = int(input('请输入成绩'))
# if grade >= 85:
#     print('良好')
# elif 60 < grade < 85:
#     print('及格')
# else:
#     print('不及格')

#练习3:根据输入的三边边长(正整数),判定三角形类型(等边,等腰,普通,无法构成三角形) 条件1:两边之和大于第三边
#1.接收输入的三角形三边长
"""
a = int(input('请输入第一个边的边长'))
b = int(input('请输入第二个边的边长'))
c = int(input('请输入第三个边的边长'))
#2.判断三角形类型--pass-空语句-语法占位 if的嵌套 
if a+b>c and a+c>b and b+c>a:
    if a ==b and b==c:
        print(f"{a} {b} {c}这三个边长构成等边三角形")
    elif a==b or b==c or c==a:
        print(f"{a} {b} {c}这三个边长构成等腰三角形")
    else:
        print(f"{a} {b} {c}这三个边长构成普通三角形")
else:
    print(f"{a} {b} {c}这三个边长不能构成三角形!")
"""
#三引号无论单双 可用于多行注释 本质是把引号里的内容框成字符串 但是必须 单独 放一段!! 前后不能有代码 行尾只能用#注释

#结构模式匹配 用一个清晰的模板去精准匹配数据的结构和内容,匹配成功则执行相应操作 match...case语句
# day = input('请输入星期几(1-7)')
# match day:
#     case '1':
#         print('Monday:Work&Meeting Day')
#     case '2':
#         print('Tuesday:Study&Training Day')
#     case '3':
#         print('Wednesday:Developing&Projects Day')
#     case '4':
#         print('Thursday:Checking&Coding Day')
#     case '5':
#         print('Friday:Summary&Planning Day')
#     case '6'|'7':# 其中的 | 表示 或 的关系,匹配多个模式中的任意一个
#         print('Weekend:Rest&Relax Day')
#     case _:# _ 匹配其他所有情况 相当于else
#         print('没有星期八')

#案例:实现一个可使用基本四则运算的计算器,用户输入需要运算的两个数和运算符后即可开始计算
# num1 = float(input('请输入第一个数:'))
# num2 = float(input('请输入第二个数:'))
# operator = input('请输入运算符(+/-*)')
# match operator:
#     case '+':
#         print(f'{num1}+{num2}={num1+num2}')
#     case '-':
#         print(f'{num1}-{num2}={num1-num2}')
#     case '*':
#         print(f'{num1}*{num2}={num1*num2}')
#     case '/' if num2 !=0 :#if条件成立,才匹配这个case  可嵌套
#         print(f'{num1}/{num2}={num1/num2}')
#     case _:
#         print('输入有误')
#match..case 不能替代if条件判断 match:基于某个变量多个 固定值 进行分支判断 if:条件判断涉及复杂的逻辑判断,范围比较及组合条件

#案例 做一个游戏 GPT
# def get_action(cmd):
#     """
#     这个函数的作用：
#     1) 接收玩家输入的指令 cmd（字符串）
#     2) 返回一个“动作字符串”（比如：'角色向上移动'）
#     3) 如果返回 None，表示要退出游戏
#     注意：这里用 return 是为了“把结果交给外面使用”   如果只用 print，那么外面很难判断“要不要退出”
#     """
# # 1) 标准化输入（非常常见）
# # strip()：去掉输入前后的空格和回车两边的空白
# # lower()：把大写变小写，让 W 和 w 都一样处理
#     c = cmd.strip().lower()#cmd只是变量名
# # 2)  if / elif 判断玩家输入哪一类指令
# # in (...) 表示：只要 c 等于括号里的任意一个，就算匹配成功
#     if c == "w" or c == "上":
#         # return：把结果“返回给调用者”
#         # 外面拿到这个字符串后再 print
#         return "角色向上移动"
#     elif c == "s" or c == "下":
#         return "角色向下移动"
#     elif c == "a" or c == "左":
#         return "角色向左移动"
#     elif c == "d" or c == "右":
#         return "角色向右移动"
# # 说明：input() 必须按回车才会提交
# # 如果你只按回车（什么都不输入），cmd 会是 ""（空字符串）
# # 我们把它当成“跳跃”
#     elif c == "" or c == "跳":
#         return "角色跳跃"
#     elif c == "j" or c == "攻击":
#         return "角色发动攻击"
# # 退出指令：esc 或 退出
#     elif c == "esc" or c == "退出":
#         # 返回 None 代表：告诉外面“该退出了”
#         return None
#     else:
#         # 输入不属于任何已知指令
#         return "无效指令，请重新输入（w/s/a/d/回车/j/esc）"
# cmd = input("请输入指令：")  # 让用户输入
# result = get_action(cmd)  # 调用函数
# if result is None:
#     print("角色退出游戏")
# else:
#     print(result)

#循环:重复执行某项操作---while 和 for 语句
#while语法结构:  while 条件表达式(bool值 True或False) 循环体语句1  循环体语句2...

#案例 打印五遍'Gym Rat'
i=0
while i<5:#循环条件
    print('Gym Rat')#条件成立时,执行的循环体逻辑
    i=i+1 #i+=1
else:
    print('循环正常结束,执行完毕')#条件不成立结束循环
#注意事项:条件表达式结果为布尔类型;通过空格缩进表述层级关系;规划好循环中止的条件,否则将无限循环(死循环)

#练习1:计算1-100之间所有的偶数累加之和
# sum = 0 #记录累加之和
# i = 1 #循环开始的数字
# while i<=100:
#     if i % 2 == 0: #偶数
#      sum += i
#     i += 1#注意缩进(层级关系)
# print(f'1-100之间所有偶数累加之和:{sum}')

#GPT练习
i=0
while i<3:
    print('666')
    i+=1

#for循环 是一种轮询遍历机制,对一批内容进行逐个处理
#for循环结构 for元素 in待处理数据集:    循环体代码(对元素进行处理)  else:循环结束时,执行的代码

#案例:定义要遍历的字符串
# msg = input('请输入需要遍历的字符串')
# for s in msg:#s 表示遍历出的元素(可以换成其他任意变量,只是大多用s代表string); msg 表示需要遍历的数据
#     print(f'元素:{s}')
# else:
#     print('遍历结束')

#for循环与while循环的场景 while循环用于在某个条件满足时一直循环,次数通常未知,只知道循环开始/结束的条件(关注循环的条件);
#for循环用于对一个已知的数据集进行遍历或已知次数循环(关注遍历的每一个元素)

#range语句:生成指定规则的数字序列 用法1:range(end)->获取一个从0开始,到end结束的数字序列(不含end);range(5)->0.1,2,3,4
#用法2:range(start,end)->获取一个从start开始,到end结束的数字序列(不含end);range(2,8)->2,3,4,5,6,7
#用法3:range(start,end,step)->获取一个从start开始end结束,以step为步长的数字序列,(不含end).range(0,10,2)->0,2,4,6,8

#练习1:计算1-500之间所有奇数之和-->如何获取1-100之间的所有奇数集?
total = 0#记录累加之和
for i in range(1,101):
    if i % 2 == 1:   #简化for i in range(1,101,2)
     total += i#if在for逻辑下 按tab缩进 累加在if逻辑下 需要再空格
print('1-100之间的奇数累加之和:',total)

#练习2:计算100-500之间所有3的倍数之和
total = 0#记录累加之和
for i in range(100,501):
    if i % 3 == 0:
     total += i
print('100-500之间所有3的倍数之和:',total)

#嵌套循环 钟表循环 for里有for 外层循环1次 内层循环n次
#案例1:根据输入的长方形的长m,宽n,打印一个长方形
#1.接受键盘录入m,n
# m = int(input('请输入长方形的长度'))
# n = int(input('请输入长方形的宽度'))
# #2.打印长方形
# for j in range(n):
#     print('*',end='')#end表示每次输出以什么结束,默认/n,表示换行
#     for i in range(m):
#         print('*',end='')
#     print()

#案例2:打印99乘法表  m*n= 外层循环控制行(n,乘数).内层循环控制列(m,被乘数)
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {j * i}',end='\t')#\t 制表符
    print()

#练习1:根据输入的直角边的边长,打印等腰直角三角形
# n = int(input("请输入直角边边长").strip())#strip去掉字符串首尾空格
# for i in range(1, n + 1):
#     print('*' * i)

#练习2:根据输入的用户名密码执行登陆操作,具体要求如下
# 正确的用户名和密码为admin/666,zza/0701,zhangsan/12345,重复输入并登录操作直到成功,输入的不能为空
#登陆成功输出"登陆成功,进入首页";登陆失败输出"用户名或密码错误,请重新输入"
#关键字 break 只能出现在循环中,表示结束,break跳出循环时,while后面的else中的代码将不会执行
#      continue 只能出现在循环中,中断本次循环,直接进入下一次循环

# while True:
#     username = input('请输入用户名').lower()#1.receive correct username and password
#     # .lower()不区分大小写
#     password = input('请输入密码')
#     if username == '' or password == '':#Check Not allow blank username or password
#         print('输入的用户名和密码不能为空!')
#         continue#结束当前循环,直接进入下一轮
#     if username == 'admin' and password == '666':
#         print('登录成功,进入首页')
#         break#跳出循环
#     elif username == 'zza' and password == '0701':
#         print('登录成功,进入首页')
#         break#跳出循环
#     elif username == 'zhangsan' and password == '12345':
#         print('登陆成功,进入首页')
#         break#跳出循环
#     else:
#         print('用户名或密码错误,请重新输入')

#练习3:同样的账号密码,但是输入错误五次后就不允许继续操作--->计次变量,错误时每次减一
# times = 5  # 剩余次数
#
# while times > 0:
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     # users = {
#     #     'admin': '666888',
#     #     'zhangsan': '123456',
#     #     'zza': '0701'
#     # }    ---->dict 字典 用行批量存储账号 少写elif
#
#     if username == 'admin' and password == '666888':
#         print('登录成功')
#         break
#     elif username == 'zhangsan' and password == '123456':
#         print('登录成功')
#         break
#     elif username == 'zza' and password == '0701':
#         print('登录成功')
#         break
#     else:
#         times = times - 1
#         if times > 0:
#             print('用户名或密码错误，还剩', times, '次机会')
#         else:
#             print('错误次数已达上限，禁止再操作')

#练习4:猜数字,系统随机生成一个数字,用户根据提示猜数并输入,如果猜错,系统给出提示是猜大了或小了,然后继续输入,猜对自动退出

import random
random_number = random.randint(1,500)#生成随机数

while True:
    num =int(input('请输入一个数字'))
    if num > random_number:
        print('比实际的大')
    elif num < random_number:
        print('比实际的小')
    else:
        print('666猜对了')
        break#跳出循环

print('随机生成的数字是:',random_number)#猜数逻辑:中位数
