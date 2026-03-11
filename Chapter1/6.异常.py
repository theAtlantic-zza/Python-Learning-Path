print("*" * 30)
#6.1 异常
'''异常 Bug 程序运行中出现的错误,会中断程序的正常执行流程
        作用:保证数据,逻辑的正确性,在开发阶段,尽量发现更多问题,尽早解决问题
        类型:NameError, KeyError, TypeError
        处理方案: 1.不做处理 有bug后整个程序中断执行
                 2.捕获异常 处理完异常后程序继续执行
        语法: try:
                 可能出现异常的业务代码
                 ..
             except [异常类型 as 变量名]
                出现异常时的预案
            finally:
                不管是否出现异常,都会执行的代码
'''
try:
    print(101)
    # print(my_name)
    # print(1/0)
    # print('ABC'[10])
except NameError as e: #捕获的是NameError 类型的异常
    print('名字不存在,请检查: 异常信息:',e)
except ZeroDivisionError as e:
    print('0不能做被除数: 异常信息:',e)
except IndexError as e:
    print('索引错误: 异常信息:',e)

except Exception as e: print('程序运行出错了,请联系管理员, 错误信息:',e)#捕获所有异常

finally:#无论程序是否正常运行 finally中的代码都会运行
    print('666 debug ASAP')

#6.2 异常的传递:异常在函数调用中层层上报,直到有人resolve,或者程序collapse
def fun1():
    print('fun1..running')
    fun2()

def fun2():
    print('fun2..running')
    fun3()

def fun3():
    print('fun3..running')
    print(my_color)

try:
    fun1()
except Exception as e:
    print('程序运行出错,请联系管理员,错误信息:',e)

print()
print()

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

            try:
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
                    case _:
                        print('输入错误,请选择1-6之间的菜单功能')

            except ValueError as e:
                print('输入的数据有问题,请检查后重新输入:',e)
            except Exception as e:
                print('程序运行出错了,请重新选择')

if __name__ == '__main__':
    edu = EduManagement()
    edu.run()