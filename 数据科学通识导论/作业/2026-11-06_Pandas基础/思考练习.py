#Produce by zza
import pandas as pd

series = pd.Series([30, 25, 27, 41, 25, 34], index=list("abcdef"))
print("\n原始 Series：\n", series)
series["g"] = 27
print("增加 g：\n", series)
series["d"] = 40
print("修改 d：\n", series)
print("大于27的数据：\n", series[series > 27])
series = series.drop(series.index[1:4])
print("删除位置1、2、3：\n", series)
