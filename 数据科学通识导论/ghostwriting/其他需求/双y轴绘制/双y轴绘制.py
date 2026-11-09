from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


folder = Path(__file__).resolve().parent
excel_file = folder / "inputs" / "origin画图(1).xlsx"
data = pd.read_excel(excel_file, sheet_name="双Y图")
x = np.arange(len(data))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, data.iloc[:, 4], color="k", marker="s", linestyle=":",
         label="Canopy temp.(100%)")
ax1.plot(x, data.iloc[:, 5], color="r", marker="o", linestyle=":",
         label="Canopy temp.(50%)")
ax1.plot(x, data.iloc[:, 6], color="b", marker="^", linestyle=":",
         label="Air temp")

ax2.bar(x - 0.175, data.iloc[:, 1], width=0.35,
        color="gray", alpha=0.3)
ax2.bar(x + 0.175, data.iloc[:, 2], width=0.35,
        color="r", alpha=0.3)

ax1.set_xticks(x, data.iloc[:, 0])
ax1.set_xlabel("Times of the day(hours)")
ax1.set_ylabel("Temperature(°C)")
ax2.set_ylabel("Fractional Light Interception")
ax1.set_ylim(25, 52.5)
ax2.set_ylim(0.70, 1.05)
ax1.legend(loc="upper left")
fig.tight_layout()

output_folder = folder / "outputs"
output_folder.mkdir(exist_ok=True)
fig.savefig(output_folder / "双y轴绘制.png", dpi=300)
plt.show()
