import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MultipleLocator

# ==================================================
# 1. 数据
# ==================================================
data = [
    # 月份, 行业, 日均消耗（元）, CTR（%）, CTCVR（‰）

    # 金融
    ["2026/01", "金融", 2396794.32, 2.12, 12.05],
    ["2026/02", "金融", 1011806.63, 2.25, 10.64],
    ["2026/03", "金融", 1315699.84, 2.00, 12.11],
    ["2026/04", "金融", 1723248.96, 2.11, 8.61],
    ["2026/05", "金融", 2198184.72, 2.19, 8.31],
    ["2026/06", "金融", 2964195.81, 2.12, 7.40],

    # 汽车
    ["2026/01", "汽车", 579396.37, 1.22, 54.49],
    ["2026/02", "汽车", 321353.07, 1.20, 32.66],
    ["2026/03", "汽车", 786977.45, 1.06, 58.11],
    ["2026/04", "汽车", 1282799.11, 0.92, 90.55],
    ["2026/05", "汽车", 810266.32, 0.86, 77.21],
    ["2026/06", "汽车", 753457.85, 0.97, 63.04],

    # 教育
    ["2026/01", "教育", 102081.18, 0.97, 10.14],
    ["2026/02", "教育", 149340.25, 1.63, 9.35],
    ["2026/03", "教育", 246031.18, 1.63, 9.40],
    ["2026/04", "教育", 185221.88, 1.59, 9.62],
    ["2026/05", "教育", 206786.61, 1.77, 9.19],
    ["2026/06", "教育", 197484.39, 1.32, 17.15],

    # 房家
    ["2026/01", "房家", 502485.32, 1.37, 41.41],
    ["2026/02", "房家", 242530.51, 1.39, 52.08],
    ["2026/03", "房家", 687725.47, 1.37, 72.10],
    ["2026/04", "房家", 878002.89, 1.27, 26.01],
    ["2026/05", "房家", 928608.43, 1.21, 22.04],
    ["2026/06", "房家", 1022875.57, 1.16, 26.36],
]

df = pd.DataFrame(
    data,
    columns=[
        "月份",
        "行业",
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

industry_order = [
    "金融",
    "汽车",
    "教育",
    "房家"
]


# ==================================================
# 2. 数据检查与清洗
# ==================================================
duplicate_rows = df.duplicated(
    subset=["月份", "行业"],
    keep=False
)

if duplicate_rows.any():
    raise ValueError(
        "存在重复的月份和行业组合：\n"
        + df.loc[
            duplicate_rows,
            ["月份", "行业"]
        ].to_string(index=False)
    )

# 补齐“4个行业 × 8个月”的完整组合
full_index = pd.MultiIndex.from_product(
    [industry_order, month_order],
    names=["行业", "月份"]
)

df = (
    df.set_index(["行业", "月份"])
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
            ["月份", "行业"]
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

df["行业"] = pd.Categorical(
    df["行业"],
    categories=industry_order,
    ordered=True
)

df = df.sort_values(
    ["行业", "月份"]
).reset_index(drop=True)


# ==================================================
# 3. 字体与高对比度配色
# ==================================================
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
    "金融": "#0072B2",  # 深蓝
    "汽车": "#D55E00",  # 橙红
    "教育": "#009E73",  # 深绿
    "房家": "#7B61A8"   # 紫色
}

# 不仅依赖颜色，也使用不同标记增强可读性
markers = {
    "金融": "o",
    "汽车": "^",
    "教育": "s",
    "房家": "D"
}

x = list(range(len(month_order)))


# ==================================================
# 4. 通用绘图函数
# ==================================================
def draw_industry_lines(ax, column, label_fmt=None):
    for idx, industry in enumerate(industry_order):
        industry_df = (
            df[df["行业"] == industry]
            .set_index("月份")
            .reindex(month_order)
        )

        ax.plot(
            x,
            industry_df[column],
            color=colors[industry],
            linewidth=3.1,
            linestyle="-",
            marker=markers[industry],
            markersize=8,
            markerfacecolor=colors[industry],
            markeredgecolor="white",
            markeredgewidth=1.3,
            label=industry,
            zorder=3
        )

        if label_fmt is not None:
            # 4行业轮流上/下、左右错位，避免拥挤
            offset_table = [(0, 12, "bottom"), (0, -14, "top"),
                            (0, 12, "bottom"), (0, -14, "top")]
            dx, dy, va = offset_table[idx % 4]
            for xi, yi in zip(x, industry_df[column]):
                if pd.isna(yi):
                    continue
                ax.annotate(
                    label_fmt(yi),
                    xy=(xi, yi),
                    xytext=(dx, dy),
                    textcoords="offset points",
                    ha="center",
                    va=va,
                    fontsize=8,
                    color=colors[industry],
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
        alpha=0.42
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


def create_legend_handles():
    handles = []

    for industry in industry_order:
        handles.append(
            Line2D(
                [0],
                [0],
                color=colors[industry],
                linewidth=3.1,
                marker=markers[industry],
                markersize=8,
                markerfacecolor=colors[industry],
                markeredgecolor="white",
                label=industry
            )
        )

    return handles


legend_handles = create_legend_handles()


# ==================================================
# 5. 图一：日均消耗变化
# ==================================================
fig_spend, ax_spend = plt.subplots(
    figsize=(17, 9),
    facecolor="white"
)

draw_industry_lines(
    ax_spend,
    "日均消耗_万元",
    label_fmt=lambda v: f"{v:,.0f}"
)

style_axis(ax_spend)

ax_spend.set_title(
    "by月看四个重点行业的日均消耗变化趋势",
    fontsize=25,
    pad=70
)

ax_spend.set_ylabel(
    "日均消耗（万元/日）",
    fontsize=15,
    labelpad=12
)


ax_spend.set_xlabel(
    "月份",
    fontsize=15,
    labelpad=12
)

# 消耗类指标保留0基线
ax_spend.set_ylim(
    0,
    320
)

ax_spend.yaxis.set_major_locator(
    MultipleLocator(40)
)

ax_spend.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:,.0f}"
    )
)

