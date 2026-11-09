import numpy as np

names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
courses = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])

print('索引1、2、4的课程：', courses[[1, 2, 4]])
print('用负数索引取方绮雯：', names[-3])
print('索引2到最后的姓名：', names[2:])
print('索引2到4的课程：', courses[2:5])

condition = (courses == 'English') | (courses == 'Physics')
print('英语和物理：', courses[condition])

print('行索引1、4的成绩：\n', scores[[1, 4]])
part = scores[[2, 4]]
print('行索引2、4的数学和Python成绩：\n', part[:, [0, 2]])
print('所有同学的数学和艺术成绩：\n', scores[:, [0, 4]])

condition = (names == '王微') | (names == '刘旭阳')
part = scores[condition]
condition = (courses == 'English') | (courses == 'Art')
print('王微和刘旭阳的英语、艺术成绩：\n', part[:, condition])

numbers = np.arange(10, 20)
numbers = numbers.reshape(2, 5)
print('10到19组成的二维数组：\n', numbers)
