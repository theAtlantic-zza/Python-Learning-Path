import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(1, 10).reshape(3, 3),
                    index=["a", "b", "c"], columns=["one", "two", "three"])
print("\n初始数据：\n", data)
print("two 和 three：\n", data[["two", "three"]])
rows = [0, 2]
cols = [0, 2]
print("第0、2行：\n", data.iloc[rows])
print("第0、2列：\n", data.iloc[:, cols])
print("指定行列交叉数据：\n", data.iloc[rows, cols])
mask = data.iloc[:, 1] > 2
data1 = data[mask].copy()
print("筛选结果：\n", data1)
data1["four"] = [10] * len(data1)
print("增加一列后：\n", data1)
mask = data1 > 9
data1[mask] = 8
print("替换数值后：\n", data1)
data1 = data1.drop(index=data1.index[0:2])
print("删去第0、1行后：\n", data1)
