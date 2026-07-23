import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MultipleLocator

# ==================================================
# 1. 数据
# ==================================================
data = [
    # 月份, 优化目标, 日均消耗（元）, CTR（%）, CTCVR（‰）

    # 412 加企微微信客服
    ["2025/11", "412", 144694.55, 1.08, 4.25],
    ["2025/12", "412", 97067.18, 0.98, 5.03],
    ["2026/01", "412", 75084.66, 1.07, 4.99],
    ["2026/02", "412", 130381.28, 1.89, 9.70],
    ["2026/03", "412", 162583.40, 2.13, 10.01],
    ["2026/04", "412", 51369.75, 2.31, 12.10],
    ["2026/05", "412", 29224.51, 2.66, 12.15],
    ["2026/06", "412", 10722.56, 2.76, 3.90],

    # 405 表单预约
    ["2025/11", "405", 6408.48, 2.42, 4.66],
    ["2025/12", "405", 8928.34, 1.91, 3.08],
    ["2026/01", "405", 9054.62, 1.32, 4.79],
    ["2026/02", "405", 5709.03, 0.96, 1.12],
    ["2026/03", "405", 17313.36, 1.03, 2.11],
    ["2026/04", "405", 16594.67, 1.10, 4.63],
    ["2026/05", "405", 14093.81, 0.97, 4.31],
    ["2026/06", "405", 8267.96, 1.32, 2.54],

    # 204 下单
    ["2025/11", "204", 127090.30, 2.53, 4.66],
    ["2025/12", "204", 36348.41, 1.85, 5.63],
    ["2026/01", "204", 12990.18, 1.36, 7.07],
    ["2026/02", "204", 13158.40, 2.47, 5.71],
    ["2026/03", "204", 60566.32, 2.08, 6.64],
    ["2026/04", "204", 110763.02, 2.16, 5.49],
    ["2026/05", "204", 152600.44, 2.27, 5.15],
    ["2026/06", "204", 157014.14, 1.90, 5.71],
]

df = pd.DataFrame(
    data,
    columns=[
        "月份",
        "优化目标",
        "日均消耗_元",
        "CTR_pct",
        "CTCVR_permille"
    ]
)

month_order = [
    "2025/11",
    "2025/12",
    "2026/01",
    "2026/02",
    "2026/03",
    "2026/04",
    "2026/05",
    "2026/06"
]

target_order = ["412", "405", "204"]

target_labels = {
    "412": "412 加企微微信客服",
    "405": "405 表单预约",
    "204": "204 下单"
}


# ==================================================
# 2. 数据清洗
# ==================================================
duplicate_rows = df.duplicated(
    subset=["月份", "优化目标"],
    keep=False
)

if duplicate_rows.any():
    raise ValueError(
        "存在重复的月份和优化目标组合：\n"
        + df.loc[
            duplicate_rows,
            ["月份", "优化目标"]
        ].to_string(index=False)
    )

full_index = pd.MultiIndex.from_product(
    [target_order, month_order],
    names=["优化目标", "月份"]
)

df = (
    df.set_index(["优化目标", "月份"])
    .reindex(full_index)
    .reset_index()
)

numeric_columns = [
    "日均消耗_元",
    "CTR_pct",
    "CTCVR_permille"
]

df[numeric_columns] = df[numeric_columns].apply(
    pd.to_numeric,
    errors="coerce"
)

missing_rows = df[
    df[numeric_columns].isna().any(axis=1)
]

if not missing_rows.empty:
    raise ValueError(
        "存在缺失数据：\n"
        + missing_rows[
            ["月份", "优化目标"]
        ].to_string(index=False)
    )

df["日均消耗_万元"] = (
    df["日均消耗_元"] / 10000
)

df["月份"] = pd.Categorical(
    df["月份"],
    categories=month_order,
    ordered=True
)

df["优化目标"] = pd.Categorical(
    df["优化目标"],
    categories=target_order,
    ordered=True
)

df = df.sort_values(
    ["优化目标", "月份"]
).reset_index(drop=True)


# ==================================================
# 3. 字体和配色
# ==================================================
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "Noto Sans CJK SC",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans"
]

plt.rcParams["axes.unicode_minus"] = False

colors = {
    "412": "#0072B2",
    "405": "#D55E00",
    "204": "#009E73"
}

markers = {
    "412": "o",
    "405": "^",
    "204": "s"
}

x = list(range(len(month_order)))


