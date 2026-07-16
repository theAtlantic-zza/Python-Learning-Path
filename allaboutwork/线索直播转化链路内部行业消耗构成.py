import pandas as pd
import matplotlib.pyplot as plt

# 所有消耗统一使用“万元”
data = [
    # 金融
    {
        "行业": "金融",
        "链路": "二跳企业微信",
        "消耗_万元": 38700,
        "CTR": 2.42,
        "CTCVR": 4.98
    },
    {
        "行业": "金融",
        "链路": "手机号码授权/拨打",
        "消耗_万元": 620,
        "CTR": 1.41,
        "CTCVR": 3.43
    },

    # 房家
    {
        "行业": "房家",
        "链路": "二跳企业微信",
        "消耗_万元": 25,
        "CTR": 5.37,
        "CTCVR": 2.34
    },
    {
        "行业": "房家",
        "链路": "手机号码授权/拨打",
        "消耗_万元": 9300,
        "CTR": 1.21,
        "CTCVR": 23.81
    },

    # 汽车
    {
        "行业": "汽车",
        "链路": "二跳企业微信",
        "消耗_万元": 1.6,
        "CTR": 2.42,
        "CTCVR": 0.36
    },
    {
        "行业": "汽车",
        "链路": "手机号码授权/拨打",
        "消耗_万元": 5900,
        "CTR": 1.06,
        "CTCVR": 62.70
    },

    # 教育
    {
        "行业": "教育",
        "链路": "二跳企业微信",
        "消耗_万元": 2100,
        "CTR": 1.72,
        "CTCVR": 8.04
    },
    {
        "行业": "教育",
        "链路": "手机号码授权/拨打",
        "消耗_万元": 117,
        "CTR": 0.85,
        "CTCVR": 12.67
    }
]

df = pd.DataFrame(data)

print(df)



# 设置中文字体
plt.rcParams["font.sans-serif"] = [
    "PingFang SC",
    "Heiti SC",
    "Arial Unicode MS",
    "SimHei",
    "Microsoft YaHei"
]
plt.rcParams["axes.unicode_minus"] = False

# 固定行业顺序
industry_order = ["金融", "房家", "汽车", "教育"]

df["行业"] = pd.Categorical(
    df["行业"],
    categories=industry_order,
    ordered=True
)

# 两张图中的行业颜色保持一致
industry_colors = {
    "金融": "#2F80ED",
    "房家": "#F2994A",
    "汽车": "#27AE60",
    "教育": "#9B51E0"
}


# 小于 1% 的占比不在扇区上显示，避免文字重叠
def show_percentage(pct):
    if pct >= 1:
        return f"{pct:.1f}%"
    return ""


# 创建左右两张图
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

chains = ["二跳企业微信", "手机号码授权/拨打"]

for ax, chain in zip(axes, chains):

    chain_df = (
        df[df["链路"] == chain]
        .sort_values("行业")
        .copy()
    )

    industries = chain_df["行业"].astype(str).tolist()
    values = chain_df["消耗_万元"].tolist()

    colors = [
        industry_colors[industry]
        for industry in industries
    ]

    wedges, _, percentage_texts = ax.pie(
        values,
        colors=colors,
        startangle=90,
        counterclock=False,
        autopct=show_percentage,
        pctdistance=0.78,
        wedgeprops={
            "width": 0.42,
            "edgecolor": "white",
            "linewidth": 2
        }
    )

    # 调整扇区百分比字体
    for text in percentage_texts:
        text.set_fontsize(10)

    total_spend = sum(values)

    # 环形图中间显示链路总消耗
    ax.text(
        0,
        0,
        f"总消耗\n{total_spend / 10000:.2f}亿元",
        ha="center",
        va="center",
        fontsize=18
    )

    ax.set_title(
        chain,
        fontsize=18,
        pad=18
    )

    # 图例中显示真实金额
    legend_labels = [
        f"{industry}：{value:,.1f} 万元"
        for industry, value in zip(industries, values)
    ]

    ax.legend(
        wedges,
        legend_labels,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.18),
        ncol=2,
        frameon=False,
        fontsize=18
    )

    ax.axis("equal")


