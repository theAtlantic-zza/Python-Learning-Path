import numpy as np

#1.一维数组体验：创建、访问、切片、筛选
#1.1创建：np.array()函数，将列表转换成NumPy的ndarray数组
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
print('姓名数组：', names)
print('课程数组：', subjects)
print('数组类型：', type(names))#type()是Python内置函数，查看对象类型

#1.2属性
print('姓名数组维数：', names.ndim)#ndim属性：一维数组是1
print('姓名数组元素个数：', names.size)#size属性：总元素个数
print('姓名数组形状：', names.shape)#shape属性：一维数组形状为(5,)
print('姓名数组元素类型：', names.dtype)#dtype属性：元素类型

#1.3访问：正数索引从0开始，负数索引从-1开始
print('姓名索引2：', names[2])
print('课程倒数第3个：', subjects[-3])

#1.4切片：开始索引包含，结束索引不包含；步长省略时为1
print('课程索引0、2、4：', subjects[[0, 2, 4]])#内层列表指定要取的多个位置
print('姓名索引1到3：', names[1:4])
print('课程从开头到最后一个之前，每隔2个取值：', subjects[:-1:2])

#1.5筛选：比较得到布尔数组，保留True位置的元素
name_mask = (names == '王微') | (names == '钱易铭')
print('姓名筛选条件：', name_mask)
print('王微和钱易铭：', names[name_mask])


#2.二维数组体验：创建、访问、切片、筛选
#2.1创建
scores = np.array([
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80]
])

print('\n成绩数组：\n', scores)
print('成绩数组维数：', scores.ndim)#ndim属性：二维数组是2
print('成绩总个数：', scores.size)#size属性：5×7=35
print('成绩数组形状：', scores.shape)#shape属性：(5, 7)，5行7列
print('成绩元素类型：', scores.dtype)#dtype属性：整数类型

#2.2访问：scores[行索引, 列索引]
print('第1行第0列的成绩：', scores[1, 0])
print('第0名同学的全部成绩：', scores[0, :])
print('所有同学的数学成绩：', scores[:, 0])

#2.3切片与位置选取
print('行索引1、3的全部成绩：\n', scores[[1, 3]])
print('所有行的列索引0、1：\n', scores[:, [0, 1]])
print('行索引0、3的列索引1到3：\n', scores[[0, 3], 1:4])
print('行索引1、3和列索引0、1分别配对：', scores[[1, 3], [0, 1]])#只取[1,0]和[3,1]
print('行索引1、3与列索引0、1组成的小表：\n', scores[[1, 3]][:, [0, 1]])#先取行，再取列

#2.4筛选：姓名对应行，课程对应列
student_mask = (names == '肖良英') | (names == '方绮雯')
subject_mask = (subjects == 'Math') | (subjects == 'Python')
print('肖良英、方绮雯的全部成绩：\n', scores[student_mask, :])
print('肖良英、方绮雯的数学和Python成绩：\n', scores[student_mask][:, subject_mask])


#3.思考与练习
#3.1一维数组访问
#3.11取索引1、2、4的课程；用负数索引取方绮雯
print('索引1、2、4的课程：', subjects[[1, 2, 4]])
print('负数索引取方绮雯：', names[-3])

#3.12切片：取索引2到最后的姓名；取索引2、3、4的课程
print('从索引2到最后的姓名：', names[2:])
print('索引2到4的课程：', subjects[2:5])

#3.13布尔条件筛选英语和物理；|表示满足任意一个条件，条件分别加括号
subject_mask = (subjects == 'English') | (subjects == 'Physics')
print('英语和物理：', subjects[subject_mask])

#3.2二维数组访问
#3.21取行索引1、4，也就是第2名和第5名同学的全部成绩
print('行索引1、4的成绩：\n', scores[[1, 4]])

#3.22取行索引2、4同学的数学、Python成绩，课程列索引是0、2
print('行索引2、4的数学和Python成绩：\n', scores[[2, 4]][:, [0, 2]])
#踩坑：先取两行，再取两列，得到2×2数组
#scores[[2, 4], [0, 2]]只会取出两个位置scores[2, 0]和scores[4, 2]

#3.23取所有同学的数学和艺术成绩，课程列索引是0、4
print('所有同学的数学和艺术成绩：\n', scores[:, [0, 4]])

#3.24按姓名和课程名称筛选，先筛行再筛列
student_mask = (names == '王微') | (names == '刘旭阳')
subject_mask = (subjects == 'English') | (subjects == 'Art')
print('王微、刘旭阳的英语和艺术成绩：\n', scores[student_mask][:, subject_mask])

#3.3生成10~19组成的2×5数组
#np.arange()函数：不包含结束值；
#reshape()方法：调整形状，元素总数不变
numbers = np.arange(10, 20).reshape(2, 5)
print('10~19组成的2×5数组：\n', numbers)


#4.课后作业：四个超市的水果价格
#4.1创建超市、水果名称数组
supermarkets = np.array(['大润发', '沃尔玛', '联华', '农工商'])
fruits = np.array(['苹果', '香蕉', '桔子', '芒果'])
print('\n超市顺序：', supermarkets)
print('水果顺序：', fruits)

#4.2创建4×4价格数组；np.random.randint()函数：生成随机整数
#范围[4, 11)，所以可能生成4~10
prices = np.random.randint(4, 11, size=(4, 4))
print('原始价格（每行一个超市，每列一种水果）：\n', prices)

#4.3大润发的苹果、联华的香蕉分别涨价1元
prices[0, 0] += 1#第0行大润发、第0列苹果；+=1是在原值上加1并保存
prices[2, 1] += 1#第2行联华、第1列香蕉

#4.4农工商所有水果减价2元
prices[3, :] -= 2#第3行农工商，:表示所有列
print('调整后的价格：\n', prices)

#4.5按调整后的价格统计苹果、芒果的均价
#mean()方法：求平均；axis参数：0沿行方向竖着计算，得到每列的均价
mean_prices = prices[:, [0, 3]].mean(axis=0)
print('四个超市苹果均价：', mean_prices[0])
print('四个超市芒果均价：', mean_prices[1])

#4.6找出桔子最贵的超市名称；max()方法：求最大值
orange_prices = prices[:, 2]
highest_price = orange_prices.max()
print('桔子最高价格：', highest_price)
print('桔子最贵的超市：', supermarkets[orange_prices == highest_price])
