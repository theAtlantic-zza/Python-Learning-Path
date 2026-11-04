# 双 Y 轴绘制

两版读取同一份 [Origin 数据](../inputs/origin画图%281%29.xlsx) 的 `双Y图` 工作表，对应同一张[题图](../inputs/双y轴绘制_题目.jpeg)。

- [基础版代码](双y轴绘制.py)和[基础版图片](outputs/双y轴绘制.png)使用普通填色柱形与课程里的基本绘图设置。
- [原图复刻代码](双y轴绘制_原图复刻.py)和[原图复刻图片](outputs/双y轴绘制_原图复刻.png)还原题图的斜线柱形、细点线、长短刻度、字体与边框。截图的压缩和字体渲染会带来少量外观差异。

## 对照代码理解画图技巧

1. **两套 Y 轴共享时间。** `ax2 = ax1.twinx()` 创建右侧坐标轴。温度曲线画在 `ax1`，截光率柱形画在 `ax2`，分别按左侧 25～52.5 和右侧 0.70～1.05 读数。两套刻度使不同量纲的数据可以放在同一张图里。
2. **两根柱形并排。** 每个时间的位置是 `x`。柱宽为 `0.35`，两组柱子的中心各偏移半个柱宽，所以使用 `x - 0.175` 和 `x + 0.175`。
3. **白底斜线填充。** `facecolor="white"` 设置柱形内部底色，`edgecolor` 设置轮廓与斜线颜色，`hatch="//"` 生成斜线图案。`hatch` 中重复斜杠可以增加密度，`plt.rcParams["hatch.linewidth"]` 控制斜线粗细。
4. **浅色点线与醒目的点。** `linestyle=":"` 设置点线，`linewidth` 控制连线粗细，`color` 设置连线颜色。`marker` 的 `"s"`、`"o"`、`"^"` 分别是方块、圆点和三角形。`markersize` 控制点的大小，`markerfacecolor` 单独设置点的填色，因此可以同时得到浅色线和深色点。
5. **让曲线显示在柱形上方。** `ax1.set_zorder(ax2.get_zorder() + 1)` 把温度坐标轴放到上层。`ax1.patch.set_visible(False)` 隐藏上层坐标轴的背景矩形，让下层柱形露出来。跨两个坐标轴叠放时，需要一起处理轴的顺序和背景。
6. **刻度分长短并朝内。** `tick_params(direction="in")` 设置方向，`length` 和 `width` 设置刻度线长短与粗细。`which="major"` 对应带数字的主刻度，`which="minor"` 对应较短的次刻度。`MultipleLocator(5)` 让左轴每隔 5 显示主刻度，`MultipleLocator(2.5)` 在中间补一个次刻度。右轴对应间隔为 0.05 和 0.025。
7. **右轴统一显示两位小数。** `FormatStrFormatter("%.2f")` 将刻度显示为 `0.70`、`0.75`、`1.00` 等形式。`set_ylim()` 控制可见范围，柱顶的截光率要按右轴读数。
8. **字体、边框与位置。** `fontsize` 和 `fontweight="bold"` 控制字号、加粗，`labelpad` 控制轴标题与刻度文字的距离。`spines` 是绘图区的四条边框，`set_linewidth()` 调整边框粗细。`figsize` 决定画布宽高，`subplots_adjust()` 留出四周的标签空间。
9. **图例只显示三条温度曲线。** 三次 `plot()` 的 `label` 提供图例文字。`legend(frameon=False)` 隐藏图例框，`loc` 和 `bbox_to_anchor` 调整位置。`handlelength`、`handletextpad`、`labelspacing` 分别控制示例线长度、线与文字间距、各行间距。

先读基础版的 `twinx()`、`bar()`、`plot()` 和坐标范围，再在复刻版中对照 `hatch`、`tick_params`、`MultipleLocator` 和 `set_zorder()`。每次只改一个参数并运行，便于看出它对应的效果。
