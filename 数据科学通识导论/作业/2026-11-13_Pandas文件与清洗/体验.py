#Produce by zza
import pandas as pd


data_folder = "/Users/zhaoziang/PycharmProjects/Python-Learning-Path/数据科学通识导论/inputs/课程资料/"
output_folder = "/Users/zhaoziang/PycharmProjects/Python-Learning-Path/数据科学通识导论/作业/2026-11-13_Pandas文件与清洗/outputs/"

student = pd.read_csv(data_folder + "student1.csv", index_col=None)
print("默认索引，最后三行：\n", student.tail(3))
print()

student = pd.read_csv(data_folder + "student1.csv", index_col=0)
print("序号作为索引，前三行：\n", student.head(3))
print()


columns = ["序号", "性别", "年龄", "身高", "体重", "省份", "成绩"]
student_txt = pd.read_csv(data_folder + "student2.txt", sep="\t",
                          header=None, names=columns, index_col=0)
print("TXT前两行：\n", student_txt.head(2))
print()


data = [[19, 68, 170], [20, 65, 165], [18, 65, 175]]
example = pd.DataFrame(data, index=[1, 2, 3], columns=["age", "weight", "height"])
example.to_csv(output_folder + "体验数据.csv", index=False)
print("保存的表格：\n", example)
print()


student_excel = pd.read_excel(data_folder + "student3.xlsx",
                              sheet_name="Group1", skiprows=3, index_col=0)
print("Excel前两行：\n", student_excel.head(2))
print()


stu = pd.read_excel(data_folder + "studentsInfo.xlsx", sheet_name="Group1",
                    index_col=0)
print("缺失值判断：\n", stu.isna())
print()

print("删除含缺失值的行：\n", stu.dropna())
print()

print("保留至少8项有效数据的行：\n", stu.dropna(thresh=8))
print()


filled = stu.fillna({"年龄": 20, "体重": stu["体重"].mean()})
print("填充年龄和体重：\n", filled)
print()

print("用上一行的数据填充：\n", stu.ffill())
print()

print("去除重复数据：\n", stu.drop_duplicates())
print()


scores = pd.Series(["71", "缺考", "90"])
print("转换为数值：\n", pd.to_numeric(scores, errors="coerce"))
print()
