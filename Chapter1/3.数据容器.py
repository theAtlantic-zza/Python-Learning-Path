#变量可存储数据,但是一次只能存储一个数据
# 定义一种可以容纳多份数据的数据类型(容器).容纳的每份数据称之为一个元素,每个元素可以是任意类型的数据(str,bool)
from multiprocessing.managers import ListProxy

#1.列表list 一次性可存储多个元素
#1.1定义:列表名称 = [元素1,元素2,] 可存储不同类型,元素可重复,有顺序
#序列类型:容器中元素按特定顺序排列,可通过索引访问的容器类型称为序列

s = [15,144,711,15,'hello']#列表会自行定义一个下标(索引) 从前向后(正向索引),下标从0开始;从后向前(反向索引),下标从-1开始
print(type(s))

#1.11访问列表元素
print(s[0])#正向索引
print(s[-5])#反向索引

#1.12修改  重新赋值
s[3]='ABC'
print(s)#注:如果指定索引超出范围,会报错 list assignment index out of range

#1.13删除 关键字del
del s[4]
print(s)

#1.14遍历
for item in s:
    print(item)

#1.15切片:对操作的数据截取其中一部分 (列表,字符串,元组都支持切片操作)
#序列数据[开始索引:结束索引:步长] 1.不包含结束索引位置对应的元素(有头无尾) 2.step默认为1,start不指定默认为0,end不指定默认为-1
s = ['a','d','c','carry','mid','and','top']
print(s[0:5:2])#从头开始索引,或步长为1时,可省略 print(s[:5])表示从0号元素开始以1步长切片到第5号元素,包含0,1,2,3,4共五个元素
print(s[:5])

#1.2常见方法
#1.21 append()在列表的尾部追加元素  s.append(10086)
#     insert()在指定索引前,插入该元素 s.insert(0,92)
#     remove()移除列表中第一个匹配到的值 s.remove(75) 如果有两个,删除靠start的那一个
#     pop()删除列表中指定索引位置的元素 s.pop(2)/s.pop() 如果未指定索引,默认删最后一个
#     sort()对列表进行排序 s.sort() 列表元素的数据类型一致,才可以进行排序
#     reverse()反转列表元素 s.reverse()

s = [56,90,88,65,90,100,209,72,145]
s.append(188)
print(s)
s.insert(2,188)
print(s)
s.remove(90)
print(s)
e=s.pop(1)
print(e)
e=s.pop()
print(e)
s.sort()#默认从小到大
print(s)
s.reverse()
print(s)

#案例1:将用户输入的10个数字.存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值,最大值,和平均值
num_list = []
for i in range(12):
    num_list.append(i)#将输入的10个数字输入列表 num=int(input('请输入一个有效的数字'))
print('数字列表',num_list)
num_list.sort()
print('排序后的数字列表',num_list)#从小到大
print('最小值',num_list[0])#sum()求和
print('最大值',num_list[-1])
print('平均值',sum(num_list)/len(num_list))#len()获取元素的个数or列表的长度 length

#案例2:合并两个列表中的元素,并对合并的结果进行去重
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#合并两列表方法1
num_list1=[*num_list1,*num_list2]
#解包:将列表这一类容器解开成一个个独立的元素
#组包:将多个值合并到一个容器

#合并两列表方法2: for num in num_list2:
#     num_list1.append(num)   循环 如果元素很多则大量消耗性能

#合并两列表方法3:num_list = num_list1 + num_list2
print('合并后的原始列表',num_list1)
new_list = []
for num in num_list1:
    #in 判断new_list中是否存在num元素,如果不存在,再添加
    if num not in new_list:#判断元素是否存在于列表中,如果存在则返回True,不存在则返回False
        new_list.append(num)
print('去重后的列表',new_list)

#案例3 生成一个1-20的平方列表--->range(1,21) range包含开始不包含结束
#法1
num_list = []
for i in range(1,21):
    num_list.append(i**2)
print(num_list)
#法2:列表推导式--->就是按照一定的规则快速生成一个列表的方法-->语法格式 [要插入的值 for i in 列表 if 条件]
num_list3 = [i**2 for i in range(1,21)]

#练习1 将如下多个列表合并,并去重按升序输入到控制台
list1 = ['M','A','C','E','F','G','H','I','J','K','N','O']
list2 = ['X','Z','T','Y','D','E','F','G']
list3 = ['W','A','S','D']
list_merged=[*list1,*list2,*list3]
print('合并后的原始列表',list_merged)
list_clean=[]
for item in list_merged:
    if item not in list_clean:
        list_clean.append(item)
