"""TMDB-TOP300 电影榜单数据统计

把 09.TMDB-TOP300电影榜单分析.ipynb 中的探索过程整理成可复用的脚本。

代码分为四层：
    1. 配置与工具：中文字体、数据/图片路径
    2. 数据加载：load_movies
    3. 统计计算：count_movies_by_year / by_language / by_genre / by_rating
    4. 图形绘制：plot_year_trend / plot_language_bar / plot_genre_bar / plot_rating_pie

运行：
    python 10.TMDB-TOP300电影榜单数据统计.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

# ==================== 配置区 ====================

# 以脚本自身位置为基准，保证从任意目录运行都能找到数据
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "movie_top240.csv"
OUTPUT_IMAGE = BASE_DIR / "data" / "02.png"  # 沿用 notebook 的输出文件名

# 需要读取的列（原表列很多，只取分析用到的）
USE_COLS = [
    "电影名",
    "电影发布年份",
    "电影上映时间",
    "电影类型",
    "电影时长",
    "电影评分",
    "电影语言",
]

# 多个类型之间的分隔符："动画,动作,冒险,科幻"
GENRE_SEP = ","

# 语言列缺失值的占位符
UNKNOWN_LANGUAGE = "未知"

# 饼图合并阈值：数量小于该值的评分区间合并为“其他”
MIN_PIE_COUNT = 5

# 图表标题
TITLE_MAIN = "TMDB-TOP300电影榜单分析"


# ==================== 工具函数 ====================


def setup_chinese_font() -> None:
    """设置 matplotlib 中文字体，否则标题/标签会显示成方块"""
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示为方块


def load_movies(path: Path = DATA_FILE) -> pd.DataFrame:
    """读取电影数据 CSV"""
    if not path.exists():
        raise FileNotFoundError(f"找不到数据文件：{path}")
    return pd.read_csv(path, usecols=USE_COLS)


# ==================== 统计计算 ====================


def count_movies_by_year(df: pd.DataFrame) -> pd.Series:
    """按发布年份统计电影数量，缺失年份补 0（保证折线连续不断档）"""
    year_count = df.groupby("电影发布年份")["电影名"].count()
    if year_count.empty:
        return year_count
    years = range(int(year_count.index.min()), int(year_count.index.max()) + 1)
    # 没有电影的年份用 0 填充，避免折线图直接跳过该年份
    return pd.Series({year: int(year_count.get(year, 0)) for year in years})


def count_movies_by_language(df: pd.DataFrame) -> pd.Series:
    """按语言统计电影数量，'-' 和空值统一归为“未知”，结果按数量降序"""
    language = df["电影语言"].replace("-", UNKNOWN_LANGUAGE).fillna(UNKNOWN_LANGUAGE)
    return language.value_counts()


def count_movies_by_genre(df: pd.DataFrame, sep: str = GENRE_SEP) -> pd.Series:
    """按类型统计电影数量

    一部电影有多个类型（"动画,动作,冒险"），需要先拆分再展开：
        split(sep)  字符串 -> 列表
        explode()   列表元素各占一行
        strip()     去掉空格，避免“动作”和“ 动作”被算成两类
    """
    return (
        df["电影类型"]
        .dropna()
        .str.split(sep)
        .explode()
        .str.strip()
        .value_counts()
    )


def count_movies_by_rating(df: pd.DataFrame, min_count: int = MIN_PIE_COUNT) -> pd.Series:
    """按评分统计电影数量，数量过少的评分区间合并为“其他”"""
    rating_count = df.groupby("电影评分")["电影名"].count().sort_index()
    small = rating_count[rating_count < min_count]
    if small.empty:
        return rating_count
    # 先剔除小类，再把它们的总数作为“其他”追加回去
    main_part = rating_count[rating_count >= min_count]
    return pd.concat([main_part, pd.Series({"其他": int(small.sum())})])


# ==================== 图形绘制 ====================


def create_figure() -> tuple[Figure, dict[str, Axes]]:
    """创建 2x2 的画布，返回画布本体和四个子图（按用途命名）"""
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle(TITLE_MAIN, fontsize=16, x=0.5, y=0.95)
    # wspace: 子图水平间距，hspace: 子图垂直间距
    fig.subplots_adjust(wspace=0.3, hspace=0.4)
    axes: dict[str, Axes] = {
        "year": ax[0][0],
        "language": ax[0][1],
        "genre": ax[1][0],
        "rating": ax[1][1],
    }
    return fig, axes


def plot_year_trend(ax: Axes, year_count: pd.Series) -> None:
    """需求一：每一年上映电影数量的变化（折线图）"""
    x = [int(i) for i in year_count.index.tolist()]
    y = [int(v) for v in year_count.values.tolist()]
    ax.plot(x, y)
    ax.set_title("电影上映年份统计")
    ax.set_xlabel("电影发布年份")
    ax.set_ylabel("电影数量")
    if x:  # 年份太多时每隔 10 年显示一个刻度
        ax.set_xticks(x[::10])
        ax.set_yticks(list(range(0, max(y) + 1, 3)))  # 整数刻度，避免出现小数
    ax.grid(linestyle="--", alpha=0.5)


def plot_language_bar(ax: Axes, language_count: pd.Series) -> None:
    """需求二：不同语言的电影数量对比（柱状图）"""
    x = language_count.index.tolist()
    y = [int(v) for v in language_count.values.tolist()]
    ax.bar(x, y)
    ax.tick_params(axis="x", rotation=45, labelsize=9)  # 标签倾斜，防止重叠
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("电影语言统计")
    ax.set_xlabel("电影语言")
    ax.set_ylabel("电影数量")
    ax.grid(linestyle="--", alpha=0.5)


def plot_genre_bar(ax: Axes, genre_count: pd.Series) -> None:
    """需求三：不同类型的电影数量对比（柱状图）"""
    x = genre_count.index.tolist()
    y = [int(v) for v in genre_count.values.tolist()]
    ax.bar(x, y, color="g")
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("电影类型统计")
    ax.set_xlabel("电影类型")
    ax.set_ylabel("电影数量")
    ax.grid(linestyle="--", alpha=0.5)


def plot_rating_pie(ax: Axes, rating_count: pd.Series) -> None:
    """需求四：各评分电影占比（饼图）"""
    labels = [str(i) for i in rating_count.index.tolist()]
    values = [int(v) for v in rating_count.values.tolist()]
    # radius: 饼图半径；autopct: 占比格式
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=0, radius=1.2)
    ax.set_title("电影评分统计")
    # bbox_to_anchor: 图例偏移量（0.5 控制水平，-0.2 控制垂直）
    ax.legend(loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.3), fontsize=12)


# ==================== 主流程 ====================


def main() -> None:
    setup_chinese_font()

    df = load_movies()
    print(f"共读取 {len(df)} 部电影")

    # 统计
    year_count = count_movies_by_year(df)
    language_count = count_movies_by_language(df)
    genre_count = count_movies_by_genre(df)
    rating_count = count_movies_by_rating(df)

    print("\n【电影语言 TOP10】")
    print(language_count.head(10).to_string())
    print("\n【电影类型 TOP10】")
    print(genre_count.head(10).to_string())

    # 绘图
    fig, axes = create_figure()
    plot_year_trend(axes["year"], year_count)
    plot_language_bar(axes["language"], language_count)
    plot_genre_bar(axes["genre"], genre_count)
    plot_rating_pie(axes["rating"], rating_count)

    # 保存并显示
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_IMAGE)
    print(f"\n图片已保存：{OUTPUT_IMAGE}")
    plt.show()


if __name__ == "__main__":
    main()
