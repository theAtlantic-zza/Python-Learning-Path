"""封装:把数据(属性)和操作数据的函数(方法)捆绑在一起,形成一个独立的单元(类),并隐藏内部的实现细节,只对外暴露必要的功能(方法)
"""
from random import choice


# 面向对象：类属性、实例属性、私有属性、私有方法

#7.1 私有属性 私有方法
class Car(object): #所有类都有一个父类:object
    # 类属性：所有实例对象共享
    wheel = 4  # 轮胎数量
    tax_rate = 0.1  # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_owner):
        # 实例属性：每个对象自己独有
        self.color = c_color  # 车身颜色
        self.brand = c_brand  # 汽车品牌
        self.name = c_name  # 汽车型号
        self.__owner = c_owner  # __ 私有属性,类外不能直接访问

    def start(self):
        # 公有方法：类外可以直接调用
        print(f'{self.brand} {self.name} 正在启动...')

    def stop(self):
        # 公有方法：类外可以直接调用
        print(f'{self.brand} {self.name} 停止行驶...')

    def __control_fuel(self):
        # __ 私有方法：类外不能直接调用
        print(f'{self.brand} {self.name} 控制燃油分配...')

    def charge(self):
        print(f'{self.brand} {self.name} 正在补充燃料...')

    def get_owner(self):#通过公共方法访问私有属性,但对输出进行限制
        return self.__owner[0:1] + '**'

'''类属性属于类,所有对象共享；实例属性属于对象,每个对象独有'''
'''__属性名表示私有属性；__方法名表示私有方法,主要在类内部使用'''

if __name__ == '__main__':
    car = Car(c_brand='Audi',c_color='black',c_name='A6',c_owner='zzzzzzza')
    print(car.brand)
    print(car.name)
    print(car.color)
    print(car.get_owner()) #已进行加密

#注意事项:Python中没有真正的私有机制
    print(car._Car__owner)
    car._Car__control_fuel()

#7.2 继承:描述的是两个类之间的关系 子类继承父类,就可以获取到父类的属性和方法,从而实现代码复用和功能扩展

#7.21
#燃油车
class FuelCar(Car):
    pass

#电车
class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1 = FuelCar(c_brand='BMW',c_name='X7',c_color='white',c_owner='张三')
    c2 = ElectricCar(c_brand='Mercedes',c_name='E300L',c_color='black',c_owner='李四')
    c1.start()
    c2.start()
    print(c1.get_owner())
    print(c2.get_owner())
    print(c1.brand)
    '''print(c1.brand()  TypeError: 'str' object is not callable 表示把字符串属性当方法调用了；属性不加(),方法才加()'''
    print(c2.brand)
    print(c1.name)
    print(c2.name)

#7.22 重写:指子类继承父类后,若父类中的方法不满足需求,可以在子类中重新定义父类中已有的方法(方法名相同),从而实现用子类的实现替换父类的实现
#         注:若子类在重写父类的方法时,需要调用父类的方法,可以通过 父类名.方法名(self)/super().方法名 来调用
class FuelCar(Car): #重新定义同名类会覆盖类名指向的新定义,但已经创建的旧对象不会自动更新
    def charge(self):
        #方式一: super().方法名()
        # super().charge()

        #方法二:类名.方法名(self)
        Car.charge(self) #必须传递self
        print(f'{self.brand} {self.name} 正在加油...')
c1 = FuelCar(c_brand='BMW',c_name='X7',c_color='white',c_owner='张三')
c1.charge()

#7.23 多继承:一个子类可同时继承多个父类,ta会将多个父类中的非私有属性和方法同时继承下来
"""注: 当一个类继承了多个父类时,默认优先使用第一个父类中的同名属性或方法,可以使用 类名.__mro__ 属性 或 类名.mro()方法查看调用顺序"""
class ADS: #Autonomous Driving System
    def __init__(self,version='V1.0'):
        self.version = version

    def run(self):
        print(f'使用ADS智驾系统{self.version}正在接管...')

