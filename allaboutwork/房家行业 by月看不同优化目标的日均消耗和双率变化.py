import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MultipleLocator

# ==================================================
# 1. 数据
# ==================================================
data = [
    # 月份, 优化目标, 日均消耗（元）, CTR（%）, CTCVR（‰）

    # 409 确认意向
    ["2026/01", "409", 7457.10, 1.49, 1.53],
    ["2026/02", "409", 6926.59, 1.13, 0.77],
    ["2026/03", "409", 3430.14, 1.70, 0.94],
    ["2026/04", "409", 22641.70, 1.19, 0.59],
    ["2026/05", "409", 64203.64, 1.13, 0.75],
    ["2026/06", "409", 69086.01, 1.15, 1.04],

    # 405 表单预约
    ["2026/01", "405", 414229.33, 1.16, 0.89],
    ["2026/02", "405", 201619.46, 1.13, 0.78],
    ["2026/03", "405", 548746.64, 1.32, 1.11],
    ["2026/04", "405", 717879.85, 1.25, 0.92],
    ["2026/05", "405", 735045.92, 1.04, 0.81],
    ["2026/06", "405", 799165.64, 0.94, 0.74],

    # 10000 综合线索收集
    ["2026/01", "10000", 58158.66, 1.01, 0.95],
    ["2026/02", "10000", 18444.83, 1.10, 0.97],
    ["2026/03", "10000", 63201.10, 1.07, 1.08],
    ["2026/04", "10000", 101628.42, 1.01, 0.86],
    ["2026/05", "10000", 96967.36, 0.95, 0.72],
    ["2026/06", "10000", 118994.71, 0.96, 0.84],
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
    "2026/01",
    "2026/02",
    "2026/03",
    "2026/04",
    "2026/05",
    "2026/06"
]

target_order = [
    "409",
    "405",
    "10000"
]

target_labels = {
    "409": "409 确认意向",
    "405": "405 表单预约",
    "10000": "10000 综合线索收集"
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

# 补齐“3个优化目标 × 6个月”
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

# 元转换为万元
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
# 3. 字体与颜色
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
    "409": "#009E73",
    "405": "#0072B2",
    "10000": "#D55E00"
}

markers = {
    "409": "s",
    "405": "o",
    "10000": "^"
}

x = list(range(len(month_order)))


# ==================================================
# 4. 创建画布
# ==================================================
fig = plt.figure(
    figsize=(18, 17),
    facecolor="white"
)

outer_grid = fig.add_gridspec(
    nrows=3,
    ncols=1,
    height_ratios=[2.0, 1.65, 1.65],
    hspace=0.46
)

# 日均消耗使用断轴
spend_grid = outer_grid[0].subgridspec(
    nrows=2,
    ncols=1,
    height_ratios=[1.2, 1],
    hspace=0.06
)

ax_spend_high = fig.add_subplot(
    spend_grid[0]
)

ax_spend_low = fig.add_subplot(
    spend_grid[1],
    sharex=ax_spend_high
)

ax_ctr = fig.add_subplot(
    outer_grid[1],
    sharex=ax_spend_low
)

ax_ctcvr = fig.add_subplot(
    outer_grid[2],
    sharex=ax_spend_low
)


# ==================================================
# 5. 通用函数
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


def add_labels(ax, column, label_fmt):
    y_min, y_max = ax.get_ylim()
    for idx, target in enumerate(target_order):
        target_df = (
            df[df["优化目标"] == target]
            .set_index("月份")
            .reindex(month_order)
        )
        # 3条线轮流上/下错位
        offset_y = 11 if idx % 2 == 0 else -13
        va = "bottom" if offset_y > 0 else "top"
        for xi, yi in zip(x, target_df[column]):
            if pd.isna(yi):
                continue
            if yi < y_min or yi > y_max:
                continue
            ax.annotate(
                label_fmt(yi),
                xy=(xi, yi),
                xytext=(0, offset_y),
                textcoords="offset points",
                ha="center",
                va=va,
                fontsize=8,
                color=colors[target],
                bbox=dict(
                    boxstyle="round,pad=0.12",
                    fc="white",
                    ec="none",
                    alpha=0.85
                ),
                zorder=4
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

    ax.spines["left"].set_color(
        "#A6A6A6"
    )

    ax.spines["bottom"].set_color(
        "#A6A6A6"
    )

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
    ax_spend_high,
    "日均消耗_万元"
)

