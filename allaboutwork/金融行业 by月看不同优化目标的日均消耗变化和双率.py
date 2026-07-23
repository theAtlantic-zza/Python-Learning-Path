import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

# =========================
# 1. 更新后的数据
# =========================
data = [
    # 月份, 优化目标, 日均消耗（元）, CTR（%）, CTCVR（‰）
    ["2025/11", "加企微微信客服", 762225.32, 2.80, 10.05],
    ["2025/12", "加企微微信客服", 994360.73, 2.44, 7.93],
    ["2026/01", "加企微微信客服", 2320731.50, 2.38, 7.45],
    ["2026/02", "加企微微信客服", 969663.48, 2.53, 5.69],
    ["2026/03", "加企微微信客服", 1225048.62, 2.52, 5.32],
    ["2026/04", "加企微微信客服", 1603426.49, 2.38, 3.79],
    ["2026/05", "加企微微信客服", 2072005.51, 2.43, 3.79],
    ["2026/06", "加企微微信客服", 2790653.93, 2.35, 3.90],

    ["2025/11", "表单预约", 10909.57, 4.75, 1.67],
    ["2025/12", "表单预约", 11165.90, 4.65, 3.67],
    ["2026/01", "表单预约", 14660.42, 3.59, 2.34],
    ["2026/02", "表单预约", 19270.57, 2.07, 1.87],
    ["2026/03", "表单预约", 36579.45, 1.79, 2.02],
    ["2026/04", "表单预约", 63613.81, 1.57, 2.34],
    ["2026/05", "表单预约", 82122.21, 1.32, 1.91],
    ["2026/06", "表单预约", 124162.84, 1.19, 1.67],
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

target_order = [
    "加企微微信客服",
    "表单预约"
]

df["月份"] = pd.Categorical(
    df["月份"],
    categories=month_order,
    ordered=True
)

df["日均消耗_万元"] = df["日均消耗_元"] / 10000

df = df.sort_values(
    ["优化目标", "月份"]
)


# =========================
# 2. 字体与配色
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
    "加企微微信客服": "#0072B2",
    "表单预约": "#D55E00"
}

x = list(range(len(month_order)))


# =========================
# 3. 创建画布
# =========================
fig = plt.figure(figsize=(17, 14))

# 外层：日均消耗、CTR、CTCVR
outer_grid = fig.add_gridspec(
    nrows=3,
    ncols=1,
    height_ratios=[2.2, 1.55, 1.55],
    hspace=0.33
)

# 日均消耗内部再拆成上下两个坐标轴
spend_grid = outer_grid[0].subgridspec(
    nrows=2,
    ncols=1,
    height_ratios=[1.25, 1],
    hspace=0.05
)

ax_spend_high = fig.add_subplot(spend_grid[0])
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


# =========================
# 4. 通用折线绘制函数
# =========================
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
            label=target,
            color=colors[target],
            linewidth=3.2,
            marker="o",
            markersize=8,
            markerfacecolor=colors[target],
            markeredgecolor="white",
            markeredgewidth=1.5,
            zorder=3
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

    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#A6A6A6")
    ax.spines["bottom"].set_color("#A6A6A6")

    ax.tick_params(
        axis="both",
        labelsize=13,
        colors="#333333"
    )


# =========================
# 5. 日均消耗断轴图
# =========================
draw_lines(ax_spend_high, "日均消耗_万元")
draw_lines(ax_spend_low, "日均消耗_万元")

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

# 上轴展示加企微微信客服：约76～279万元
ax_spend_high.set_ylim(60, 300)
ax_spend_high.set_yticks(
    [75, 125, 175, 225, 275]
)

# 下轴放大表单预约：约1～12.4万元
# 明确从0开始，0会位于坐标轴最底部
ax_spend_low.set_ylim(0, 15)
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

# 隐藏断轴之间相邻的边框
ax_spend_high.spines["bottom"].set_visible(False)
ax_spend_low.spines["top"].set_visible(False)

ax_spend_high.tick_params(
    axis="x",
    which="both",
    bottom=False,
    labelbottom=False
)

ax_spend_low.tick_params(
    axis="x",
    labelbottom=False
)

# 绘制断轴符号
break_size = 0.012
break_kwargs = dict(
    color="#666666",
    clip_on=False,
    linewidth=1.5
)

ax_spend_high.plot(
    (-break_size, +break_size),
    (-break_size, +break_size),
    transform=ax_spend_high.transAxes,
    **break_kwargs
)

ax_spend_high.plot(
    (1 - break_size, 1 + break_size),
    (-break_size, +break_size),
    transform=ax_spend_high.transAxes,
    **break_kwargs
)

ax_spend_low.plot(
    (-break_size, +break_size),
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
    0.88,
    "断轴区间：15～60万元",
    transform=ax_spend_low.transAxes,
    ha="right",
    va="top",
    fontsize=11,
    color="#777777"
)


# =========================
# 6. CTR趋势
# =========================
draw_lines(ax_ctr, "CTR_pct")
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

# 强制从0开始
ax_ctr.set_ylim(bottom=0)
ax_ctr.yaxis.set_major_locator(
    MaxNLocator(nbins=6)
)
ax_ctr.yaxis.set_major_formatter(
    FuncFormatter(lambda value, _: f"{value:.1f}%")
)

ax_ctr.tick_params(
    axis="x",
    labelbottom=False
)


# =========================
# 7. CTCVR趋势
# =========================
draw_lines(ax_ctcvr, "CTCVR_permille")
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

# 强制从0开始
ax_ctcvr.set_ylim(bottom=0)
ax_ctcvr.yaxis.set_major_locator(
    MaxNLocator(nbins=6)
)
ax_ctcvr.yaxis.set_major_formatter(
    FuncFormatter(lambda value, _: f"{value:.1f}‰")
)


# =========================
# 8. 横轴
# =========================
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

for ax in [
    ax_spend_high,
    ax_spend_low,
    ax_ctr,
    ax_ctcvr
]:
    ax.set_xlim(-0.25, len(month_order) - 0.75)


# =========================
# 9. 主标题与图例
# =========================
fig.suptitle(
    "金融行业 by月看不同优化目标的日均消耗和双率变化趋势",
    fontsize=27,
    y=0.985
)

handles, labels = ax_spend_high.get_legend_handles_labels()

fig.legend(
    handles,
    labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.947),
    ncol=2,
    frameon=False,
    fontsize=17,
    handlelength=3.5,
    handletextpad=0.9,
    columnspacing=3.5
)

fig.subplots_adjust(
    top=0.87,
    bottom=0.07,
    left=0.10,
    right=0.97
)


# =========================
# 10. 保存与展示
# =========================
output_path = "金融行业_by月看不同优化目标的日均消耗和双率变化趋势.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"图片已保存：{output_path}")
