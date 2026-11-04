from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


folder = Path(__file__).resolve().parent
excel_file = folder.parent / "inputs" / "origin画图(1).xlsx"
data = pd.read_excel(excel_file, sheet_name="双Y图")
x = np.arange(len(data))

plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]
plt.rcParams["hatch.linewidth"] = 0.8

fig, ax1 = plt.subplots(figsize=(10.8, 8.15))
ax2 = ax1.twinx()
fig.subplots_adjust(left=0.09, right=0.88, bottom=0.14, top=0.98)

ax2.bar(x - 0.175, data.iloc[:, 1], width=0.35,
        facecolor="white", edgecolor="#555555", hatch="//", linewidth=1)
ax2.bar(x + 0.175, data.iloc[:, 2], width=0.35,
        facecolor="white", edgecolor="#d36759", hatch="//", linewidth=1)

ax1.set_zorder(ax2.get_zorder() + 1)
ax1.patch.set_visible(False)
ax1.plot(x, data.iloc[:, 4], color="#aaaaaa", linestyle=":", linewidth=1,
         marker="s", markersize=10, markerfacecolor="#555555",
         markeredgewidth=0,
         label="Canopy temp.(100%)")
ax1.plot(x, data.iloc[:, 5], color="#d4aaa0", linestyle=":", linewidth=1,
         marker="o", markersize=11, markerfacecolor="#ed604a",
         markeredgewidth=0,
         label="Canopy temp.(50%)")
ax1.plot(x, data.iloc[:, 6], color="#9fbdcd", linestyle=":", linewidth=1,
         marker="^", markersize=12, markerfacecolor="#0878cd",
         markeredgewidth=0,
         label="Air temp")

ax1.set_xlim(-0.5, 4.5)
ax1.set_ylim(25, 52.5)
ax2.set_ylim(0.70, 1.05)
ax1.set_xticks(x, data.iloc[:, 0])
ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.yaxis.set_major_locator(MultipleLocator(5))
ax1.yaxis.set_minor_locator(MultipleLocator(2.5))
ax2.yaxis.set_major_locator(MultipleLocator(0.05))
ax2.yaxis.set_minor_locator(MultipleLocator(0.025))
ax2.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))

ax1.set_xlabel("Times of the day(hours)", fontsize=25, fontweight="bold",
               labelpad=16)
ax1.set_ylabel("Temperature(°C)", fontsize=25, fontweight="bold",
               labelpad=8)
ax2.set_ylabel("Fractional Light Interception", fontsize=25,
               fontweight="bold", labelpad=10)

for ax in (ax1, ax2):
    ax.tick_params(axis="both", which="major", direction="in",
                   length=9, width=2, labelsize=20, pad=10)
    ax.tick_params(axis="both", which="minor", direction="in",
                   length=4.5, width=1.8)
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight("bold")

ax1.legend(loc="upper left", bbox_to_anchor=(0.024, 0.985),
           frameon=False, fontsize=20, handlelength=2.4,
           handletextpad=0.3, labelspacing=0.35, borderaxespad=0)

output_folder = folder / "outputs"
output_folder.mkdir(exist_ok=True)
fig.savefig(output_folder / "双y轴绘制_原图复刻.png", dpi=300)
plt.show()
