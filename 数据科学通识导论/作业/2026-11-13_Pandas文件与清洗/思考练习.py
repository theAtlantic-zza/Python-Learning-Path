#Produce by zza
import numpy as np
import pandas as pd


data_folder = "/Users/zhaoziang/PycharmProjects/Python-Learning-Path/数据科学通识导论/inputs/课程资料/"
output_folder = "/Users/zhaoziang/PycharmProjects/Python-Learning-Path/数据科学通识导论/作业/2026-11-13_Pandas文件与清洗/outputs/"

numbers = np.random.randint(10, 100, (50, 7))
random_data = pd.DataFrame(numbers, columns=["a", "b", "c", "d", "e", "f", "g"])
random_data.to_csv(output_folder + "随机数据.csv", index=False)
print("第43页：随机表格\n", random_data)
print()


names = ["flymiles", "videogame", "icecream", "type"]
dating = pd.read_csv(data_folder + "datingTestSet.csv", skiprows=2,
                     header=None, names=names)
print("第43页：交友数据前五条记录\n", dating.head(5))
print()

large_doses = dating[dating["type"] == "largeDoses"]
print("largeDoses的全部记录：\n", large_doses.to_string())
print()

dating.loc[dating["videogame"] > 10, "videogame"] = 10
print("限制游戏时间后：\n", dating)
print()


stu = pd.read_excel(data_folder + "studentsInfo.xlsx", sheet_name="Group1",
                    index_col=0)
stu["案例教学"] = np.nan
stu = stu.dropna(thresh=len(stu.columns) - 2)
stu = stu.dropna(axis=1, how="all")
print("第54页：数据清洗\n", stu)
print()


stu["体重"] = stu["体重"].fillna(stu["体重"].mean())
stu["成绩"] = stu["成绩"].fillna(stu["成绩"].mean())
stu["年龄"] = stu["年龄"].ffill()
stu["月生活费"] = stu["月生活费"].fillna(stu["月生活费"].median())
print("第54页：数据填充\n", stu)
print()
