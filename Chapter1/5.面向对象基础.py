"""  引入
面向过程Programming:
                把一个需求分解成一系列要执行的步骤,然后按步骤依次执行这些任务(Procedure,step)
                适用于简单,线性的任务
面向对象Programming:
                    对象:可理解为人/物在程序中的数字化身(万物皆对象)
                        它把一个人/物的特征(属性)和功能(方法)打包到一起,是面向对象编程的基本单元(关注谁来帮我做这件事)
                    类:描述的是一组具有相同属性(特征)和方法(功能/行为)的模板
                            对象是类的实例,是基于类这个模板创建出来的(实例对象),创建的过程称为对象的实例化,一个类可以创建无数个对象

"""

#1. 类与对象
#1.1 类的定义:
'''1.11 动态为对象添加属性
       class 类名:      类名命名 遵循大驼峰法 每个单词首字母均大写,单词之间没有分隔符 e.g. UserInfo
        pass
        创建对象 对象名 = 类名()
                对象名.属性名1 = 属性值1
print(对象名.__dict__)      __dict__是Python中用户自定义类实例的一个特殊属性,用于以字典形式存储对象的属性

class Car:
    pass
c1 = Car()

c1.color = "black"
c1.brand = "Audi"
c1.model = "A8L Horch"
c1.price = "1000000"

print(c1.__dict__)  '''

#1.12 定义类时指定实例属性
#class 类名:
#   def __init__(self, 参数列表):
#       self.属性名 == 参数值
#       对象名 = 类名(参数列表)

class Car:
    def __init__(self,c_color,c_model,c_price,c_brand):
        # self:方法的第一个参数,表示当前创建的实例对象
        self.color = c_color
        self.model = c_model
        self.price = c_price
        self.brand = c_brand
        print('Car 类型的对象初始化完毕,对象属性已添加完毕')

c1 = Car("black","A8L Horch","100000",c_brand="Audi")
print(c1)#<__main__.Car object at 0x000001E7233E2FF0> 此为16进制(0-9 + ABCDEF) 内存地址
print(c1.__dict__)#__dict__会将对象中的所有属性以字典的形式输出出来

'''定义在类外面的称之为函数,定义在类里面的称之为方法'''
#__init__ :初始化方法.对象创建后自动调用,主要用于设置对象的初始状态(设置对象属性)

c2 = Car("grey","YU 7","270000",c_brand="Xiaomi")
print(c2.__dict__)

#1.2 实例方法
class Car:
    def __init__(self,c_color,c_model,c_price,c_brand):
        # self:方法的第一个参数,表示当前创建的实例对象
        self.color = c_color
        self.model = c_model
        self.price = c_price
        self.brand = c_brand
        print('Car 类型的对象初始化完毕,对象属性已添加完毕')