list_clean.sort()
print('去重排序后的列表',list_clean)

#练习2 将如下列表中能被3或5整除的数提出,并获取这些数字对应的平方,组成一个新列表
list8=[]
for i in range(1,31):
    if i% 3==0 or i % 5==0:
     list8.append(i**2)
print('能被3或5整除的数的平方集',list8)

#练习3 将如下列表中的正数提出,组成一个新的列表
list9=[11,2,31,4,-5,15,17,28,49,-11,-14,-16,16,10,54,36,87]
positives=[]
for num in list9:
    if num>0:
        positives.append(num)
print('正数集',positives)

#2.字符串str 可存储任意数量字符的容器
#2.1特点:不可变性(无法修改),有序性,可迭代性     每个字符都有其对应的下标(索引),通过元素对应的索引,就可获取到对应的元素
s='Hello-Python'
print(s[4])#正向索引
print(s[-8:])#反向索引

#2.11切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[6:12:])#[start,end,step]含头不含尾
#step-->positive:从前往后,negative:从后往前
print(s[::-1])#从后往前一个一个取,反转
print(s[-1:-7:-1])

#2.2常用方法
#2.21 find() 在字符串中查找子串，返回第一次出现的位置 如果找不到，返回 -1
print(s.find("Python"))  # 6
print(s.find("Java"))    # -1

#2.22 count() 统计子串在字符串中出现的次数
print(s.count("o"))      # 2
print(s.count("H"))      # 1

#2.23 upper() 将字符串中的所有字母转换为大写--->只是返回转换后的结果,并未修改字符串本身
print(s.upper())         # HELLO PYTHON

#2.24 lower() 将字符串中的所有字母转换为小写
print(s.lower())         # hello python

#2.25 split() 按指定分隔符拆分字符串，返回列表
print(s.split(" "))      # ['Hello', 'Python']

#2.26 strip() 去除字符串两端的空白字符（空格、换行等）
s2 = "  hello  "
print(s2.strip())        # 'hello'
# 也可以去除指定字符
s3 = "***hello***"
print(s3.strip("*"))     # 'hello'

#2.27 replace() 将字符串中的指定子串替换为新的子串
print(s.replace("Hello", "Hi"))  # Hi Python

#2.28 startswith/endswith() 判断字符串是否以指定子串开头/结尾，返回布尔值 True / False
print(s.startswith("H"))        # True
print(s.endswith("P"))        # False

print(s)#原始字符串并未改变,只是表现形式变化

#2.31案例1 邮箱格式验证:用户输入一个邮箱,验证其是否正确(包含一个@和至少一个.).如果输入正确,输出'邮箱格式正确';否则输出'邮箱格式错误'
mail="Please confirm your mail address: ziang.zhao@cariad-technology.cn"
if mail.count("@")==1 and mail.count(".")>=1:#if mail.count('@')==1 and '.' in mail:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

#2.32案例2:输入一个字符串,判断该字符串是否是回文(两边对称)
# s = input("请输入一个字符串：")#上海自来水来自海上
# reverse_s = s[::-1]
# if s == reverse_s:
#     print("这是一个回文字符串")
# else:
#     print("这不是一个回文字符串")

#2.33案例3:将用户输入的10个字符串反转并全部转为大写,然后记录在列表中,将列表中内容遍历输出
s = "abcdhhhh7788"
result = []
s = s[::-1]
s = s.upper()
for ch in s:
    result.append(ch)
for item in result:
    print(item)

#3.元组tuple --->与列表最大不同--不能修改,只能查询  //  不可变序列
#3.1特点:可重复,有序, 不可修改(支持索引,访问,切片),可存储不同类型元素
#3.12定义:元组名 = (元素1,元素2,...)

#3.2常见方法
#3.21 count() 统计某元素在元组中出现的次数
#3.22 index() 查找某个元素在元组中的索引位置(第一次出现的位置)

t1 = (80,95,78,50,76,80,85,20)
print(t1)
print(type(t1))
print(t1[0],t1[-1])#索引访问
print(t1[0:5:1])#切片
print(t1.count(80))#count() 统计元素的个数
print(t1.index(80))#index() 获取第一个元素的索引
#注意点:如果定义单元素的元组,单个元素之后需要加上逗号>>>不加逗号系统会识别为字符串
t2=(100,)
print(t2)
print(type(t2))#如果不加, 此处会输出int

