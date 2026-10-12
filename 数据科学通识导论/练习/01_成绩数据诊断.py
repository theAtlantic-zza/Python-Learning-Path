"""第 1 讲：用课程课件的成绩表做 Python 与 NumPy 诊断。

数据来自《2-多维数据与计算》第 3 页。先独立完成任务，再运行本文件检查。
若暂时不会 NumPy，可以先完成前两题，并告诉老师卡在哪里。
"""

import numpy as np


NAMES = ["王微", "肖良英", "方绮雯", "刘旭阳", "钱易铭"]
SUBJECTS = ["Math", "English", "Python", "Chinese", "Art", "Database", "Physics"]
SCORES = [
    [70, 85, 77, 90, 82, 84, 89],
    [60, 64, 80, 75, 80, 92, 90],
    [90, 93, 88, 87, 86, 90, 91],
    [80, 82, 91, 88, 83, 86, 80],
    [88, 72, 78, 90, 91, 73, 80],
]


def subject_scores(subject: str) -> list[int]:
    """题 1：只用 Python 列表，按科目名称返回五位同学的成绩。"""
    # 例如 subject_scores("Python") 应返回 [77, 80, 88, 91, 78]。
    raise NotImplementedError("请完成题 1")


def top_student() -> str:
    """题 2：只用 Python 基础语法，返回七门课平均分最高的同学姓名。"""
    # 想想如何让每一行成绩与 NAMES 中的姓名对应。
    raise NotImplementedError("请完成题 2")


def numpy_subject_means() -> np.ndarray:
    """题 3：将 SCORES 转为二维 NumPy 数组，返回七门课各自的平均分。"""
    # 请在这里检查数组的 shape，并想清楚 mean 的 axis 应取 0 还是 1。
    raise NotImplementedError("请完成题 3")


if __name__ == "__main__":
    # 完成一题后，可先把其余题的检查行临时注释掉，再运行。
    print("题 1：", subject_scores("Python"))
    print("题 2：", top_student())
    print("题 3：", numpy_subject_means())
