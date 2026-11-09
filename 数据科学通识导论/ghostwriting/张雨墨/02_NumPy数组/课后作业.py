import numpy as np

shops = np.array(['大润发', '沃尔玛', '联华', '农工商'])
fruits = np.array(['苹果', '香蕉', '桔子', '芒果'])
print('超市：', shops)
print('水果：', fruits)

prices = np.random.randint(4, 11, (4, 4))
print('原来的价格：\n', prices)

prices[0, 0] = prices[0, 0] + 1
prices[2, 1] = prices[2, 1] + 1
prices[3, :] = prices[3, :] - 2
print('调整后的价格：\n', prices)

apple_average = prices[:, 0].mean()
mango_average = prices[:, 3].mean()
print('苹果平均价格：', apple_average)
print('芒果平均价格：', mango_average)

orange = prices[:, 2]
highest = orange.max()
print('桔子最贵的超市：')
for i in range(len(shops)):
    if orange[i] == highest:
        print(shops[i])