#3.3组包与解包 Packing:将多个值合并到一个容器(元组,列表)中;Unpacking:将容器(元组,列表)解开成独立的元素,分别赋值给多个变量
#3.31定义元组,组包
t1 = (5,7,9,1)#定义元组,组包
#3.32基础解包
a,b,c,d = t1
#3.33扩展解包(*收集剩余的所有元素,封装到列表list中)
x,*y,z=t1#x为5,y为[7,9],z为1
t2=(1,2,3,4)
o,*e=t2# *将剩下的值都装进e这个列表里
print(a,b,c,d)
print(x,y,z)
print(o,e)#如果此处e前有*,相当于把e列表中所有元素拆包,输出结果会变成1 2 3 4 print接收到4个独立参数,默认用空格把它们连起来打印

#3.3 Q&A
# t1 = (1, 2)
# a, b, c = t1 这里有3个变量，但元组只有2个值 ValueError: not enough values to unpack (expected 3, got 2)
t = (1, 2)
a, b, *c = t
print(a, b, c) # 输出：1 2 []

#3.3 review previous example
#现有两个变量a=10,b=20,现需要交换两变量的值,然后输出到控制台
a=10
b=20
# t=b,a 组包
# a,b=t 解包
a,b=b,a#合并
print(a,b)#交换赋值

#3.41 案例 根据学生成绩单,完成以下需求 1.计算学生总分,各科平均分 2.统计各科最高最低分,平均分 3.查找平均分大于90的优秀学生
students =(
    ('S001','乔峰  ',85,92,78),
    ('S002','慕容复',92,88,95),
    ('S003','黄药师',78,85,82),
    ('S004','欧阳锋',88,79,91),
    ('S005','洪七公',95,96,89),
    ('S006','周伯通',76,82,77),
    ('S007','柯镇恶',89,91,94),
    ('S008','fishman',75,69,82),
    ('S009','黄蓉',86,89,98),
)
#3.411.计算并输出学生总分和平均分
print('学号\t\t姓名\t\t 总分\t平均分')
#方式一
for s in students:
    total = s[2]+s[3]+s[4]
    avr = total/3
    print(f'{s[0]:<6}{s[1]:<10}{total:<6}{avr:<6.1f}')# :.1f --->保留1位小数  冒号也是组成部分!!!; <宽度 固定列宽
#方式二:元组解包
# for id,name,chinese,math,english in students:
#     total = chinese+math+english
#     avr = total/3
#     print(f"id\t{name}\t{chinese}\t{math}\t{english}\t{total}") 每个子元素赋给对应列表

#3.412.统计各科成绩最高,最低分和平均分
Chinese_scores = [s[2]for s in students]
math_scores = [s[3]for s in students]
English_scores = [s[4]for s in students]
print(f'语文最低分:{min(Chinese_scores)},最高分:{max(Chinese_scores)},平均分:{sum(Chinese_scores)/len(Chinese_scores):.1f}')
print(f'数学最低分:{min(math_scores)},最高分:{max(math_scores)},平均分:{sum(math_scores)/len(math_scores):.1f}')
print(f'英语最低分:{min(English_scores)},最高分:{max(English_scores)},平均分:{sum(English_scores)/len(English_scores):.1f}')

#3.413.查找成绩优秀(平均分大于90)的学生,并输出
for s in students:
    total = s[2]+s[3]+s[4]
    avr = total/3
    if avr>90:#优秀学生
        print(f'学号:{s[0]},姓名:{s[1]},平均分{avr:.1f}')#{} ()一一对应

#4.集合set
#4.11特点:无序的,不可重复的,可修改的
#4.12定义s1={'C','D','X'} 空集合s2=set()--->注意,{}表示空字典  且由于集合无序,故不支持索引
s1={5,3,2,0,9,12,43,64,22,5,0}
s2=set()#不加set是元组
s3={}#花括号是字典
print(s1)
print(type(s1))#自动去重
print(type(s2))
print(type(s3))

#4.2常见方法
s1 = {'a', 'b', 'c', 'd'}#定义两集合
s2 = {'c', 'd', 'e'}

print("初始集合：")
print("s1 =", s1)
print("s2 =", s2)
print("-" * 30)
#4.21. add() —— 向集合中添加元素
s1.add('x')
print("add('x') 后 s1 =", s1)

#4.22. remove() —— 删除指定元素（元素不存在会报错）
s1.remove('a')
print("remove('a') 后 s1 =", s1)

