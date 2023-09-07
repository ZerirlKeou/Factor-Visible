import matplotlib.pyplot as plt
import pandas as pd
df=[]
# 读取数据
for i in range(3):
    df.append(pd.read_csv('rvi_'+str(i)+'.csv'))
# 创建一个4x4的子图网格
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))
i = 0
gorge = [(0.242, 0.207, 0.25), (0.344, 0.379, 0.449), (0.4765, 0.586, 0.668), (0.746, 0.656, 0.574),
         (0.547, 0.457, 0.4375)]
# 在每个子图中绘制随机数据
keo = 0
a = gorge[0]
for ax in axes.flat:
    if (i % 3 == 0):
        a = gorge[keo]
        keo = keo + 1
    ax.scatter(df[i]['X'], df[i]['y'], s=5, alpha=0.35, color=a)
    # ax.set_title('Scatter plot of bone('+str(0)+'->'+str(1)+') and Distance Between Wrist and Camera')
    i = i + 1
# 调整子图之间的间距
fig.text(0.5, 0.04, 'Hand Bone Vector Fork Multiplied Area', ha='center')
fig.text(0.04, 0.5, 'The Distance Between Wrist and Camera', va='center', rotation='vertical')
# fig.tight_layout()

fig = plt.figure(figsize=(100, 100))
# 调整子图的布局，使其填充总图
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.50, top=0.50, wspace=0.15, hspace=0.2)

# 显示图像
plt.show()
