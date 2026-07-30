import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# =========================
# 1. 数据
# =========================
data = [
    # 月份, 流量场景, 日均消耗（元）, CTR（%）, CTCVR（‰）
    ["2026/01", "微信公众号与小程序", 638800.95, 2.34, 50.69],
    ["2026/02", "微信公众号与小程序", 282441.87, 2.24, 45.45],
    ["2026/03", "微信公众号与小程序", 628048.82, 2.02, 108.77],
    ["2026/04", "微信公众号与小程序", 1304635.03, 1.86, 81.74],
    ["2026/05", "微信公众号与小程序", 1443671.53, 2.10, 44.64],
    ["2026/06", "微信公众号与小程序", 1849446.18, 2.05, 42.02],

    ["2026/01", "微信视频号", 2603531.70, 1.39, 43.99],
    ["2026/02", "微信视频号", 1154167.68, 1.34, 35.26],
    ["2026/03", "微信视频号", 1831221.57, 1.20, 41.94],
    ["2026/04", "微信视频号", 1942636.52, 1.01, 56.76],
    ["2026/05", "微信视频号", 1985679.44, 0.96, 41.24],
    ["2026/06", "微信视频号", 2290320.00, 0.93, 33.75],

    ["2026/01", "微信朋友圈", 568998.98, 0.85, 12.23],
    ["2026/02", "微信朋友圈", 393852.58, 1.04, 6.80],
    ["2026/03", "微信朋友圈", 696924.89, 0.76, 13.50],
    ["2026/04", "微信朋友圈", 912055.04, 0.70, 18.55],
    ["2026/05", "微信朋友圈", 900886.92, 0.74, 17.08],
    ["2026/06", "微信朋友圈", 982570.21, 0.89, 13.84],
]

df = pd.DataFrame(
    data,
    columns=["月份", "流量场景", "日均消耗_元", "CTR_pct", "CTCVR_permille"]
)

month_order = [
    "2026/01", "2026/02",
    "2026/03", "2026/04", "2026/05", "2026/06"
]

scene_order = [
    "微信公众号与小程序",
    "微信视频号",
    "微信朋友圈"
]

df["月份"] = pd.Categorical(
    df["月份"],
    categories=month_order,
    ordered=True
)

df["日均消耗_万元"] = df["日均消耗_元"] / 10000
df = df.sort_values(["流量场景", "月份"])


# =========================
# 2. 字体与颜色
# =========================

# 不指定字体粗细，避免：
# findfont: Failed to find font weight bold
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "Noto Sans CJK SC",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans"
]
plt.rcParams["axes.unicode_minus"] = False

# 高对比度、色盲友好配色
colors = {
    "微信公众号与小程序": "#0072B2",  # 深蓝
    "微信视频号": "#D55E00",          # 橙红
    "微信朋友圈": "#009E73"           # 深绿
}


# =========================
# 3. 创建画布
# =========================
fig, axes = plt.subplots(
    nrows=3,
    ncols=1,
    figsize=(17, 12),
    sharex=True
)

chart_config = [
    {
        "column": "日均消耗_万元",
        "title": "日均消耗变化",
        "ylabel": "日均消耗（万元/日）",
        "formatter": FuncFormatter(lambda x, _: f"{x:,.0f}"),
        "label_fmt": lambda v: f"{v:,.0f}"
    },
    {
        "column": "CTR_pct",
        "title": "模型 CTR 变化",
        "ylabel": "CTR（%）",
        "formatter": FuncFormatter(lambda x, _: f"{x:.1f}%"),
        "label_fmt": lambda v: f"{v:.2f}%"
    },
    {
        "column": "CTCVR_permille",
        "title": "CTCVR 变化",
        "ylabel": "CTCVR（‰）",
        "formatter": FuncFormatter(lambda x, _: f"{x:.0f}‰"),
        "label_fmt": lambda v: f"{v:.1f}‰"
    }
]

x = range(len(month_order))


# =========================
# 4. 绘制三联折线图
# =========================
for ax, config in zip(axes, chart_config):

    for idx, scene in enumerate(scene_order):
        scene_df = (
            df[df["流量场景"] == scene]
            .set_index("月份")
            .reindex(month_order)
        )

        ax.plot(
            x,
            scene_df[config["column"]],
            label=scene,
            color=colors[scene],
            linewidth=3.2,
            marker="o",
            markersize=8,
            markerfacecolor=colors[scene],
            markeredgecolor="white",
            markeredgewidth=1.5,
            zorder=3
        )

        # 3条线轮流上/下错位
        offset_y = 11 if idx % 2 == 0 else -13
        va = "bottom" if offset_y > 0 else "top"
        # 数据标签
        for xi, yi in zip(x, scene_df[config["column"]]):
            if pd.isna(yi):
                continue
            ax.annotate(
                config["label_fmt"](yi),
                xy=(xi, yi),
                xytext=(0, offset_y),
                textcoords="offset points",
                ha="center",
                va=va,
                fontsize=8,
                color=colors[scene],
                bbox=dict(
                    boxstyle="round,pad=0.12",
                    fc="white",
                    ec="none",
                    alpha=0.85
                ),
                zorder=4
            )

        # 数据标签
        for xi, yi in zip(x, scene_df[config["column"]]):
            if pd.isna(yi):
                continue
            ax.annotate(
                config["label_fmt"](yi),
                xy=(xi, yi),
                xytext=(0, 10),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8.5,
                color=colors[scene],
                bbox=dict(
                    boxstyle="round,pad=0.15",
                    fc="white",
                    ec="none",
                    alpha=0.85
                ),
                zorder=4
            )

    ax.set_title(
        config["title"],
        loc="left",
        fontsize=18,
        pad=13
    )

    ax.set_ylabel(
        config["ylabel"],
        fontsize=15,
        labelpad=12
    )

    ax.yaxis.set_major_formatter(config["formatter"])

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=1,
        color="#B8B8B8",
        alpha=0.45
    )

    ax.set_axisbelow(True)
    ax.margins(x=0.03, y=0.15)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#A6A6A6")
    ax.spines["bottom"].set_color("#A6A6A6")

    ax.tick_params(
        axis="y",
        labelsize=13,
        colors="#333333"
    )


# =========================
# 5. 横轴、标题和图例
# =========================
axes[-1].set_xticks(list(x))
axes[-1].set_xticklabels(
    month_order,
    fontsize=14
)

axes[-1].set_xlabel(
    "月份",
    fontsize=15,
    labelpad=12
)

fig.suptitle(
    "by月看不同流量场景日均消耗与双率变化",
    fontsize=27,
    y=0.985
)

handles, labels = axes[0].get_legend_handles_labels()

fig.legend(
    handles,
    labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.94),
    ncol=3,
    frameon=False,
    fontsize=16,
    handlelength=3.5,
    handletextpad=0.8,
    columnspacing=2.8
)

fig.subplots_adjust(
    top=0.86,
    bottom=0.08,
    left=0.10,
    right=0.97,
    hspace=0.30
)


# =========================
# 6. 保存与展示
# =========================
output_path = "by月看不同流量场景日均消耗与双率变化.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"图片已保存：{output_path}")