#4.23. pop() —— 随机删除一个元素并返回
e = s1.pop()
print("pop() 删除的元素 =", e)
print("pop() 后 s1 =", s1)

#4.24. clear() —— 清空集合
s3 = {'m', 'n', 'o'}
s3.clear()
print("clear() 后 s3 =", s3)
print("-" * 30)

#4.25. difference() —— 差集（s1 中有，s2 中没有）
print("s1 - s2 =", s1.difference(s2))

#4.26. union() —— 并集
print("s1 ∪ s2 =", s1.union(s2))

#4.27. intersection() —— 交集
print("s1 ∩ s2 =", s1.intersection(s2))

#Q&A:如何在集合中删除多个元素--->difference_update()
s = {1, 2, 3, 4, 5}
s.difference_update({2, 4})
print(s)#-->{1,3,5}

#4.31案例:根据提供的班级学生的选课情况,完成以下需求
football_set={'詹姆斯','科比','欧文','库里','保罗','布克','Biden','东七七','内马尔'} #选修足球学生名单
basketball_set={'内马尔','姆巴佩','梅西','詹姆斯','C罗','穆勒','Trump','哈兰德','保罗','罗纳尔多','科比'}
french_set={'姆巴佩','Linkln','Biden','Trump','布克','科比','东七七','詹姆斯'}
art_set={'C罗','Linkln','梅西','欧文','科比','穆勒','库里','布克','詹姆斯'}

#4.311 找出同时选修了 法语和艺术的学生-->求交集
#法1
fa_set=french_set.intersection(art_set)
print(f'同时选修了法语和艺术的学生:{fa_set}')
#法2:&-->交集
fa_set2=french_set & art_set
print(f'同修法语和艺术的学生:{fa_set2}')

#4.312同时修四门课的学生--->交集
all_set=football_set & basketball_set & french_set & art_set
print(f'同时修四门课的学生:{all_set}')

#4.313选了足球但没有选篮球的--->差集
#法1:
fbutb_set=football_set.difference(basketball_set)
print(f'选足球没选篮球:{fbutb_set}')
#法2:- 差集
fb_set=football_set- basketball_set
print(f'选足不选篮:{fb_set}')
#法3:集合推导式--->快速构建集合,语法{要往集合中添加的数据i for s in set1 if 条件}
fb_set2={s for s in football_set if s not in basketball_set} #第一个s: 要放进集合的新元素是s
print(f'没选篮球但选足球:{fb_set2}')

#4.314统计每一个学生选修的课程数量
all_set=football_set.union(basketball_set).union(french_set).union(art_set)#获取学生名单--->并集( | )
students_set=football_set|basketball_set|french_set|art_set
print(f'学生名单:{students_set}')
print(f'全部名单:{all_set}')#并集自动去重

#4.315获取每个学生选修的课程数量
all_list=[*football_set,*french_set,*art_set,*basketball_set]#列表 解包 里面存在重复性元素
for s in all_set:
    print(f'{s}选修了{all_list.count(s)}课程')

#5.字典dict
#5.11特点:键值对(key:value)存储,键key 不能重复,可修改
#5.12定义:存储的是键值对(key:value)类型的数据,可通过键key找到对应值value
#字典名称={key1:value,key2:value,key3:value} 空字典 dict1=  {} / dict()
#根据key获取value 值=字典名称[key] value可以是任意类型,而key是不可变类型str,int,float,tuple (不能为list,set,dict)

#5.13说明
dict1 = {'王林':568,'李木碗':608,'蓄力过':632,'翁护甲':680,'王林':588}
print(dict1)#'王林':588--->key不能重复 如果重复 后面的值会覆盖前面的值 key必须是不可变类型(str,int,float,tuple)
dict2 = {1.5 : 568,(1,2):476}
print(dict2)

print(dict2.keys())#查key值
print(dict1['蓄力过'])#根据key查value
dict1['李木碗']=618#字典可以修改
print(dict1)

#5.2常见方法
d = {"小智": 675, "李思": 608, "李理": 478, "小黑": 545, "温智": 429}

#5.21  添加/修改：dict[key] = value  （key 不存在：新增;存在:修改）
d["清哥"] = 688
print(d)  # {'小智': 675, ... , '清哥': 688}

#5.221  删除：pop(key)  删除指定 key，并返回对应 value（key 不存在会报错）
v = d.pop("温智")
print(v)  # 429
print(d)  # '温智' 不存在d中--------删除key后,相应value也不存在