#Porsche Panamera
class PorschePanamera(Car,ADS):#多继承写法是 class 子类(父类1,父类2): 父类之间用逗号隔开,冒号放最后
    def __init__(self, c_brand, c_name, c_color, c_owner, version='V1.0'):
        super().__init__(c_color, c_brand, c_name, c_owner) #调用Car的init
        ADS.__init__(self, version) #调用ADS的int

    def run(self):
        Car.start(self)
        ADS.run(self)

# MRO: Method Resolution Order 方法解析顺序
c = PorschePanamera(c_brand='Porsche', c_name='Panamera', c_color='Sakura', c_owner='laozi')
print(PorschePanamera.mro())
print(c.__dict__)

c.run()

#7.3 多态:指同一个方法,在不同对象身上有不同执行效果

class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand}{self.name}正在充电...')

def handle_charge(car: Car): #函数参数类型声明---指定的是父类型
    car.charge()

handle_charge(ElectricCar(c_brand='Tesla',c_name='Model Y',c_color='black',c_owner='brother'))
handle_charge(FuelCar(c_brand='Nissan',c_name='Qijun',c_color='red',c_owner='mom'))

#7.31 鸭子类型

'''鸭子类型是多态的一种体现；不关心对象属于哪个类,只关心对象有没有需要调用的方法'''
'''只要对象有同名方法,就可以被同一段代码调用；像鸭子一样走路和叫,就可以当鸭子用'''

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')

def go_swimming(duck: Duck):
    duck.swimming()

go_swimming(Dog('Rich', 4))
go_swimming(Duck('Raffle', 5))
go_swimming(Pig('Piggy', 6))

#7.4 案例
"""基于面向对象的编程思想完成如下系统开发

某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。
系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。
设计并实现这个图书管理系统

核心功能： 增删改查
1. 会员登录：会员通过卡号和密码登录系统
2. 借书：会员可以借阅库存中有余量的图书
3. 还书：会员可以归还借阅的图书
4. 查看我的借阅：展示当前会员已经借阅的图书列表
5. 退出系统

借阅规则：
1. 普通会员最多可借3本
2. VIP会员最多可借 6+VIP等级 本（VIP等级，默认为1）


注意：
1. 登录成功（卡号和密码均正确）后，才可以访问该系统
2. 图书库存不足，或者当前会员借书数量达到最大借书数量，不能再借新书"""

from abc import ABC, abstractmethod
import json

#书籍类
class Book:
    def __init__(self,book_id, title, author, total_num):
        self.book_id = book_id #书籍编号
        self.title = title  #书籍标题
        self.author = author  #作者
        self.total_num = total_num  #总数量
        self.__available_num = total_num  #可借阅数量

    def borrow_book(self): #借书
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self): #还书
        self.__available_num += 1

    def get_available_num(self): #获取可用数量
        return self.__available_num

#抽象类:是一种只能被继承,不能被直接实例化的类,作用就是规定子类必须要实现哪些方法,强制子类必须遵守的统一代码规范
# Python中的抽象类,需要继承 abc 模块中的ABC类 --> ABC: Abstract Base Class


#会员类
class Member(ABC):
    def __init__(self,member_id,name, password):
        self.member_id = member_id #会员卡号
        self.name = name  #会员姓名
        self.__password = password  #会员密码
        self.__borrowed_books = []  #已借阅书籍列表

    def borrow_book(self,book:Book): #借阅书籍
        # 判断当前会员借阅数量是否达到限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print('借阅失败,您的借阅数量已达上限!')
            return False

        #判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f'{self.name}已成功借阅图书{book.title}')
            return True
        else:
            print(f'借阅图书失败,图书{book.title}已被借完!')
            return False

    def return_book(self,book:Book):  #归还书籍
        # 判断当前会员是否借阅了该书籍
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f'{self.name}已成功归还图书{book.title}')
        else:
            print(f'归还失败,这不是您借阅的图书!{book.title}')

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    #获得会员最大借阅数量(需要在子类中实现)
    @abstractmethod #抽象方法装饰器
    def get_max_books(self)->int:
       pass

