"""封装:把数据(属性)和操作数据的函数(方法)捆绑在一起,形成一个独立的单元(类),并隐藏内部的实现细节,只对外暴露必要的功能(方法)
"""
# 面向对象：类属性、实例属性、私有属性、私有方法

class Car:
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