#Produce by zza
import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(1, 10).reshape(3, 3),
                    index=list("abc"), columns=["one", "two", "three"])
print("\n原始 DataFrame：\n", data)

print("two、three列：\n", data[["two", "three"]])

print("第0、2行：\n", data.iloc[[0, 2], :])

print("第0、2列：\n", data.iloc[:, [0, 2]])

print("第0、2行与第0、2列交叉数据：\n", data.iloc[[0, 2], [0, 2]])

data1 = data[data.iloc[:, 1] > 2].copy()
print("第1列大于2的行：\n", data1)

data1["four"] = 10
print("添加 four：\n", data1)
data1[data1 > 9] = 8
print("大于9的值改为8：\n", data1)
data1 = data1.drop(data1.index[:2])
print("删除第0、1行：\n", data1)
