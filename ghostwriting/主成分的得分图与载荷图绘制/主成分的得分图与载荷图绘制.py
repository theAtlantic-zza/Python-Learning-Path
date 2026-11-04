from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


folder = Path(__file__).resolve().parent
excel_file = folder.parent / "inputs" / "作业(1).xlsx"
data = pd.read_excel(excel_file, sheet_name="原始数据", index_col=0)
group_data = pd.read_excel(excel_file, sheet_name="得分-LDA", index_col=0)
groups = group_data.loc[data.index, "类别"].to_numpy()
variable_x = data.columns.to_numpy(dtype=float)
values = data.to_numpy(dtype=float)

# 数据预处理：每列减去该列均值，进行均值中心化，保持原始尺度，不做方差标准化。
centered_data = values - values.mean(axis=0)
cov_matrix = np.cov(centered_data, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
loadings = eigenvectors[:, order]
scores = centered_data @ loadings[:, :2]
ratio = eigenvalues[:2] / eigenvalues.sum() * 100

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["PingFang SC", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
output_folder = folder / "outputs"
output_folder.mkdir(exist_ok=True)

fig1, ax1 = plt.subplots()
for group, color, marker in zip([1, 2, 3], ["k", "r", "b"], ["s", "o", "^"]):
    selected = groups == group
    ax1.scatter(scores[selected, 0], scores[selected, 1],
                color=color, marker=marker, label=f"类别{group}")

ax1.axhline(0, color="gray", linestyle="--")
ax1.axvline(0, color="gray", linestyle="--")
ax1.set_xlabel(f"PC1 ({ratio[0]:.2f}%)")
ax1.set_ylabel(f"PC2 ({ratio[1]:.2f}%)")
ax1.set_title("主成分1和主成分2得分图")
ax1.legend()
fig1.tight_layout()
fig1.savefig(output_folder / "主成分得分图.png", dpi=300, bbox_inches="tight")

fig2, ax2 = plt.subplots()
ax2.plot(variable_x, loadings[:, 1])
ax2.axhline(0, color="gray", linestyle="--")
ax2.set_xlabel("变量坐标")
ax2.set_ylabel("PC2载荷系数")
ax2.set_title(f"主成分2载荷图（贡献率 {ratio[1]:.2f}%）")
fig2.tight_layout()
fig2.savefig(output_folder / "主成分2载荷图.png", dpi=300, bbox_inches="tight")
plt.show()
