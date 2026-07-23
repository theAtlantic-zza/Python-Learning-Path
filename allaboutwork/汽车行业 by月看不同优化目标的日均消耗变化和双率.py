import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MultipleLocator

# =========================
# 1. 数据
# =========================
data = [
    # 月份, 优化目标, 日均消耗（元）, CTR（%）, CTCVR（‰）

    # 405 表单预约
    ["2025/11", "405", 202877.91, 1.63, 4.42],
    ["2025/12", "405", 410997.92, 1.78, 7.85],
    ["2026/01", "405", 305432.59, 1.67, 2.73],
    ["2026/02", "405", 213545.30, 1.27, 1.12],
    ["2026/03", "405", 312354.39, 1.39, 1.38],
    ["2026/04", "405", 315263.50, 1.47, 1.57],
    ["2026/05", "405", 260696.85, 1.52, 1.41],
    ["2026/06", "405", 350410.54, 1.36, 1.32],

    # 0 异常数据
    ["2025/11", "0", 234478.53, 0.50, np.nan],
    ["2025/12", "0", 111506.81, 0.52, np.nan],
    ["2026/01", "0", 94923.30, 0.64, np.nan],
    ["2026/02", "0", 33441.78, 0.66, np.nan],
    ["2026/03", "0", 194312.89, 0.47, np.nan],
    ["2026/04", "0", 402027.24, 0.51, np.nan],
    ["2026/05", "0", 242655.90, 0.42, np.nan],
    ["2026/06", "0", 169520.37, 0.46, np.nan],

    # 301 关键页面访问
    ["2025/11", "301", 223009.81, 0.96, 89.53],
    ["2025/12", "301", 119329.45, 1.06, 101.05],
    ["2026/01", "301", 88233.02, 1.08, 101.72],
    ["2026/02", "301", 43668.95, 1.20, 115.27],
    ["2026/03", "301", 103673.15, 1.42, 135.74],
    ["2026/04", "301", 218982.53, 1.02, 93.27],
    ["2026/05", "301", 153398.16, 1.03, 93.99],
    ["2026/06", "301", 112135.59, 1.34, 124.11],

    # 7 点击
    ["2025/11", "7", 169235.11, 1.20, np.nan],
    ["2025/12", "7", 61059.50, 0.68, np.nan],
    ["2026/01", "7", 40499.77, 1.64, np.nan],
    ["2026/02", "7", 13698.99, 1.36, np.nan],
    ["2026/03", "7", 107353.09, 1.00, np.nan],
    ["2026/04", "7", 214300.20, 1.02, np.nan],
    ["2026/05", "7", 83980.55, 0.82, np.nan],
    ["2026/06", "7", 72986.09, 0.78, np.nan],
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
    "2025/11", "2025/12", "2026/01", "2026/02",
    "2026/03", "2026/04", "2026/05", "2026/06"
]

target_order = ["405", "0", "301", "7"]

target_labels = {
    "405": "405 表单预约",
    "0": "0 异常数据",
    "301": "301 关键页面访问",
    "7": "7 点击"
}


# =========================
# 2. 数据处理
# =========================

# 检查重复月份
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

# 补齐所有“优化目标×月份”组合
full_index = pd.MultiIndex.from_product(
    [target_order, month_order],
    names=["优化目标", "月份"]
)

df = (
    df.set_index(["优化目标", "月份"])
    .reindex(full_index)
    .reset_index()
)

# 数值化
numeric_columns = [
    "日均消耗_元",
    "CTR_pct",
    "CTCVR_permille"
]

df[numeric_columns] = df[numeric_columns].apply(
    pd.to_numeric,
    errors="coerce"
)

# 检查日均消耗与CTR是否缺失
core_missing = df[
    df[["日均消耗_元", "CTR_pct"]].isna().any(axis=1)
]

if not core_missing.empty:
    raise ValueError(
        "日均消耗或CTR存在缺失：\n"
        + core_missing[
            ["月份", "优化目标"]
        ].to_string(index=False)
    )

# 元转万元
df["日均消耗_万元"] = df["日均消耗_元"] / 10000

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


# =========================
# 3. 字体和样式
# =========================
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "Noto Sans CJK SC",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans"
]
plt.rcParams["axes.unicode_minus"] = False

colors = {
    "405": "#0072B2",  # 蓝色
    "0": "#E31A1C",    # 醒目红色
    "301": "#009E73",  # 绿色
    "7": "#E69F00"     # 橙色
}

line_styles = {
    "405": "-",
    "0": "--",
    "301": "-",
    "7": "-"
}

markers = {
    "405": "o",
    "0": "D",
    "301": "s",
    "7": "^"
}

line_widths = {
    "405": 2.8,
    "0": 3.8,
    "301": 2.8,
    "7": 2.8
}

x = list(range(len(month_order)))


# =========================
# 4. 创建画布
# =========================
fig = plt.figure(figsize=(18, 15))

outer_grid = fig.add_gridspec(
    nrows=3,
    ncols=1,
    height_ratios=[1.45, 1.45, 2.1],
    hspace=0.34
)

ax_spend = fig.add_subplot(outer_grid[0])

ax_ctr = fig.add_subplot(
    outer_grid[1],
    sharex=ax_spend
)

# CTCVR使用断轴
ctcvr_grid = outer_grid[2].subgridspec(
    nrows=2,
    ncols=1,
    height_ratios=[1.2, 1],
    hspace=0.05
)

ax_ctcvr_high = fig.add_subplot(
    ctcvr_grid[0],
    sharex=ax_spend
)