ax_spend.set_xticks(x)

ax_spend.set_xticklabels(
    month_order,
    fontsize=14
)

fig_spend.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.895),
    ncol=4,
    frameon=False,
    fontsize=16,
    handlelength=3,
    handletextpad=0.8,
    columnspacing=2.8
)

fig_spend.subplots_adjust(
    top=0.78,
    bottom=0.13,
    left=0.09,
    right=0.97
)

spend_output = "四个重点行业_日均消耗变化.png"

fig_spend.savefig(
    spend_output,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)


# ==================================================
# 6. 图二：双率变化
# ==================================================
fig_rate, axes_rate = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(17, 12),
    sharex=True,
    facecolor="white"
)

ax_ctr, ax_ctcvr = axes_rate


# --------------------------------------------------
# 6.1 CTR变化
# --------------------------------------------------
draw_industry_lines(
    ax_ctr,
    "CTR_pct",
    label_fmt=lambda v: f"{v:.2f}%"
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

# 折线趋势图不强制从0开始
ax_ctr.set_ylim(
    0.75,
    2.55
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


# --------------------------------------------------
# 6.2 CTCVR变化
# --------------------------------------------------
draw_industry_lines(
    ax_ctcvr,
    "CTCVR_permille",
    label_fmt=lambda v: f"{v:.1f}‰"
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

ax_ctcvr.set_xlabel(
    "月份",
    fontsize=15,
    labelpad=12
)

# 保留完整量级，避免不同坐标造成误判
ax_ctcvr.set_ylim(
    0,
    100
)

ax_ctcvr.yaxis.set_major_locator(
    MultipleLocator(10)
)

ax_ctcvr.yaxis.set_major_formatter(
    FuncFormatter(
        lambda value, _: f"{value:.0f}‰"
    )
)

ax_ctcvr.set_xticks(x)

ax_ctcvr.set_xticklabels(
    month_order,
    fontsize=14
)

fig_rate.suptitle(
    "by月看四个重点行业的双率变化趋势",
    fontsize=25,
    y=0.985
)

fig_rate.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.945),
    ncol=4,
    frameon=False,
    fontsize=16,
    handlelength=3,
    handletextpad=0.8,
    columnspacing=2.8
)

fig_rate.subplots_adjust(
    top=0.86,
    bottom=0.09,
    left=0.09,
    right=0.97,
    hspace=0.38
)

rate_output = "by月看四个重点行业双率变化趋势.png"

fig_rate.savefig(
    rate_output,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)


# ==================================================
# 7. 展示和输出
# ==================================================
plt.show()

print(f"日均消耗图已保存：{spend_output}")
print(f"双率图已保存：{rate_output}")
