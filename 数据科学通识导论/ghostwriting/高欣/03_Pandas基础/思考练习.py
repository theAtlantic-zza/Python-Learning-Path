from pandas import Series

s = Series([30, 25, 27, 41, 25, 34], index=["a", "b", "c", "d", "e", "f"])
print("\nSeries：\n", s)
s["g"] = 27
print("增加元素：\n", s)
s["d"] = 40
print("修改元素：\n", s)
print("筛选结果：\n", s.loc[s > 27])
s = s.drop([s.index[1], s.index[2], s.index[3]])
print("删除位置1到3的数据：\n", s)
