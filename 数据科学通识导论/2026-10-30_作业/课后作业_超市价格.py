import numpy as np

# 1. 超市与水果
supermarkets = np.array(['大润发', '沃尔玛', '联华', '农工商'])
fruits = np.array(['苹果', '香蕉', '桔子', '芒果'])
print('超市：', supermarkets)
print('水果：', fruits)

# 2. 随机价格
prices = np.random.randint(4, 11, size=(4, 4))
print('原始价格：\n', prices)

# 3. 大润发苹果、联华香蕉涨价
prices[0, 0] += 1
prices[2, 1] += 1

# 4. 农工商所有水果降价
prices[3, :] -= 2
print('调价后价格：\n', prices)

# 5. 苹果和芒果的均价
mean_prices = prices[:, [0, 3]].mean(axis=0)
print('苹果均价：', mean_prices[0])
print('芒果均价：', mean_prices[1])

# 6. 桔子最贵的超市
orange_prices = prices[:, 2]
print('桔子最高价格：', orange_prices.max())
print('桔子最贵的超市：', supermarkets[orange_prices == orange_prices.max()])
