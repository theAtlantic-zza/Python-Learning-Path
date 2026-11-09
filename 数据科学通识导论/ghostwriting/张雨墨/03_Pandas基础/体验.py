import pandas as pd

# Series
heights = {"10": 182, "11": 189, "12": 176, "15": 185, "18": 190}
player = pd.Series(heights)
print(player)
print(player.index)
print(player.values)
print(player.loc["11"])
print(player.loc[["10", "18"]])
print(player.iloc[0:3])
print(player[player >= 185])

player.loc["10"] = 184
player.iloc[1:3] = 180
print(player)
player.loc["20"] = 192
player.loc["21"] = 187
print(player)
player = player.drop(["12", "15"])
print(player)
player.index = [10, 11, 18, 20, 21]
print(player.loc[10])
print(player.iloc[0])

# DataFrame
student = pd.DataFrame({
    "age": [18, 20, 19],
    "height": [169, 175, 181],
    "weight": [58, 66, 73]
}, index=[1, 2, 3])
print("\n学生数据：\n", student)
print(student.index)
print(student.columns)
print(student.values)
print(student.loc[2, "height"])
print(student.loc[[1, 3], ["height", "weight"]])
print(student.iloc[[0, 2], [0, 1]])
print(student[["height", "weight"]])
print(student.iloc[1:3, 0:2])
condition = student["height"] > 170
print(student.loc[condition, ["height", "weight"]])

student["expense"] = [1300, 1500, 1700]
print(student)
student["expense"] = 1100
student.loc[2] = [21, 176, 67, 300]
print(student)
student.loc[student["expense"] < 500, "expense"] = 1300
print(student)
print(student.drop(index=1))
print(student.drop(columns="expense"))
student = student.drop(columns=["age", "weight"])
print(student)
