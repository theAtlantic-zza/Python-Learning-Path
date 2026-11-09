#Produce by zza
#体验
import pandas as pd

# Series
height = pd.Series([188, 191, 185, 179, 186], index=["13", "14", "7", "2", "9"])
print(height)
print(height.index)
print(height.values)
print(height["13"])
print(height[["14", "9"]])
print(height.iloc[1:4])
print(height[height > 185])

height["13"] = 190
height.iloc[1:3] = 180
print(height)

new_height = pd.concat([height, pd.Series([193, 187], index=["23", "5"])])
print(new_height)
print(new_height.drop(["13", "9"]))
height.index = [13, 14, 7, 2, 9]
print(height.loc[13])
print(height.iloc[0])

# DataFrame
students = pd.DataFrame(
    [[19, 172, 65], [20, 168, 60], [18, 178, 70]],
    index=[1, 2, 3],
    columns=["age", "height", "weight"]
)
print("\n学生信息：\n", students)
print(students.index)
print(students.columns)
print(students.values)

print(students.loc[1, "age"])
print(students.loc[[1, 3], ["height", "weight"]])

print(students.iloc[[0, 2], [0, 1]])
print(students[["height", "weight"]])

print(students.iloc[1:, :2])
print(students.loc[students["height"] >= 170, ["height", "weight"]])

students["expense"] = [1400, 1600, 1200]
print(students)
students["expense"] = 1000
students.loc[1, :] = [21, 180, 70, 200]
print(students)
students.loc[students["expense"] < 500, "expense"] = 1200
print(students)
print(students.drop(1, axis=0))
print(students.drop("expense", axis=1))
students.drop(["age", "weight"], axis=1, inplace=True)
print(students)
