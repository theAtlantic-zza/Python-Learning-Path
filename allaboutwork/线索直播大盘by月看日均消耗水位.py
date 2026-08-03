import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# =========================
# 1. 数据：按月份从早到晚排列
#    两类“日均数量”口径不同，请勿混用：
#    - 日均活跃广告主数：直接取月度报表的日均值
#    - 日均有消耗主体数：逐日去重主体数之和 ÷ 当月自然日数
#    注意：上半年累计去重主体数 6,570 不是日均值，
#    不能用 6,570 ÷ 181 计算日均活跃主体数
# =========================
data = {
    "月份": [
        "2026/01",
        "2026/02",
        "2026/03",
        "2026/04",
        "2026/05",
        "2026/06",
    ],
    "日均消耗_元": [
        3756869.79,
        1829964.88,
        3158926.24,
        4170378.40,
        4336980.10,
        5123561.56,
    ],
    "自然日数": [
        31,
        28,
        31,
        30,
        31,
        30,
    ],
    "每日去重主体数合计": [
        27548,
        13291,
        23965,
        23977,
        26641,
        29915,
    ],
    "日均活跃广告主数": [
        1415,
        817,
        1349,
        1487,
        1663,
        1856,
    ],
    "CPM_元": [
        43.78,
        29.64,
        26.41,
        26.94,
        31.70,
        37.93,
    ],
}

df = pd.DataFrame(data)

# 将“元/日”换算成“万元/日”
df["日均消耗_万元"] = df["日均消耗_元"] / 10000

# 由逐日截图计算真正的月度日均有消耗主体数
df["日均有消耗主体数"] = (
    df["每日去重主体数合计"] / df["自然日数"]
)


# =========================
# 2. 设置中文字体
# =========================
plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "PingFang SC",
    "Heiti SC",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.weight"] = "normal"
plt.rcParams["axes.titleweight"] = "normal"


# =========================
# 3. 单指标趋势图函数
# =========================
def create_trend_chart(
    x,
    y,
    title,
    legend_label,
    ylabel,
    color,
    label_format,
    axis_format,
    output_file,
):
    """绘制并保存一张独立的月度趋势图。"""
    fig, ax = plt.subplots(figsize=(13, 6.5))

    x_labels = np.asarray(x)
    x_positions = np.arange(len(x_labels))

    y = pd.to_numeric(y, errors="coerce")
    valid = y.notna()

    ax.plot(
        x_positions[valid],
        y[valid],
        marker="o",
        markersize=8,
        linewidth=2.8,
        color=color,
        label=legend_label,
    )

    # 添加数据标签
    for x_position, value in zip(
        x_positions[valid],
        y[valid],
    ):
        ax.annotate(
            label_format(value),
            xy=(x_position, value),
            xytext=(0, 12),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
            color=color,
            bbox=dict(
                boxstyle="round,pad=0.18",
                facecolor="white",
                edgecolor="none",
                alpha=0.88,
            ),
        )

    # 自动设置纵轴范围
    values = y[valid]
    value_min = values.min()
    value_max = values.max()
    value_range = value_max - value_min

    padding = (
        value_range * 0.30
        if value_range > 0
        else max(abs(value_max) * 0.15, 1)
    )

    ax.set_ylim(
        max(0, value_min - padding),
        value_max + padding,
    )

    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)
    ax.set_xlim(-0.3, len(x_labels) - 0.7)

    ax.set_title(
        title,
        fontsize=18,
        pad=24,
    )
    ax.set_xlabel("月份", fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

    ax.yaxis.set_major_formatter(
        FuncFormatter(axis_format)
    )

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=0.28,
    )

    legend = ax.legend(
        loc="upper left",
        fontsize=11,
        frameon=True,
    )
    legend.get_frame().set_facecolor("white")
    legend.get_frame().set_edgecolor("#DDDDDD")
    legend.get_frame().set_alpha(0.9)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#BBBBBB")
    ax.spines["bottom"].set_color("#BBBBBB")

    ax.tick_params(
        axis="x",
        labelsize=10,
        length=0,
    )
    ax.tick_params(
        axis="y",
        labelsize=10,
        length=0,
    )

    fig.tight_layout()

    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
        facecolor="white",
    )

    return fig