ax_ctcvr_low = fig.add_subplot(
    ctcvr_grid[1],
    sharex=ax_spend
)


# =========================
# 5. 绘图函数
# =========================
def draw_lines(ax, column, targets):
    for target in targets:
        target_df = (
            df[df["优化目标"] == target]
            .set_index("月份")
            .reindex(month_order)
        )

        values = target_df[column]

        # 整条序列为空时不绘制
        if values.notna().sum() == 0:
            continue

        ax.plot(
            x,
            values,
            color=colors[target],
            linestyle=line_styles[target],
            linewidth=line_widths[target],
            marker=markers[target],
            markersize=9 if target == "0" else 8,
            markerfacecolor=colors[target],
            markeredgecolor="white",
            markeredgewidth=1.3,
            zorder=5 if target == "0" else 3
        )


def style_axis(ax):
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=1,
        color="#B8B8B8",
        alpha=0.45
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


# =========================
# 6. 日均消耗
# =========================
draw_lines(
    ax_spend,
    "日均消耗_万元",
    target_order
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

# 坐标轴从0开始
ax_spend.set_ylim(0, 45)

ax_spend.yaxis.set_major_locator(
    MultipleLocator(5)
)

ax_spend.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:,.0f}"
    )
)

ax_spend.tick_params(
    axis="x",
    labelbottom=False
)


# =========================
# 7. CTR
# =========================
draw_lines(
    ax_ctr,
    "CTR_pct",
    target_order
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

ax_ctr.set_ylim(0, 2.0)

ax_ctr.yaxis.set_major_locator(
    MultipleLocator(0.25)
)

ax_ctr.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.2f}%"
    )
)

ax_ctr.tick_params(
    axis="x",
    labelbottom=False
)


# =========================
# 8. CTCVR
# =========================
# 0和7的CTCVR均为缺失值，因此只绘制405和301
ctcvr_targets = ["405", "301"]

draw_lines(
    ax_ctcvr_high,
    "CTCVR_permille",
    ctcvr_targets
)

draw_lines(
    ax_ctcvr_low,
    "CTCVR_permille",
    ctcvr_targets
)

style_axis(ax_ctcvr_high)
style_axis(ax_ctcvr_low)

ax_ctcvr_high.set_title(
    "CTCVR 变化趋势（断轴展示）",
    loc="left",
    fontsize=19,
    pad=14
)

ax_ctcvr_high.set_ylabel(
    "CTCVR（‰）",
    fontsize=15,
    labelpad=12
)

# 上半部分展示301
ax_ctcvr_high.set_ylim(80, 145)
ax_ctcvr_high.set_yticks(
    [80, 100, 120, 140]
)

# 下半部分展示405，并从0开始
ax_ctcvr_low.set_ylim(0, 10)
ax_ctcvr_low.set_yticks(
    [0, 2, 4, 6, 8, 10]
)

ctcvr_formatter = FuncFormatter(
    lambda value, _: f"{value:.0f}‰"
)

ax_ctcvr_high.yaxis.set_major_formatter(
    ctcvr_formatter
)

ax_ctcvr_low.yaxis.set_major_formatter(
    ctcvr_formatter
)

# 隐藏断轴处边框
ax_ctcvr_high.spines["bottom"].set_visible(False)
ax_ctcvr_low.spines["top"].set_visible(False)

ax_ctcvr_high.tick_params(
    axis="x",
    bottom=False,
    labelbottom=False
)


# =========================
# 9. 绘制断轴符号
# =========================
break_size = 0.012

break_kwargs = {
    "color": "#666666",
    "clip_on": False,
    "linewidth": 1.5
}

ax_ctcvr_high.plot(
    (-break_size, break_size),
    (-break_size, break_size),
    transform=ax_ctcvr_high.transAxes,
    **break_kwargs
)

ax_ctcvr_high.plot(
    (1 - break_size, 1 + break_size),
    (-break_size, break_size),
    transform=ax_ctcvr_high.transAxes,
    **break_kwargs
)

ax_ctcvr_low.plot(
    (-break_size, break_size),
    (1 - break_size, 1 + break_size),
    transform=ax_ctcvr_low.transAxes,
    **break_kwargs
)

ax_ctcvr_low.plot(
    (1 - break_size, 1 + break_size),
    (1 - break_size, 1 + break_size),
    transform=ax_ctcvr_low.transAxes,
    **break_kwargs
)

ax_ctcvr_low.text(
    0.99,
    0.88,
    "0和7的CTCVR为缺失值",
    transform=ax_ctcvr_low.transAxes,
    ha="right",
    va="top",
    fontsize=12,
    color="#777777"
)


# =========================
# 10. 横轴
# =========================
ax_ctcvr_low.set_xticks(x)

ax_ctcvr_low.set_xticklabels(
    month_order,
    fontsize=14
)

ax_ctcvr_low.set_xlabel(
    "月份",
    fontsize=15,
    labelpad=12
)


# =========================
# 11. 标题和图例
# =========================
fig.suptitle(
    "汽车行业 by月看不同优化目标的日均消耗和双率变化趋势",
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
            linestyle=line_styles[target],
            linewidth=line_widths[target],
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
    ncol=4,
    frameon=False,
    fontsize=16,
    handlelength=3.2,
    handletextpad=0.8,
    columnspacing=2.4
)

fig.subplots_adjust(
    top=0.87,
    bottom=0.07,
    left=0.10,
    right=0.97
)


# =========================
# 12. 保存与展示
# =========================
output_path = "汽车行业_by月看不同优化目标的日均消耗与双率变化.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"图片已保存：{output_path}")
