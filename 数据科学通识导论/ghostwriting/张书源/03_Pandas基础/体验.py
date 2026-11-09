import pandas as pd

# Series
values = [180, 186, 192, 177, 188]
labels = ["3", "6", "8", "16", "22"]
height = pd.Series(values, index=labels)
print(height)
print(height.index)
print(height.values)
print(height["8"])
print(height[["3", "16"]])
print(height.iloc[[0, 2, 4]])
print(height.iloc[1:4])
print(height[height < 185])

height["3"] = 183
height.iloc[2:4] = 185
print(height)
extra = pd.Series([190, 181], index=["25", "30"])
all_height = pd.concat([height, extra])
print(all_height)
all_height = all_height.drop("16")
print(all_height)
height.index = [3, 6, 8, 16, 22]
print(height.loc[6])
print(height.iloc[1])

# DataFrame
info = [[20, 174, 64], [19, 166, 55], [21, 182, 76]]
students = pd.DataFrame(info, index=[101, 102, 103],
                        columns=["age", "height", "weight"])
print("\n学生表：\n", students)
print(students.index)
print(students.columns)
print(students.values)
print(students.loc[101, "weight"])
print(students.loc[[101, 103], ["height", "weight"]])
print(students.iloc[[0, 2], [0, 1]])
print(students.loc[:, ["height", "weight"]])
print(students.iloc[0:2, 1:3])
mask = students["height"] >= 174
print(students.loc[mask, ["height", "weight"]])

students["expense"] = [1200, 1400, 1600]
print(students)
students["expense"] = 1200
students.loc[101, :] = [20, 175, 65, 400]
print(students)
students.loc[students["expense"] < 600, "expense"] = 1400
print(students)
print(students.drop(102, axis=0))
print(students.drop("expense", axis=1))
students.drop(columns=["age", "weight"], inplace=True)
print(students)
