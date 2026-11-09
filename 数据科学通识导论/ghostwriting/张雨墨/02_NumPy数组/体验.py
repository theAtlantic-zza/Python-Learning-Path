import numpy as np

# 一维数组
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
courses = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])

print('学生姓名：', names)
print('课程名称：', courses)
print('维数：', names.ndim)
print('元素个数：', names.size)
print('形状：', names.shape)
print('数据类型：', names.dtype)
print('第三个姓名：', names[2])
print('倒数第三门课程：', courses[-3])
print('索引1到3的姓名：', names[1:4])
print('索引0、2、4的课程：', courses[[0, 2, 4]])
print('间隔取课程：', courses[:-1:2])

condition = (names == '王微') | (names == '钱易铭')
print('筛选姓名：', names[condition])

# 二维数组
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])

print('成绩：\n', scores)
print('维数：', scores.ndim)
print('元素个数：', scores.size)
print('形状：', scores.shape)
print('数据类型：', scores.dtype)
print('行索引1、列索引0：', scores[1, 0])
print('行索引1、3：\n', scores[[1, 3]])
print('所有行的前两列：\n', scores[:, :2])
print('行索引0、3，列索引1到3：\n', scores[[0, 3], 1:4])
print('两个位置的成绩：', scores[[1, 3], [0, 1]])

part = scores[[1, 3]]
print('行索引1、3的前两列：\n', part[:, :2])

condition = (names == '肖良英') | (names == '方绮雯')
part = scores[condition]
print('两位同学的成绩：\n', part)
condition = (courses == 'Math') | (courses == 'Python')
print('两位同学的数学和Python成绩：\n', part[:, condition])
