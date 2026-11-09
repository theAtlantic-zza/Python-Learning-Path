import numpy as np

names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])

english = scores[:, 1] - 3
print('英语成绩减3分：', english)

for i in range(len(names)):
    average = scores[i].mean()
    print(names[i], '所有科目的平均分：', average)

numbers = np.random.uniform(-1, 1, (3, 4))
print('随机数组：\n', numbers)
print('所有元素的和：', numbers.sum())
