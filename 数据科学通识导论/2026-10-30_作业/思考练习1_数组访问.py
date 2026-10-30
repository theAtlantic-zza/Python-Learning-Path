import numpy as np

names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])

# 1. 一维数组访问
print('\n索引1、2、4的课程：', subjects[[1, 2, 4]])
print('负数索引取方绮雯：', names[-3])
print('从索引2到最后的姓名：', names[2:])
print('索引2、3、4的课程：', subjects[2:5])
print('英语和物理：', subjects[(subjects == 'English') | (subjects == 'Physics')])

# 2. 二维数组访问
print('行索引1、4的成绩：\n', scores[[1, 4]])
print('行索引2、4的数学和Python成绩：\n', scores[[2, 4]][:, [0, 2]])
print('所有同学的数学和艺术成绩：\n', scores[:, [0, 4]])
student_mask = (names == '王微') | (names == '刘旭阳')
subject_mask = (subjects == 'English') | (subjects == 'Art')
print('王微、刘旭阳的英语和艺术成绩：\n', scores[student_mask][:, subject_mask])

# 3. 生成2×5数组
numbers = np.arange(10, 20).reshape(2, 5)
print('10到19组成的2×5数组：\n', numbers)