#定义实例方法
    def running(self):
        print(f'Car {self.brand} {self.model}正在高速行驶中...')

    def total_cost(self,discount,rate): #可在此处直接给参数设置默认值 rate=0.06 如若不传rate,将使用默认值
        """
        计算提车的总费用,包含车的价格,税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = discount * self.price + rate * self.price
        return total_cost

#测试
c1 = Car(c_brand='Porsche',c_color='white',c_model="911 GT S",c_price=1500000,)
c1.running()

total_c1 = c1.total_cost(discount=0.85,rate=0.06)
print(f'提车的总费用为{total_c1:.2f}')#f'<UNK>{变量.2f}' 显示两位小数

#1.3 魔法方法 :Python中以双下划线开头和结尾的特殊方法,用于定义类的特殊行为
#如__init__ 不需要手动调用,Python会在合适时机自动调用
"""
__init__        初始化方法
__str__         字符串表示的方法
比较两个对象的大小关系
__eq__          比较是否相等(equal)
__lt__ / __le__ 比较是否<= less than / less than or equal
__gt__ / __ge__ 比较是否>= greater than / greater than or equal
"""

class Car:
    def __init__(self,c_color,c_model,c_price,c_brand):
        # self:方法的第一个参数,表示当前创建的实例对象
        self.color = c_color
        self.model = c_model
        self.price = c_price
        self.brand = c_brand
        print('Car 类型的对象初始化完毕,对象属性已添加完毕')

    def running(self):
        print(f'Car {self.brand} {self.model}正在高速行驶中...')
    def __str__(self):
        return f'Car {self.brand} {self.model} {self.price}'
    def __eq__(self,other):
        return self.price == other.price and self.brand == other.brand and self.model == other.model and self.color == other.color
    def __lt__(self,other):
        return self.price < other.price and self.brand < other.brand

c3 = Car(c_price=510000,c_model="E300L",c_brand="Mercedes",c_color="black",)
c4 = Car(c_model="E300L",c_brand="Mercedes",c_color="black",c_price=510000)
print(c3 == c4)
print(c4 < c3)#虽定义的是lt 此处如果是> 也可执行 即结果取反

#1.4 实例属性与类属性
#实例属性: 属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据) 实例对象.属性
#类属性: 属于类本身的属性,所有实例共享(所有对象共享的数据或配置)  类名.属性
#注: __init__后定义的都是实例属性     通过实例查找属性时,先查找实例属性,实例属性不存在时,再查找类属性

class MobilePhone:
    #类属性
    camera = 4
    subsidy_rate = 0.1

    def __init__(self,p_color,p_model,p_price,p_brand):
        #实例属性
        self.color = p_color
        self.model = p_model
        self.price = p_price
        self.brand = p_brand
        print('Mobile Phone 类型的对象初始化完毕,对象属性已添加完毕')

    def running(self):
        print(f'Mobile Phone {self.brand} {self.model}正在运行中...')

    def total_cost(self,discount,rate):
        total_cost = discount * self.price + rate * self.price
        return total_cost

p1 = MobilePhone(p_color= 'red', p_brand= "Honor", p_model= "Magic8Pro", p_price= 6399)
print(p1.__dict__)
p1.running()

print(p1.brand)
print(p1.camera)#通过实例对象,查找属性时,会先查找实例属性,实例属性不存在,再查找类属性

print(MobilePhone.camera)#直接查找类属性

#1.5 案例
'''采用面向对象编程的四向,完成教务管理系统的开发:增删改查,展示全部学生成绩'''
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f'姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}|总分:{self.chinese + self.math + self.english}'
    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#测试
s1=Student('lyg',91,95,95)#输数字时加引号导致type变成字符串
print(s1)

s1.update_score(english=96)
print(s1)

class EduManagement:
    sys_version = "1.0"
    sys_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] #列表,记录的是在校学生的成绩

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名:")

        #判断学生姓名是否存在,如果存在,则添加失败(不能重复添加)
        for s in self.student_list:
            if s.name == name:
                print('该学生已经存在,添加失败!')
                return

        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))

        #判断分数是否在0~100之间
        if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print('学生信息添加成功~')
        else:
            print('学生成绩必须在0~100之间!')

    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名:")

        #根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f'当前成绩:{s}')

                chinese =int(input("请输入修改后的语文成绩:"))
                math = int(input("请输入修改后的数学成绩:"))
                english = int(input("请输入修改后的英语成绩:"))

                #判断分数是否合规
                if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print('成绩修改成功')
                    print(f'修改后的成绩:{s}')
                    return
                else:
                    print('各科成绩需在0~100之间!')
                    return

        print('未找到目标学生,修改失败')

    #删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print('学生信息已删除')
                return
        print('未找到目标学生.删除失败')

    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print('学生信息已删除')
                return
        print('未找到目标学生')

    #展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    #运行系统
    def run(self):
        print(f'欢迎使用教务管理系统 V{EduManagement.sys_version} ')

        while True:
            print("##"*40)
            print('# 1.添加学生  2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统')
            print("##" * 40)

            choice = input("请选择要执行的操作:,输入1~6  :")
            match choice:
                case "1":
                    self.add_student()
                case '2':
                    self.update_student()
                case '3':
                    self.delete_student()
                case '4':
                    self.query_student()
                case '5':
                    self.list_student()
                case '6':
                    print('Bye')
                    break

if __name__ == '__main__':
    edu = EduManagement()
    edu.run()