draw_lines(
    ax_spend_low,
    "日均消耗_万元"
)

style_axis(ax_spend_high)
style_axis(ax_spend_low)

ax_spend_high.set_title(
    "日均消耗变化趋势（断轴展示）",
    loc="left",
    fontsize=19,
    pad=14
)

ax_spend_high.set_ylabel(
    "日均消耗（万元/日）",
    fontsize=15,
    labelpad=12
)

# 上方坐标轴展示405
ax_spend_high.set_ylim(
    18,
    85
)

ax_spend_high.set_yticks(
    [20, 35, 50, 65, 80]
)

# 下方坐标轴展示409和10000
ax_spend_low.set_ylim(
    0,
    15
)

ax_spend_low.set_yticks(
    [0, 3, 6, 9, 12, 15]
)

spend_formatter = FuncFormatter(
    lambda value, _: f"{value:,.0f}"
)

ax_spend_high.yaxis.set_major_formatter(
    spend_formatter
)

ax_spend_low.yaxis.set_major_formatter(
    spend_formatter
)

# 隐藏断轴连接位置的边框
ax_spend_high.spines["bottom"].set_visible(
    False
)

ax_spend_low.spines["top"].set_visible(
    False
)

ax_spend_high.tick_params(
    axis="x",
    bottom=False,
    labelbottom=False
)

ax_spend_low.tick_params(
    axis="x",
    labelbottom=False
)


# ==================================================
# 7. 日均消耗断轴符号
# ==================================================
break_size = 0.012

break_kwargs = {
    "color": "#666666",
    "clip_on": False,
    "linewidth": 1.5
}

ax_spend_high.plot(
    (-break_size, break_size),
    (-break_size, break_size),
    transform=ax_spend_high.transAxes,
    **break_kwargs
)

ax_spend_high.plot(
    (1 - break_size, 1 + break_size),
    (-break_size, break_size),
    transform=ax_spend_high.transAxes,
    **break_kwargs
)

ax_spend_low.plot(
    (-break_size, break_size),
    (1 - break_size, 1 + break_size),
    transform=ax_spend_low.transAxes,
    **break_kwargs
)

ax_spend_low.plot(
    (1 - break_size, 1 + break_size),
    (1 - break_size, 1 + break_size),
    transform=ax_spend_low.transAxes,
    **break_kwargs
)

ax_spend_low.text(
    0.99,
    0.87,
    "断轴区间：15～18万元",
    transform=ax_spend_low.transAxes,
    ha="right",
    va="top",
    fontsize=11,
    color="#777777"
)

# 断轴上下轴各自标注（值落在区间内才标）
spend_label_fmt = lambda v: f"{v:.1f}"
add_labels(ax_spend_high, "日均消耗_万元", spend_label_fmt)
add_labels(ax_spend_low, "日均消耗_万元", spend_label_fmt)

# 断轴上下轴各自标注（值落在区间内才标）
spend_label_fmt = lambda v: f"{v:.1f}"
add_labels(ax_spend_high, "日均消耗_万元", spend_label_fmt)
add_labels(ax_spend_low, "日均消耗_万元", spend_label_fmt)


# ==================================================
# 8. CTR变化趋势
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

# 不从0开始，放大有效波动
ax_ctr.set_ylim(
    0.80,
    1.80
)

# 更细的0.10%颗粒度
ax_ctr.yaxis.set_major_locator(
    MultipleLocator(0.10)
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

add_labels(ax_ctr, "CTR_pct", lambda v: f"{v:.2f}%")

add_labels(ax_ctr, "CTR_pct", lambda v: f"{v:.2f}%")


# ==================================================
# 9. CTCVR变化趋势
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

# 不从0开始，放大有效波动
ax_ctcvr.set_ylim(
    0.50,
    1.60
)

# 更细的0.10‰颗粒度
ax_ctcvr.yaxis.set_major_locator(
    MultipleLocator(0.10)
)

ax_ctcvr.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.2f}‰"
    )
)

add_labels(ax_ctcvr, "CTCVR_permille", lambda v: f"{v:.2f}‰")


# ==================================================
# 10. 月份横轴
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
# 11. 主标题和图例
# ==================================================
fig.suptitle(
    "房家行业 by月看不同优化目标的日均消耗和双率变化趋势",
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
    left=0.10,
    right=0.97
)


# ==================================================
# 12. 保存与展示
# ==================================================
output_path = "房家行业_不同优化目标月度趋势.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"图片已保存：{output_path}")
