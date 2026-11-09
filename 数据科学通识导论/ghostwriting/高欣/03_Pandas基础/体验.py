from pandas import Series, DataFrame

# Series
player_height = Series([181, 188, 195, 183, 190],
                       index=["1", "4", "7", "10", "12"])
print(player_height)
print(player_height.index)
print(player_height.values)
print(player_height.loc["4"])
print(player_height.loc[["1", "12"]])
print(player_height.iloc[1:4])
print(player_height[player_height >= 188])

player_height.loc["1"] = 184
player_height.iloc[1:3] = 186
print(player_height)
player_height.loc["15"] = 193
print(player_height)
player_height.drop(index="10", inplace=True)
print(player_height)
player_height.index = [1, 4, 7, 12, 15]
print(player_height.loc[4])
print(player_height.iloc[1])

# DataFrame
student_info = DataFrame(
    [[19, 171, 61], [21, 179, 72], [20, 164, 54]],
    index=["A", "B", "C"], columns=["age", "height", "weight"]
)
print("\n学生信息：\n", student_info)
print(student_info.index)
print(student_info.columns)
print(student_info.values)
print(student_info.loc["B", "age"])
print(student_info.loc[["A", "C"], ["height", "weight"]])
print(student_info.iloc[[0, 2], [0, 1]])
print(student_info[["height", "weight"]])
print(student_info.iloc[1:, :2])
print(student_info.loc[student_info["height"] > 170, ["height", "weight"]])

student_info["expense"] = [1500, 1800, 1300]
print(student_info)
student_info["expense"] = 1300
student_info.loc["C"] = [20, 165, 55, 250]
print(student_info)
student_info.loc[student_info["expense"] < 500, "expense"] = 1500
print(student_info)
print(student_info.drop(index="A"))
print(student_info.drop(columns="expense"))
student_info = student_info.drop(["age", "weight"], axis=1)
print(student_info)