# ==================================================
# 4. 创建画布
# ==================================================
fig, axes = plt.subplots(
    nrows=3,
    ncols=1,
    figsize=(18, 14),
    sharex=True,
    facecolor="white"
)

ax_spend, ax_ctr, ax_ctcvr = axes


# ==================================================
# 5. 通用绘图函数
# ==================================================
def draw_lines(ax, column):
    for target in target_order:
        target_df = (
            df[df["优化目标"] == target]
            .set_index("月份")
            .reindex(month_order)
        )

        ax.plot(
            x,
            target_df[column],
            color=colors[target],
            linewidth=3.0,
            linestyle="-",
            marker=markers[target],
            markersize=8,
            markerfacecolor=colors[target],
            markeredgecolor="white",
            markeredgewidth=1.3,
            zorder=3
        )


def style_axis(ax):
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.9,
        color="#B8B8B8",
        alpha=0.40
    )

    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#A6A6A6")
    ax.spines["bottom"].set_color("#A6A6A6")

    ax.tick_params(
        axis="both",
        labelsize=13,
        colors="#333333"
    )

    ax.set_xlim(
        -0.25,
        len(month_order) - 0.75
    )


# ==================================================
# 6. 日均消耗变化趋势
# ==================================================
draw_lines(
    ax_spend,
    "日均消耗_万元"
)

style_axis(ax_spend)

ax_spend.set_title(
    "日均消耗变化趋势",
    loc="left",
    fontsize=19,
    pad=14
)

ax_spend.set_ylabel(
    "日均消耗（万元/日）",
    fontsize=15,
    labelpad=12
)

ax_spend.set_ylim(
    0,
    18
)

ax_spend.yaxis.set_major_locator(
    MultipleLocator(2)
)

ax_spend.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.0f}"
    )
)

ax_spend.tick_params(
    axis="x",
    labelbottom=False
)


# ==================================================
# 7. CTR变化趋势
# ==================================================
draw_lines(
    ax_ctr,
    "CTR_pct"
)

style_axis(ax_ctr)

ax_ctr.set_title(
    "模型 CTR 变化趋势",
    loc="left",
    fontsize=19,
    pad=14
)

ax_ctr.set_ylabel(
    "CTR（%）",
    fontsize=15,
    labelpad=12
)

ax_ctr.set_ylim(
    0.80,
    2.90
)

ax_ctr.yaxis.set_major_locator(
    MultipleLocator(0.20)
)

# 显示为1.4%，不显示为1.40%
ax_ctr.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.1f}%"
    )
)

ax_ctr.tick_params(
    axis="x",
    labelbottom=False
)


# ==================================================
# 8. CTCVR变化趋势
# ==================================================
draw_lines(
    ax_ctcvr,
    "CTCVR_permille"
)

style_axis(ax_ctcvr)

ax_ctcvr.set_title(
    "CTCVR 变化趋势",
    loc="left",
    fontsize=19,
    pad=14
)

ax_ctcvr.set_ylabel(
    "CTCVR（‰）",
    fontsize=15,
    labelpad=12
)

ax_ctcvr.set_ylim(
    0.50,
    12.80
)

ax_ctcvr.yaxis.set_major_locator(
    MultipleLocator(1)
)

ax_ctcvr.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.1f}‰"
    )
)


# ==================================================
# 9. 月份横轴
# ==================================================
ax_ctcvr.set_xticks(x)

ax_ctcvr.set_xticklabels(
    month_order,
    fontsize=14
)

ax_ctcvr.set_xlabel(
    "月份",
    fontsize=15,
    labelpad=12
)


# ==================================================
# 10. 主标题与图例
# ==================================================
fig.suptitle(
    "教育行业 by月看不同优化目标的日均消耗和双率变化趋势",
    fontsize=27,
    y=0.985
)

legend_handles = []

for target in target_order:
    legend_handles.append(
        Line2D(
            [0],
            [0],
            color=colors[target],
            linewidth=3.0,
            marker=markers[target],
            markersize=8,
            markerfacecolor=colors[target],
            markeredgecolor="white",
            label=target_labels[target]
        )
    )

fig.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.947),
    ncol=3,
    frameon=False,
    fontsize=16,
    handlelength=3.2,
    handletextpad=0.8,
    columnspacing=2.5
)

fig.subplots_adjust(
    top=0.87,
    bottom=0.07,
    left=0.09,
    right=0.97,
    hspace=0.46
)


# ==================================================
# 11. 保存与展示
# ==================================================
output_path = "教育行业_不同优化目标月度趋势.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"图片已保存：{output_path}")