class NormalMember(Member):  #普通会员类
    def get_max_books(self)->int:
        return 3

class VIPMember(Member):
    def __init__(self, member_id, name, password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level #会员等级

    def get_max_books(self)->int:
        return self.vip_level + 6

#图书馆管理系统
class LlibrarySystem:
    def __init__(self):
        self.books = {}  #书籍列表 --> {“AI001": Book对象,"AI002": Book对象,...}
        self.members = {} #会员列表  --> {“N001": Member对象,"N002": Member对象,...}
        self.current_members : Member | None = None #当前登录会员
        #加载数据(书籍,会员)
        self.load_books_data(self)
        self.load_members_data(self)

    def load_books_data(self,books):
        #加载 data/books.json 中的数据
        with open('data/books.json','r',encoding='utf-8') as f:

            '''with open()用于打开文件,代码块执行完会自动关闭文件；self会自动传入,调用方法时不用手动传self'''

            books_data = json.load(f)
            for book in books_data:
                self.books[book['id']] = Book(book['id'],book['title'],book['author'],book['total_num'])
            print('加载书籍信息成功')
    def load_members_data(self,members):
        # 加载 data/member.json 中的数据
        with open('data/members.json', 'r', encoding='utf-8') as f:

            members_data = json.load(f)
            for member in members_data:
                if member["id"].startswith("N"):
                    self.members[member["id"]] = NormalMember(member["id"], member["name"], member["password"])
                elif member["id"].startswith("V"):
                    self.members[member["id"]] = VIPMember(member["id"], member["name"], member["password"],member["vip_level"])
                print("加载会员数据成功！")

    def login(self):#登录
        while True:
            print("登录")
            member_id = input('请输入会员卡号:  ')
            password = input('请输入会员密码: ')

            #判断会员卡号是否存在
            if member_id not in self.members:
                print('登录失败,会员卡号不存在!')
                continue

            #判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print(f'Login Success,Welcome {member.name}!')
                self.current_members = member
                return True
            else:
                print('Login Fail, Wrong Password!')
                continue

    def borrow_book(self):
        #1.展示当前图书馆的图书列表
        for book in self.books.values():
            print(f'编号:{book.book_id},标题:{book.title},作者:{book.author},总数:{book.total_num},可用:{book.get_available_num()}')

        #2.获取用户输入的图书编号,执行借书操作
        book_id = input('请输入要借阅的图书编号')
        if book_id not in self.books:
            print('借书失败,图书编号不存在!')
            return
        self.current_members.borrow_book(self.books[book_id])

    def return_book(self):  # 归还图书
        borrowed_books = self.current_members.get_borrowed_books()

        if len(borrowed_books) == 0:
            print("您当前没有借阅任何图书！")
            return

        print("【已经借阅的图书列表：】")
        for book in borrowed_books:
            print(f"编号：{book.book_id}，标题：{book.title}")

        book_id = input("请输入要归还的图书编号：").strip()

        if book_id not in self.books:
            print("还书失败，图书编号不存在！")
            return

        self.current_members.return_book(self.books[book_id])

    def show_borrowed_books(self):  # 查看借阅
        borrowed_books = self.current_members.get_borrowed_books()

        if len(borrowed_books) > 0:
            print("【已经借阅的图书列表：】")

            for book in borrowed_books:
                print(f"编号：{book.book_id}，标题：{book.title}")
        else:
            print("您没有借阅任何图书！")

    def run(self):
        if self.login():
            while True:
                print('\n1.借阅图书')
                print('2.归还图书')
                print('3.查看借阅图书')

                choice = input('请选择操作(1-4):  ')
                match choice:
                    case '1':
                        self.borrow_book()
                    case '2':
                        self.return_book()
                    case '3':
                        self.show_borrowed_books()
                    case '4':
                        print('Log out, Bye')
                        break
                    case _:
                        print('无效选项,重新选择')


if __name__ == '__main__':
    ls = LlibrarySystem()
    ls.run()

