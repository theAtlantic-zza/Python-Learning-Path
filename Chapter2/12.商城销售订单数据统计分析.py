"""
商城销售订单数据统计分析

来源：黑马程序员 PPT 练习 —— 某连锁店销售订单统计分析。
4 个需求：
  1. 每天销售额变化（折线图）
  2. 不同城市累计销售数量对比（柱状图）
  3. 不同产品类型订单比例（饼图）
  4. 不同支付方式订单比例（饼图）

最终在 2×2 网格里渲染 4 张图，并保存到 data/商城销售订单统计.png。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# Path(__file__) 是当前脚本的绝对路径；.parent 拿到所在目录。
# 这样不管你在哪个工作目录运行（PyCharm / 终端 / 别的脚本调用），都能找到 data/。
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "sales02.csv"
OUTPUT_PATH = BASE_DIR / "data" / "商城销售订单统计.png"

# macOS 系统中文字体；Windows 改成 "Microsoft YaHei"，否则中文显示成方框
plt.rcParams["font.sans-serif"] = ["PingFang SC"]
# 防止负号在某些字体下被渲染成方块（折线图 y 轴出现负值时会用到）
plt.rcParams["axes.unicode_minus"] = False


def load_orders(csv_path: Path) -> pd.DataFrame:
    """读取订单 CSV 并做必要清洗：列名 strip、日期转 datetime、过滤异常值、补销售额列。"""
    data = pd.read_csv(csv_path)

    # CSV 列名两边可能有看不见的空格；str.strip() 去掉前后空格，保险动作。
    data.columns = data.columns.str.strip()

    # 异常值过滤：单价或销售数量 ≤ 0 视为录入错误（比如 PPT 截图里第 7 行袜子 -29）。
    # 用布尔索引取交集：两个条件都满足才保留。~ 表示按位取反，用来找被剔除的行做日志
    bad_rows = data[(data["销售数量"] <= 0) | (data["单价"] <= 0)]
    if len(bad_rows) > 0:
        print(f" 过滤掉 {len(bad_rows)} 条异常订单（销售数量或单价 ≤ 0）")
    data = data[(data["销售数量"] > 0) & (data["单价"] > 0)].copy()

    # 日期统一：CSV 里大多数是 "2025-06-02"，但混入了 "2025/06/02" 这种斜杠格式。
    # 直接按字符串 groupby 会把它们当成两天 —— pd.to_datetime 能识别两种格式，转完都是同一天。
    # format="mixed" 让 pandas 对每行自由推断格式（pandas 2.0+ 支持）。
    data["订单日期"] = pd.to_datetime(data["订单日期"], format="mixed")

    # 衍生列：销售额 = 销售数量 × 单价。后面折线图直接用，避免每个图里重算
    data["销售额"] = data["销售数量"] * data["单价"]

    return data


def plot_daily_sales(ax: Axes, data: pd.DataFrame) -> None:
    """折线图：每天销售额变化。"""
    # 按日期分组求和，得到 Series：index=日期，value=当日销售额。
    # 日期已经是 datetime 类型，groupby 后天然按时间升序排列
    daily = data.groupby("订单日期")["销售额"].sum()

    ax.plot(daily.index, daily.values, color="orange")
    ax.set_title("每天销售额变化", fontsize=23)
    ax.set_xlabel("日期", fontsize=12)
    ax.set_ylabel("销售额（元）", fontsize=12)

    # 日期标签太密会重叠，旋转 45° 让相邻标签错开
    ax.tick_params(axis="x", rotation=45)
    ax.grid(linestyle="--", alpha=0.3)


def plot_city_bar(ax: Axes, data: pd.DataFrame) -> None:
    """柱状图：不同城市累计销售数量（降序）。"""
    # 按城市分组累加销售数量。注意是"累计销售数量"，不是订单数 ——
    # 一个订单可能买 10 件，对应 10 件销量，不是 1 单 = 1 件
    city_count = data.groupby("客户所在城市")["销售数量"].sum().sort_values(ascending=False)

    ax.bar(city_count.index.tolist(), city_count.values.tolist(),
           color="orange", width=0.7)
    ax.set_title("各个城市的销售数量统计", fontsize=23)
    ax.set_xlabel("城市", fontsize=12)
    ax.set_ylabel("销售数量", fontsize=12)
    ax.grid(linestyle="--", alpha=0.3)
    # 城市名旋转 45° 避免相邻文字重叠
    ax.tick_params(axis="x", rotation=45)


def plot_category_pie(ax: Axes, data: pd.DataFrame) -> None:
    """饼图：不同产品类型订单数量占比。"""
    # value_counts() 一步搞定"分组 + 计数 + 降序"，比 groupby().count().sort_values() 更紧凑
    category_count = data["产品类别"].value_counts()

    ax.pie(
        category_count.values.tolist(),
        labels=category_count.index.tolist(),
        autopct="%1.1f%%",   # 每块自动显示百分比，1 位小数
        startangle=90,       # 从 12 点钟方向开始切（默认是 3 点钟）
    )
    ax.set_title("不同产品类型对应的订单数量", fontsize=23, pad=20)
    # 图例横排放在饼图下方，ncol 设大点保证一行排得下
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05),
              ncol=len(category_count))


def plot_payment_pie(ax: Axes, data: pd.DataFrame) -> None:
    """饼图：不同支付方式订单数量占比。"""
    payment_count = data["支付方式"].value_counts()

    ax.pie(
        payment_count.values.tolist(),
        labels=payment_count.index.tolist(),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("各支付方式对应的订单数量", fontsize=23, pad=20)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05),
              ncol=len(payment_count))


def build_dashboard(data: pd.DataFrame) -> Figure:
    """组装 2×2 子图，依次画 4 张图。返回 Figure 对象供保存/显示。"""
    # plt.subplots(2, 2) 返回 (Figure, axes 二维数组)。
    # figsize 单位是英寸，dpi=100 -> 实际像素 2000×1300
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 13), dpi=100)

    # 整张大图的总标题
    fig.suptitle("商城销售数据统计分析", fontsize=23, x=0.5, y=0.97)

    # 子图之间间距：hspace 纵向、wspace 横向。值是相对子图高/宽的比例。
    # 饼图带底部图例，纵向间距要留多点，否则上下两行图会贴在一起
    fig.subplots_adjust(hspace=0.55, wspace=0.25)

    # axes[行][列]：左上、右上、左下、右下
    plot_daily_sales(axes[0][0], data)
    plot_city_bar(axes[0][1], data)
    plot_category_pie(axes[1][0], data)
    plot_payment_pie(axes[1][1], data)

    return fig


def main() -> None:
    data = load_orders(DATA_PATH)
    print(f"清洗后保留 {len(data)} 条订单")
    fig = build_dashboard(data)

    # bbox_inches="tight" 自动裁掉四周空白；dpi=300 保存高清（屏幕显示用 100 就够）
    fig.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
    print(f"已保存到 {OUTPUT_PATH}")

    # 弹出交互窗口。PyCharm 里会在右侧 SciView 显示
    plt.show()


# 这一行 == "如果是直接运行这个文件就跑 main()"。
# 别的脚本 `import` 这个文件时不会自动执行，方便做单元测试 / 复用某个函数
if __name__ == "__main__":
    main()


# ─────────────────────────────────────────────────────────────
# 协助署名
#   原始分析思路与练习需求 : ethanzzhao（黑马程序员 PPT 练习）
#   函数封装 / 注释整理   : Claude Opus 4.7 (1M context)
#                          — Anthropic, via Claude Code
# ─────────────────────────────────────────────────────────────