fig.suptitle(
    "不同转化链路的行业消耗构成",
    fontsize=25,
    y=0.98
)

plt.tight_layout(rect=[0, 0.05, 1, 0.93])

# 必须先保存，再显示
fig.savefig(
    "不同转化链路的行业消耗构成.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()


# ==============================
# CTR、CTCVR 哑铃图
# ==============================

import numpy as np
from matplotlib.ticker import FuncFormatter


def plot_dumbbell_chart(
    data,
    metric,
    title,
    output_file,
    x_max=None
):
    """
    绘制各行业两种转化链路的指标对比哑铃图。

    metric 可填写：
    "CTR" 或 "CTCVR"
    """

    # 固定行业显示顺序
    industry_order = ["金融", "房家", "汽车", "教育"]

    # 将数据转换成宽表
    plot_df = (
        data.pivot(
            index="行业",
            columns="链路",
            values=metric
        )
        .reindex(industry_order)
    )

    # 获取两条链路的数据
    wechat_values = plot_df["二跳企业微信"]
    phone_values = plot_df["手机号码授权/拨打"]

    # 每个行业在纵轴上的位置
    y_positions = np.arange(len(plot_df))

    # 配色
    color_wechat = "#2F80ED"
    color_phone = "#F2994A"
    connection_color = "#D0D0D0"

    # 创建画布
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 1. 绘制连接线
    for y, wechat, phone in zip(
        y_positions,
        wechat_values,
        phone_values
    ):
        ax.plot(
            [wechat, phone],
            [y, y],
            color=connection_color,
            linewidth=3,
            zorder=1
        )

    # 2. 绘制企微数据点
    ax.scatter(
        wechat_values,
        y_positions,
        s=120,
        color=color_wechat,
        label="二跳企业微信",
        zorder=3
    )

    # 3. 绘制手机号数据点
    ax.scatter(
        phone_values,
        y_positions,
        s=120,
        color=color_phone,
        label="手机号码授权/拨打",
        zorder=3
    )

    # 4. 企微指标标签，放在点上方
    for x, y in zip(wechat_values, y_positions):
        ax.annotate(
            f"{x:.2f}%",
            xy=(x, y),
            xytext=(0, 12),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            color=color_wechat,
            bbox=dict(
                boxstyle="round,pad=0.15",
                facecolor="white",
                edgecolor="none",
                alpha=0.85
            )
        )

    # 5. 手机号指标标签，放在点下方
    for x, y in zip(phone_values, y_positions):
        ax.annotate(
            f"{x:.2f}%",
            xy=(x, y),
            xytext=(0, -14),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=11,
            color=color_phone,
            bbox=dict(
                boxstyle="round,pad=0.15",
                facecolor="white",
                edgecolor="none",
                alpha=0.85
            )
        )

    # 6. 纵轴设置
    ax.set_yticks(y_positions)
    ax.set_yticklabels(plot_df.index, fontsize=12)

    # 让金融显示在最上方
    ax.invert_yaxis()

    # 7. 横轴显示百分号
    ax.xaxis.set_major_formatter(
        FuncFormatter(lambda value, position: f"{value:g}%")
    )

    ax.set_xlabel(f"{metric}（%）", fontsize=13)
    ax.set_title(title, fontsize=18, pad=25)

    # 8. 横轴范围
    if x_max is None:
        max_value = max(
            wechat_values.max(),
            phone_values.max()
        )
        ax.set_xlim(0, max_value * 1.18)
    else:
        ax.set_xlim(0, x_max)

    # 9. 网格线
    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.25
    )

    # 10. 图例
    legend = ax.legend(
        loc="best",
        bbox_to_anchor=(0.5, 1.05),
        ncol=2,
        frameon=True,
        fontsize=11
    )

    legend.get_frame().set_edgecolor("#DDDDDD")
    legend.get_frame().set_alpha(0.9)

    # 11. 美化边框
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=11)

    plt.tight_layout()

    # 12. 先保存，再显示
    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
        facecolor="white"
    )

    plt.show()


# ==============================
# 生成 CTR 哑铃图
# ==============================