# =========================
# 4. 广告主数与主体数合并图函数
# =========================
def create_count_comparison_chart(
    x,
    advertiser_values,
    entity_values,
    output_file,
):
    """
    将日均活跃广告主数和日均有消耗主体数
    绘制在同一个坐标轴。
    """
    fig, ax = plt.subplots(figsize=(13, 6.5))

    x_labels = np.asarray(x)
    x_positions = np.arange(len(x_labels))

    advertiser_values = pd.to_numeric(
        advertiser_values,
        errors="coerce",
    )
    entity_values = pd.to_numeric(
        entity_values,
        errors="coerce",
    )

    series = [
        {
            "values": advertiser_values,
            "label": "日均活跃广告主数",
            "color": "#F2994A",
            "label_offset": 12,
            "value_format": lambda value: f"{value:,.0f}",
        },
        {
            "values": entity_values,
            "label": "日均有消耗主体数",
            "color": "#27AE60",
            "label_offset": -18,
            "value_format": lambda value: f"{value:,.1f}",
        },
    ]

    for item in series:
        ax.plot(
            x_positions,
            item["values"],
            marker="o",
            markersize=8,
            linewidth=2.8,
            color=item["color"],
            label=item["label"],
        )

        # 两条线的数据标签分别放在线上方和下方
        for x_position, value in zip(
            x_positions,
            item["values"],
        ):
            ax.annotate(
                item["value_format"](value),
                xy=(x_position, value),
                xytext=(0, item["label_offset"]),
                textcoords="offset points",
                ha="center",
                va=(
                    "bottom"
                    if item["label_offset"] > 0
                    else "top"
                ),
                fontsize=10,
                color=item["color"],
                bbox=dict(
                    boxstyle="round,pad=0.18",
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.88,
                ),
            )

    # 根据两条线的全部数据统一设置纵轴范围
    all_values = pd.concat(
        [advertiser_values, entity_values],
        ignore_index=True,
    )

    value_min = all_values.min()
    value_max = all_values.max()
    value_range = value_max - value_min
    padding = value_range * 0.22

    ax.set_ylim(
        max(0, value_min - padding),
        value_max + padding,
    )

    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)
    ax.set_xlim(-0.3, len(x_labels) - 0.7)

    ax.set_title(
        "线索直播大盘日均活跃广告主数"
        "与日均有消耗主体数变化趋势",
        fontsize=18,
        pad=24,
    )

    ax.set_xlabel("月份", fontsize=12)
    ax.set_ylabel("数量（个/日）", fontsize=12)

    ax.yaxis.set_major_formatter(
        FuncFormatter(
            lambda value, position: f"{value:,.0f}"
        )
    )

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.8,
        alpha=0.28,
    )

    legend = ax.legend(
        loc="upper left",
        fontsize=11,
        frameon=True,
    )
    legend.get_frame().set_facecolor("white")
    legend.get_frame().set_edgecolor("#DDDDDD")
    legend.get_frame().set_alpha(0.9)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#BBBBBB")
    ax.spines["bottom"].set_color("#BBBBBB")

    ax.tick_params(
        axis="x",
        labelsize=10,
        length=0,
    )
    ax.tick_params(
        axis="y",
        labelsize=10,
        length=0,
    )

    fig.tight_layout()

    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
        facecolor="white",
    )

    return fig


# =========================
# 5. 生成三张趋势图
# =========================
figures = []

# 图1：原有月度日均消耗趋势
figures.append(
    create_trend_chart(
        df["月份"],
        df["日均消耗_万元"],
        title="线索直播大盘月度日均消耗趋势",
        legend_label="日均消耗",
        ylabel="日均消耗（万元/日）",
        color="#2F80ED",
        label_format=lambda value: f"{value:,.1f}",
        axis_format=lambda value, position: f"{value:,.1f}",
        output_file="线索直播大盘月度日均消耗趋势.png",
    )
)

# 图2：日均活跃广告主数与日均有消耗主体数
figures.append(
    create_count_comparison_chart(
        df["月份"],
        df["日均活跃广告主数"],
        df["日均有消耗主体数"],
        output_file=(
            "线索直播大盘日均活跃广告主数"
            "与日均有消耗主体数变化趋势.png"
        ),
    )
)

# 图3：日均 CPM 趋势
figures.append(
    create_trend_chart(
        df["月份"],
        df["CPM_元"],
        title="线索直播大盘日均 CPM 变化趋势",
        legend_label="CPM",
        ylabel="CPM（元）",
        color="#9B51E0",
        label_format=lambda value: f"{value:,.2f}",
        axis_format=lambda value, position: f"{value:,.2f}",
        output_file="线索直播大盘日均CPM变化趋势.png",
    )
)

plt.show()
