import pandas as pd
import matplotlib.pyplot as plt

# 1. 准备数据：剔除 2026/07，因为 7 月不是完整月
data = {
    "时间": [
        "2025/11", "2025/12",
        "2026/01", "2026/02", "2026/03", "2026/04", "2026/05", "2026/06"
    ],
    "活跃广告主数": [
        6407, 4691,
        8096, 4581, 8933, 9061, 10985, 11189
    ],
    "有消耗主体数": [
        95, 92,
        94, 85, 94, 86, 101, 106
    ]
}

df = pd.DataFrame(data)

# 2. 设置中文字体
plt.rcParams["font.sans-serif"] = [
    "PingFang SC", "Heiti SC", "Arial Unicode MS", "SimHei", "Microsoft YaHei"
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.weight"] = "normal"
plt.rcParams["axes.titleweight"] = "normal"
plt.rcParams["axes.labelweight"] = "normal"

# 3. 配色
color_active = "#2F80ED"   # 蓝色：活跃广告主数
color_cost = "#F2994A"     # 橙色：有消耗主体数

# 4. 创建画布
fig, ax1 = plt.subplots(figsize=(13, 6.5))

# 5. 左轴：活跃广告主数
line1 = ax1.plot(
    df["时间"],
    df["活跃广告主数"],
    color=color_active,
    marker="o",
    markersize=7,
    linewidth=2.8,
    label="活跃广告主数"
)

ax1.set_ylabel("活跃广告主数", fontsize=12, color=color_active)
ax1.tick_params(axis="y", labelcolor=color_active, labelsize=10)
ax1.tick_params(axis="x", labelsize=10)
ax1.set_ylim(0, max(df["活跃广告主数"]) * 1.18)
ax1.margins(x=0.06)
ax1.grid(axis="y", linestyle="--", alpha=0.25)

# 6. 右轴：有消耗主体数
ax2 = ax1.twinx()

line2 = ax2.plot(
    df["时间"],
    df["有消耗主体数"],
    color=color_cost,
    marker="s",
    markersize=6.5,
    linewidth=2.8,
    linestyle="--",
    label="有消耗主体数"
)

ax2.set_ylabel("有消耗主体数", fontsize=12, color=color_cost)
ax2.tick_params(axis="y", labelcolor=color_cost, labelsize=10)
ax2.set_ylim(80, 110)

# 7. 标题
ax1.set_title(
    "2025/11–2026/06金融行业活跃广告主数与有消耗主体数变化",
    fontsize=17,
    pad=26
)

ax1.set_xlabel("时间", fontsize=12)

# 8. 图例
lines = line1 + line2
labels = [line.get_label() for line in lines]

legend = ax1.legend(
    lines,
    labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.02),
    ncol=2,
    fontsize=11,
    frameon=True
)

legend.get_frame().set_alpha(0.9)
legend.get_frame().set_edgecolor("#DDDDDD")
# 9. 为每个时间点单独设置标签偏移，避免重叠
# 格式：(x方向偏移, y方向偏移, 水平对齐方式)

active_offsets = {
    "2025/11": (0, 12, "center"),
    "2025/12": (-10, -18, "left"),   # 重点：蓝色标签向左上移动
    "2026/01": (0, 12, "center"),
    "2026/02": (0, 12, "center"),
    "2026/03": (0, 12, "center"),
    "2026/04": (0, 12, "center"),
    "2026/05": (0, 12, "center"),
    "2026/06": (8, -12, "right"),
}

cost_offsets = {
    "2025/11": (0, -16, "center"),
    "2025/12": (0, 20, "center"),    # 重点：橙色标签向右下移动
    "2026/01": (0, -16, "center"),
    "2026/02": (0, -18, "center"),
    "2026/03": (0, -16, "center"),
    "2026/04": (0, -18, "center"),
    "2026/05": (0, -16, "center"),
    "2026/06": (0, 12, "center"),
}

# 10. 添加蓝线标签
for x, y in zip(df["时间"], df["活跃广告主数"]):
    dx, dy, ha = active_offsets.get(x, (0, 12, "center"))
    ax1.annotate(
        f"{y:,}",
        xy=(x, y),
        xytext=(dx, dy),
        textcoords="offset points",
        ha=ha,
        va="center",
        fontsize=9.5,
        color=color_active,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8)
    )

# 11. 添加橙线标签
for x, y in zip(df["时间"], df["有消耗主体数"]):
    dx, dy, ha = cost_offsets.get(x, (0, -16, "center"))
    ax2.annotate(
        f"{y}",
        xy=(x, y),
        xytext=(dx, dy),
        textcoords="offset points",
        ha=ha,
        va="center",
        fontsize=9.5,
        color=color_cost,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8)
    )


# 12. 美化边框
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax1.spines["left"].set_color(color_active)
ax2.spines["right"].set_color(color_cost)

# 13. 布局
plt.tight_layout()

# 14. 保存（先保存再显示）
fig.savefig(
    "2025-11至2026-06金融行业活跃广告主数与有消耗主体数变化.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
