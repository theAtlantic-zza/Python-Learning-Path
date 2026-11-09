import numpy as np
import pandas as pd

numbers = np.arange(1, 10).reshape(3, 3)
data = pd.DataFrame(numbers, index=["a", "b", "c"],
                    columns=["one", "two", "three"])
print("\n创建表格：\n", data)
print("选择两列：\n", data.loc[:, ["two", "three"]])
print("第0行：\n", data.iloc[0])
print("第2行：\n", data.iloc[2])
print("第0列：\n", data.iloc[:, 0])
print("第2列：\n", data.iloc[:, 2])
print("指定行列交叉数据：\n", data.iloc[[0, 2], [0, 2]])
condition = data["two"] > 2
data1 = data.loc[condition, :].copy()
print("筛选后的 data1：\n", data1)
data1.loc[:, "four"] = 10
print("新增 four 列：\n", data1)
data1[data1 > 9] = 8
print("修改后：\n", data1)
delete_rows = data1.index[[0, 1]]
data1.drop(index=delete_rows, inplace=True)
print("删除两行后：\n", data1)
