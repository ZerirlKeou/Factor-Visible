import pandas as pd
import seaborn as sns
import Multifunction
# 读取CSV文件
from matplotlib import pyplot as plt

df = pd.read_csv('alpha1.csv')

# df['X'] = df['X'].apply(lambda x: float(x.strip('[]')))
# df['X'] = pd.to_numeric(df['X'])
# df['X'] = df.rolling(window=14).apply(Multifunction.Rank(df['X']))
# 绘制双变量密度图
sns.kdeplot(data=df, x="X", y="y", cmap="hsv", fill=True, alpha=.5, linewidth=0)
# 绘制散点图
sns.scatterplot(data=df, x="X", y="y")
sns.rugplot(data=df, x="X", y="y")
# 添加标题和轴标签
# plt.title('Kernel Density Estimation of Area and the Distance')
plt.xlabel('alpha1')
plt.ylabel('change')

# 显示图形
plt.show()
