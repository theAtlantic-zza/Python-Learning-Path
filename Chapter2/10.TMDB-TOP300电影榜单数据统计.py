"""
TMDB-Top300 电影榜单数据统计

参考自同目录 09.TMDB-Top300电影榜单分析.ipynb，把 4 个分析需求封装成函数：
  1. 每年上映电影数量变化（折线图）
  2. 不同语言电影数量对比（柱状图）
  3. 不同类型电影数量对比（柱状图）
  4. 各评分电影占比（饼图）

最终在 2×2 网格里渲染 4 张图，并保存到 data/TMDB-Top300.png。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# Path(__file__) 是当前脚本的绝对路径；.parent 拿到所在目录。
# 这样不管你在哪个工作目录运行（PyCharm / 终端 / 别的脚本调用），都能找到 data/。
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "movies.csv"
OUTPUT_PATH = BASE_DIR / "data" / "TMDB-Top300.png"

# 只关心这几列；其他列丢掉减少干扰
USE_COLS = ["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言"]

# 饼图阈值：占比 < 2% 的评分合并成"其他"，避免饼图被无数细缝切碎
SMALL_SLICE_THRESHOLD = 0.02

# macOS 系统中文字体；Windows 改成 "Microsoft YaHei"，否则中文显示成方框
plt.rcParams["font.sans-serif"] = ["PingFang SC"]


def load_movies(csv_path: Path) -> pd.DataFrame:
    """读取 CSV 并做基础清洗，返回可直接用于分析的 DataFrame。"""
    data = pd.read_csv(csv_path)

    # CSV 列名两边可能有看不见的空格（notebook 时代直接 usecols 选列因此报过 ValueError）。
    # str.strip() 去掉前后空格，之后才能用 "年份" 这种纯字符串匹配列名。
    data.columns = data.columns.str.strip()

    # 选列。.copy() 是为了拿到独立 DataFrame，
    # 后续修改不会触发 pandas 的 SettingWithCopyWarning。
    data = data[USE_COLS].copy()

    # 重要！大写 "Int64" 是 pandas 的可空整型，能容纳 NaN；
    # 小写 "int64" 是 numpy 整型，遇到缺失值会报错。
    # 我们后面要把缺失年份补回去，所以必须用可空版本。
    data["年份"] = data["年份"].astype("Int64")

    # 缺失年份用"上映时间"前 4 位补（例如 "2008-07-18" -> 2008）。
    # str[:4] 是字符串切片；fillna 只会作用在 NaN 上，已有年份不动。
    data["年份"] = data["年份"].fillna(data["上映时间"].str[:4].astype("Int64"))

    return data


def plot_year_trend(ax: Axes, data: pd.DataFrame) -> None:
    """折线图：每年上映电影数量。"""
    # groupby("年份")["年份"].count() = 按年份分组后数每组多少行。
    # 结果是一个 Series，index 是年份，value 是数量。
    year_count = data.groupby("年份")["年份"].count()

    # ⚠️ 不能直接用 year_count.index 当 x 轴 —— 那样某些没电影的年份会被跳过，折线会"压缩"。
    # 用 range(min, max+1) 生成完整年份范围，缺失年份补 0，折线才会真实反映"那年没电影"。
    years = range(year_count.index.min(), year_count.index.max() + 1)
    counts = [int(year_count.get(y, 0)) for y in years]  # .get(key, 默认值)：年份不存在就返回 0

    ax.plot(list(years), counts, color="green")
    ax.set_title("每年电影数量变化折线图", fontsize=23)
    ax.set_xlabel("年份", fontsize=12)
    ax.set_ylabel("电影数量", fontsize=12)

    # x 轴年份太密，每 10 年标一个刻度即可
    ax.set_xticks(list(years)[::10])
    # y 轴从 0 到最大值+3，每 3 个一格（+3 是为了顶部不顶满）
    ax.set_yticks(range(0, max(counts) + 3, 3))
    # 加虚线网格，alpha=0.3 让线变淡不抢眼
    ax.grid(linestyle="--", alpha=0.3)


def plot_language_bar(ax: Axes, data: pd.DataFrame) -> None:
    """柱状图：不同语言电影数量（数量降序）。"""
    # sort_values(ascending=False)：从大到小排，柱子按高低自然递减更好看
    language_count = data.groupby("语言")["语言"].count().sort_values(ascending=False)

    # .index = 分组的键（语言名）；.values = 每组的数量。tolist() 转 Python 列表给 matplotlib
    ax.bar(language_count.index.tolist(), language_count.values.tolist(),
           color="green", width=0.7)
    ax.set_title("不同语言电影数量柱状图", fontsize=23)

    # labelpad 控制 xlabel 文字和 x 轴的距离：
    #   正数 = 离轴更远，负数 = 离轴更近（甚至覆盖到轴上）。
    # 这里因为 x 轴刻度文字旋转后会向下伸，xlabel 顶到下面去，所以用负值往上挪
    ax.set_xlabel("语言", fontsize=12, labelpad=-12)
    ax.set_ylabel("电影数量", fontsize=12)
    ax.grid(linestyle="--", alpha=0.5)

    # 语言名（"汉语普通话"这种）较长，旋转 45° 避免相邻文字重叠
    ax.tick_params(axis="x", rotation=45)


def plot_genre_bar(ax: Axes, data: pd.DataFrame) -> None:
    """柱状图：不同类型电影数量。"""
    # "类型"列长这样：'剧情,犯罪'、'喜剧,爱情'... 一部电影含多类型，不能直接 groupby。
    # 思路：把每行字符串按逗号拆开，逐个类型累加进字典。
    type_count: dict[str, int] = {}
    for types in data["类型"].str.split(","):  # 每个 types 是一个列表，如 ["剧情", "犯罪"]
        for t in types:
            # dict.get(key, 0)：键存在返回值，否则返回 0。比 if/else 简洁
            type_count[t] = type_count.get(t, 0) + 1

    ax.bar(list(type_count.keys()), list(type_count.values()),
           color="green", width=0.7)
    ax.set_title("不同类型电影数量", fontsize=23)
    ax.set_xlabel("类型", fontsize=12)
    ax.set_ylabel("电影数量", fontsize=12)
    ax.grid(linestyle="--", alpha=0.3)
    ax.tick_params(axis="x", rotation=45)


def plot_score_pie(ax: Axes, data: pd.DataFrame) -> None:
    """饼图：各评分电影占比，占比 < 2% 的合并为"其他"。"""
    score_count = data.groupby("评分")["评分"].count()
    total = score_count.sum()

    # 用布尔索引把数据切成两半：大块自己显示，小块合并避免饼图碎成蛛网
    large = score_count.loc[score_count >= total * SMALL_SLICE_THRESHOLD]
    small = score_count.loc[score_count < total * SMALL_SLICE_THRESHOLD]
    if not small.empty:
        # 给 Series 加一个新键就像往字典里塞键值对：large["其他"] = 小块总和
        large["其他"] = small.sum()

    ax.pie(
        large.values.tolist(),
        labels=large.index.tolist(),
        autopct="%1.1f%%",  # 每块自动显示百分比，1 位小数
        startangle=90,       # 从 12 点钟方向开始切（默认是 3 点钟）
        radius=1.2,          # 饼图半径放大一点，更醒目
    )
    # pad 给标题留点和饼图的间距（默认贴得太近）
    ax.set_title("不同评分电影数量占比饼状图", fontsize=23, pad=25)
    # bbox_to_anchor=(x, y) 用相对坐标把图例钉在饼图右下；ncol=3 让图例三列横排，不要太高
    ax.legend(loc="center left", bbox_to_anchor=(1, -0.2), ncol=3)


def build_dashboard(data: pd.DataFrame) -> Figure:
    """组装 2×2 子图，依次画 4 张图。返回 Figure 对象供保存/显示。"""
    # plt.subplots(2, 2) 返回 (Figure, axes 二维数组)。
    # figsize 单位是英寸，dpi=100 -> 实际像素 2000×1300
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 13), dpi=100)

    # 整张大图的总标题；x、y 用相对坐标（0~1），y=0.95 就是顶部往下 5%
    fig.suptitle("TMDB-Top300电影榜单数据统计", fontsize=23, x=0.5, y=0.95)

    # 子图之间间距：hspace 纵向、wspace 横向。值是相对子图高/宽的比例
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    # axes[行][列]：左上、右上、左下、右下
    plot_year_trend(axes[0][0], data)
    plot_language_bar(axes[0][1], data)
    plot_genre_bar(axes[1][0], data)
    plot_score_pie(axes[1][1], data)

    return fig


def main() -> None:
    data = load_movies(DATA_PATH)
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
#   原始分析思路与 notebook 实现 : ethanzzhao
#   重构 / 函数封装 / 注释整理   : Claude Opus 4.7 (1M context)
#                                  — Anthropic, via Claude Code
# ─────────────────────────────────────────────────────────────
