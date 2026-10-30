import numpy as np

# 一维数组体验
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
print('姓名：', names)
print('课程：', subjects)
print('姓名数组维数：', names.ndim)
print('姓名数组元素个数：', names.size)
print('姓名数组形状：', names.shape)
print('姓名数组元素类型：', names.dtype)
print('姓名索引2：', names[2])
print('课程倒数第3个：', subjects[-3])
print('姓名索引1到3：', names[1:4])
print('课程索引0、2、4：', subjects[[0, 2, 4]])
print('课程间隔切片：', subjects[:-1:2])
print('姓名筛选：', names[(names == '王微') | (names == '钱易铭')])

# 二维数组体验
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])
print('\n成绩数组：\n', scores)
print('成绩数组维数：', scores.ndim)
print('成绩总个数：', scores.size)
print('成绩数组形状：', scores.shape)
print('成绩元素类型：', scores.dtype)
print('行索引1、列索引0的成绩：', scores[1, 0])
print('行索引1、3的成绩：\n', scores[[1, 3]])
print('所有行的列索引0、1：\n', scores[:, [0, 1]])
print('行索引0、3的列索引1到3：\n', scores[[0, 3], 1:4])
print('配对位置[1,0]和[3,1]：', scores[[1, 3], [0, 1]])
print('行索引1、3与列索引0、1组成的小表：\n', scores[[1, 3]][:, [0, 1]])
student_mask = (names == '肖良英') | (names == '方绮雯')
subject_mask = (subjects == 'Math') | (subjects == 'Python')
print('按姓名筛选：\n', scores[student_mask])
print('按姓名和课程筛选：\n', scores[student_mask][:, subject_mask])
