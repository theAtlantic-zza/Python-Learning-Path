import pandas as pd

values = [30, 25, 27, 41, 25, 34]
labels = ["a", "b", "c", "d", "e", "f"]
series = pd.Series(values, index=labels)
print("\n创建 Series：\n", series)
series = pd.concat([series, pd.Series([27], index=["g"])])
print("添加 g 后：\n", series)
series.loc["d"] = 40
print("更改 d 后：\n", series)
mask = series > 27
print("符合条件的数据：\n", series.loc[mask])
series.drop(index=series.index[1:4], inplace=True)
print("删除位置1、2、3后：\n", series)
