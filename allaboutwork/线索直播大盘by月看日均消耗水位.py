import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# =========================
# 1. 数据：按月份从早到晚排列
# =========================
data = {
    "月份": [
        "2026/01",
        "2026/02",
        "2026/03",
        "2026/04",
        "2026/05",
        "2026/06"
    ],
    "日均消耗_元": [
        3756869.79,
        1829964.88,
        3158926.24,
        4170378.40,
        4336980.10,
        5123561.56
    ]
}

df = pd.DataFrame(data)

# 将“元/日”换算成“万元/日”
df["日均消耗_万元"] = df["日均消耗_元"] / 10000

# =========================
# 2. 设置中文字体
# =========================
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "PingFang SC",
    "Heiti SC",
    "Arial Unicode MS"
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.weight"] = "normal"
plt.rcParams["axes.titleweight"] = "normal"

# =========================
# 3. 创建画布
# =========================
fig, ax = plt.subplots(figsize=(13, 6.5))

line_color = "#2F80ED"

# =========================
# 4. 绘制折线
# =========================
ax.plot(
    df["月份"],
    df["日均消耗_万元"],
    marker="o",
    markersize=8,
    linewidth=2.8,
    color=line_color,
    label="日均消耗"
)

# =========================
# 5. 添加数据标签
# =========================
for month, value in zip(df["月份"], df["日均消耗_万元"]):
    ax.annotate(
        f"{value:,.1f}",
        xy=(month, value),
        xytext=(0, 12),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=10,
        color=line_color,
        bbox=dict(
            boxstyle="round,pad=0.18",
            facecolor="white",
            edgecolor="none",
            alpha=0.85
        )
    )

# =========================
# 6. 标题与坐标轴
# =========================
ax.set_title(
    "线索直播大盘月度日均消耗趋势",
    fontsize=18,
    pad=24
)

ax.set_xlabel("月份", fontsize=12)
ax.set_ylabel("日均消耗（万元/日）", fontsize=12)

# Y轴显示一位小数
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda value, position: f"{value:,.1f}")
)

# 给顶部和底部留出空间
y_min = max(0, df["日均消耗_万元"].min() * 0.72)
y_max = df["日均消耗_万元"].max() * 1.18
ax.set_ylim(y_min, y_max)

ax.margins(x=0.06)

# =========================
# 7. 网格和图例
# =========================
ax.grid(
    axis="y",
    linestyle="--",
    linewidth=0.8,
    alpha=0.28
)

legend = ax.legend(
    loc="upper left",
    fontsize=11,
    frameon=True
)

legend.get_frame().set_facecolor("white")
legend.get_frame().set_edgecolor("#DDDDDD")
legend.get_frame().set_alpha(0.9)

# =========================
# 8. 美化边框
# =========================
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#BBBBBB")
ax.spines["bottom"].set_color("#BBBBBB")

ax.tick_params(axis="x", labelsize=10, length=0)
ax.tick_params(axis="y", labelsize=10, length=0)

# =========================
# 9. 调整布局
# =========================
plt.tight_layout()

# =========================
# 10. 先保存，再显示
# =========================
fig.savefig(
    "线索直播大盘月度日均消耗趋势.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