#5.222  删除：pop(key, default)  key 不存在返回 default，不报错
x = d.pop("不存在", None)
print(x)  # None

#5.223  删除：del dict[key]  删除指定 key-value（key 不存在会报错）
del d["李理"]
print(d)

#5.231  查询：dict[key]  根据 key 获取 value（key 不存在会报 KeyError）
print(d["小黑"])  # 545

#5.232  查询：dict.get(key)  key 不存在返回 None（不报错）
print(d.get("不存在"))  # None

#5.233  查询：dict.get(key, default)  key 不存在返回 default
print(d.get("不存在", 0))  # 0

#5.241  keys()  获取所有 key（可遍历）
print(d.keys())  # dict_keys(['小智', '李思', '小黑', '清哥', ...])

#5.242  values() 获取所有 value（可遍历）
print(d.values())  # dict_values([658, 608, 545, 688, ...])

#5.243  items()  获取所有 (key, value)（可遍历）
print(d.items())  # dict_items([('小智', 658), ...])

#5.244  遍历 items（最常用）
for k, v in d.items():
    print(k, v)
print('0000')
for item in d.items():
    print(f'{item[0]}:{item[1]}')

# d[key]：key 不存在会报错   d.get(key)：key 不存在不报错
# pop(key) / del d[key]：key 不存在会报错（pop(key, default) 例外）

#5.3案例 开发一个购物车管理系统,实现商品信息的添加,修改,删除,查询功能.系统使用字典结构存储商品数据,通过控制台与用户交互
# print('欢迎使用购物车管理系统')#alt + shift 一次性选中多行
# menu= """
# ######购物车系统######
# #     1.添加购物车   #
# #     2.修改购物车   #
# #     3.删除购物车   #
# #     4.查询购物车   #
# #     5.退出购物车   #
# ####################
# """
# shopping_cart={}
#
# while True:
#     print(menu)
#
#     choice=input("请选择要执行的操作(1-5):")
#     print("DEBUG choice =", repr(choice))
# # shopping_cart = {'Magic9':{'price':6999,'num':2},'手机':{...}}
#     match choice:
#
#         case'1':#添加购物车:用户根据提示录入商品名称,以及该商品的价格,数量,保存该商品到购物车
#             goods_name = input('请输入商品名称')
#             goods_price = float(input('请输入商品价格'))
#             goods_quantity = input('请输入商品数量')
#             if goods_name in shopping_cart:
#                 print('该商品已存在,请重新选择')#如果商品存在,则不执行添加,提示信息
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "quantity": goods_quantity}
#                 print('已添加商品')
#
#         case'2':#修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格,数量.输入完成后修改商品信息
#             goods_name = input('请输入要修改的商品名称')
#             if goods_name not in shopping_cart:
#                 print('该商品不存在,请重新选择')#如果商品不存在,则让用户重新选择
#                 continue
#             goods_price = input('请输入商品的最新价格')
#             goods_quantity = input('请输入商品的最新数量')
#             shopping_cart[goods_name] = {"price": goods_price, "quantity": goods_quantity}
#             print('商品修改完毕')
#
#         case'3':#删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品
#             goods_name = input('请输入要删除的商品名称')
#             if goods_name not in shopping_cart:
#                 print('该商品不存在,请重新选择')
#             else:
#                 del shopping_cart[goods_name]
#                 print('商品删除完毕')
#
#         case'4':#查询购物车:将购物车中的商品信息展示出来,格式为'商品名称:xxx,商品价格:xxx,商品数量:xxx'
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f'商品名称:{goods_name},商品价格:{goods_info["price"]},商品数量:{goods_info["quantity"]}')
#         case'5':#退出购物车
#             print('Bye')
#             break
#         case _ :#匹配其他所有情况
#             print('别乱输')
#             input('按回车继续')

#5.4练习 开发一个教务管理系统,在该系统中可以维护和管理学生的成绩信息(增删改查,遍历信息,统计班级成绩,各科最高分,最低分,平均分,平均分,学员姓名)
students = {}  # {姓名: {"chinese":分数, "math":分数, "english":分数}}

menu = """
================ 教务管理系统 ================
1. 添加学生信息
2. 修改学生信息
3. 删除学生信息
4. 查询学生信息
5. 列出所有学生
6. 统计班级成绩
7. 退出系统
============================================
"""

