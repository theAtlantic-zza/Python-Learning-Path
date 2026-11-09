import pandas as pd

s = pd.Series({"a": 30, "b": 25, "c": 27, "d": 41, "e": 25, "f": 34})
print("\n初始数据：\n", s)
s.loc["g"] = 27
print("添加数据后：\n", s)
s.loc["d"] = 40
print("修改数据后：\n", s)
result = s[s > 27]
print("值大于27：\n", result)
delete_index = s.index[[1, 2, 3]]
s = s.drop(delete_index)
print("删除位置1至3后：\n", s)
