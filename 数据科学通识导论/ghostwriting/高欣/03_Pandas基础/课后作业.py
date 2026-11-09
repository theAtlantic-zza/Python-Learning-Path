import numpy as np
from pandas import DataFrame

array = np.arange(1, 10).reshape(3, 3)
data = DataFrame(array, index=list("abc"), columns=["one", "two", "three"])
print("\n原始表格：\n", data)
print("取 two、three：\n", data.loc[:, ["two", "three"]])
print("第0和第2行：\n", data.iloc[[0, 2]])
print("第0和第2列：\n", data.iloc[:, [0, 2]])
print("对应行列的交叉数据：\n", data.iloc[[0, 2], [0, 2]])
data1 = data.loc[data["two"] > 2].copy()
print("第1列大于2：\n", data1)
data1["four"] = 10
print("加入 four 列：\n", data1)
data1[data1 > 9] = 8
print("大于9改成8：\n", data1)
row_labels = list(data1.index[:2])
data1 = data1.drop(row_labels)
print("删除前两行后：\n", data1)