plot_dumbbell_chart(
    data=df,
    metric="CTR",
    title="各行业不同转化链路 CTR 对比",
    output_file="各行业不同转化链路CTR对比.png",
    x_max=6
)


# ==============================
# 生成 CTCVR 哑铃图
# ==============================

plot_dumbbell_chart(
    data=df,
    metric="CTCVR",
    title="各行业不同转化链路 CTCVR 对比",
    output_file="各行业不同转化链路CTCVR对比.png",
    x_max=70
)

from matplotlib.ticker import FuncFormatter


def format_spend(value):
    """
    将以万元为单位的消耗格式化为更容易阅读的金额。
    """
    if value >= 10000:
        return f"{value / 10000:.2f}亿元"
    elif value >= 100:
        return f"{value:,.0f}万元"
    else:
        return f"{value:,.1f}万元"


def plot_industry_ctr_by_chain(
    data,
    chain,
    title,
    output_file,
    bar_color
):
    """
    固定一条转化链路，对比不同行业的 CTR。
    柱尾同时标注 CTR 和消耗规模。
    """

    # 1. 筛选指定链路并按照 CTR 从低到高排序
    plot_df = (
        data[data["链路"] == chain]
        .copy()
        .sort_values("CTR", ascending=True)
    )

    # 2. 计算行业 CTR 最大差异
    ctr_max = plot_df["CTR"].max()
    ctr_min = plot_df["CTR"].min()
    ctr_gap = ctr_max - ctr_min

    # 3. 创建画布
    fig, ax = plt.subplots(figsize=(11, 6.5))

    # 4. 绘制横向柱状图
    bars = ax.barh(
        plot_df["行业"].astype(str),
        plot_df["CTR"],
        height=0.55,
        color=bar_color,
        alpha=0.88
    )

    # 5. 在柱子右侧标注 CTR 和消耗
    for bar, ctr, spend in zip(
        bars,
        plot_df["CTR"],
        plot_df["消耗_万元"]
    ):
        ax.annotate(
            f"{ctr:.2f}%  ｜  消耗 {format_spend(spend)}",
            xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
            xytext=(10, 0),
            textcoords="offset points",
            ha="left",
            va="center",
            fontsize=11
        )

    # 6. 横轴显示百分号
    ax.xaxis.set_major_formatter(
        FuncFormatter(lambda value, position: f"{value:g}%")
    )

    # 给右侧标签预留空间
    ax.set_xlim(0, ctr_max * 1.55)

    ax.set_xlabel("CTR（%）", fontsize=12)
    ax.set_ylabel("行业", fontsize=12)

    # 7. 标题
    ax.set_title(
        title,
        fontsize=18,
        pad=30
    )

    # 8. 标题下方显示行业差异
    ax.text(
        0.5,
        1.015,
        f"行业最高与最低相差 {ctr_gap:.2f} 个百分点",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=11,
        color="#666666"
    )

    # 9. 网格及边框
    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.25
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.tick_params(axis="y", length=0, labelsize=12)
    ax.tick_params(axis="x", labelsize=10)

    # 消耗只能近似反映样本规模，因此增加口径提示
    fig.text(
        0.5,
        0.015,
        "消耗用于辅助判断数据规模，CTR 稳定性仍需结合曝光量、点击量及投放客户数验证。",
        ha="center",
        fontsize=9.5,
        color="#777777"
    )

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])

    # 10. 先保存，再显示
    fig.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
        facecolor="white"
    )

    plt.show()


# ==============================
# 图一：企业微信链路，各行业 CTR 对比
# ==============================

plot_industry_ctr_by_chain(
    data=df,
    chain="二跳企业微信",
    title="二跳企业微信链路：各行业 CTR 对比",
    output_file="二跳企业微信链路各行业CTR对比.png",
    bar_color="#2F80ED"
)


# ==============================
# 图二：手机号链路，各行业 CTR 对比
# ==============================

plot_industry_ctr_by_chain(
    data=df,
    chain="手机号码授权/拨打",
    title="手机号码授权拨打链路：各行业 CTR 对比",
    output_file="手机号码授权拨打链路各行业CTR对比.png",
    bar_color="#F2994A"
)