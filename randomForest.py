import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import csv
import ast
import math
import joblib

df = pd.read_csv('cci.csv')
print(df['X'].tolist())

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['X'].tolist(), df['y'].tolist(), test_size=0.1, random_state=0)

# 定义随机森林模型
rf = RandomForestRegressor(n_estimators=200, random_state=0, max_features='log2')

# 训练模型
rf.fit(X_train, y_train)
print(y_test)
joblib.dump(rf, "HandDistanceForest2.joblib")  # save
# 在测试集上评估模型性能
score = rf.score(X_test, y_test)
print("模型评分：", score)

# 使用模型进行预测
y_pred = rf.predict(X_test)
print("预测结果：", y_pred)

# 计算回归模型的评估指标
print("MSE:", mean_squared_error(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