while True:
    print(menu)
    choice = input("请选择操作(1-7): ").strip()

    match choice:
        case "1":  # 添加
            name = input("请输入学生姓名: ").strip()
            if not name:
                print("姓名不能为空")
                input("按回车继续...")
                continue
            if name in students:
                print("该学生已存在，请使用修改功能")
                input("按回车继续...")
                continue

            # 语文
            while True:
                try:
                    chinese = float(input("请输入语文成绩(0-100): ").strip())
                    if 0 <= chinese <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            # 数学
            while True:
                try:
                    math = float(input("请输入数学成绩(0-100): ").strip())
                    if 0 <= math <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            # 英语
            while True:
                try:
                    english = float(input("请输入英语成绩(0-100): ").strip())
                    if 0 <= english <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            students[name] = {"chinese": chinese, "math": math, "english": english}
            print("添加成功")
            input("按回车继续...")

        case "2":  # 修改
            name = input("请输入要修改的学生姓名: ").strip()
            if name not in students:
                print("该学生不存在")
                input("按回车继续...")
                continue

            while True:
                try:
                    chinese = float(input("请输入语文最新成绩(0-100): ").strip())
                    if 0 <= chinese <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            while True:
                try:
                    math = float(input("请输入数学最新成绩(0-100): ").strip())
                    if 0 <= math <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            while True:
                try:
                    english = float(input("请输入英语最新成绩(0-100): ").strip())
                    if 0 <= english <= 100:
                        break
                    print("分数必须在0~100之间")
                except ValueError:
                    print("请输入合法数字")

            students[name] = {"chinese": chinese, "math": math, "english": english}
            print("修改成功")
            input("按回车继续...")

        case "3":  # 删除
            name = input("请输入要删除的学生姓名: ").strip()
            if name not in students:
                print("该学生不存在")
            else:
                del students[name]
                print("删除成功")
            input("按回车继续...")

        case "4":  # 查询
            name = input("请输入要查询的学生姓名: ").strip()
            if name not in students:
                print("该学生不存在")
            else:
                info = students[name]
                total = info["chinese"] + info["math"] + info["english"]
                avg = total / 3
                print(f"姓名:{name}  语文:{info['chinese']:.1f}  数学:{info['math']:.1f}  英语:{info['english']:.1f}  总分:{total:.1f}  平均:{avg:.1f}")
            input("按回车继续...")

        case "5":  # 列表
            if not students:
                print("暂无学生数据")
            else:
                print("姓名\t语文\t数学\t英语\t总分\t平均")
                for name, info in students.items():
                    total = info["chinese"] + info["math"] + info["english"]
                    avg = total / 3
                    print(f"{name}\t{info['chinese']:.1f}\t{info['math']:.1f}\t{info['english']:.1f}\t{total:.1f}\t{avg:.1f}")
            input("按回车继续...")

        case "6":  # 统计班级成绩
            if not students:
                print("暂无学生数据，无法统计")
                input("按回车继续...")
                continue

            subjects = ["chinese", "math", "english"]
            subject_cn = {"chinese": "语文", "math": "数学", "english": "英语"}

            for sub in subjects:
                scores = []
                for name, info in students.items():
                    scores.append((name, info[sub]))

                values = []
                for _, v in scores:
                    values.append(v)

                max_val = max(values)
                min_val = min(values)
                avg_val = sum(values) / len(values)

                max_names = []
                min_names = []
                for name, v in scores:
                    if v == max_val:
                        max_names.append(name)
                    if v == min_val:
                        min_names.append(name)

                print(f"\n")
                print(f"最高分: {max_val:.1f}  学生: {', '.join(max_names)}")
                print(f"最低分: {min_val:.1f}  学生: {', '.join(min_names)}")
                print(f"平均分: {avg_val:.1f}")

            # 可选：统计总分最高/最低
            totals = []
            total_values = []
            for name, info in students.items():
                t = info["chinese"] + info["math"] + info["english"]
                totals.append((name, t))
                total_values.append(t)

            max_total = max(total_values)
            min_total = min(total_values)
            max_total_names = []
            min_total_names = []
            for name, t in totals:
                if t == max_total:
                    max_total_names.append(name)
                if t == min_total:
                    min_total_names.append(name)

            print("\n【总分】")
            print(f"最高总分: {max_total:.1f}  学生: {', '.join(max_total_names)}")
            print(f"最低总分: {min_total:.1f}  学生: {', '.join(min_total_names)}")

            input("\n按回车继续...")

        case "7":  # 退出
            print("Bye")
            break

        case _:  # 其他
            print("输入有误，请重新输入")
            input("按回车继续...")
