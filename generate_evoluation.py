import random
import math
import numpy as np
import pandas as pd
import tushare as ts

ts.set_token("9719560105905c9ea068aec2f4834ad3932cb6e4778b24ef0f8acc2f")
pro = ts.pro_api()
# pool = ['000001.SZ', '000002.SZ', '000004.SZ', '000005.SZ', '000008.SZ', '000004.SZ', '600010.SH', '600020.SH']
pool = ['000001.SZ']
for i in pool:
    df = pro.daily(ts_code=i, start_date='20170602', end_date='20230421')
    dfy = pro.daily(ts_code=i, start_date='20170601', end_date='20230420')


# 定义双变量函数集合
def multi(a, b):
    return a * b


def subtract(a, b):
    return a - b


def add(a, b):
    return a + b


# 定义最后一代处理函数集合
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def absolute(x):
    return abs(x)


def sine(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def sqrt(x):
    return math.sqrt(x)


def exp(x):
    return math.exp(x)


def logarithm(x):
    return math.log(x)


function_Two = [multi, subtract, add]
function_LastSet = [sigmoid, absolute, sine, cos, tan, sqrt, logarithm]
golden_nums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# 定义种群大小和迭代次数
population_size = 50
num_generations = 100


# 定义适应度函数
def fitness(alpha, pct_chg):
    a = pd.Series(alpha)
    b = pd.Series(pct_chg)
    # 计算与涨跌值相关的相关系数
    corralation = a.corr(b)
    return corralation


# 计算组合数
def Combinatorial(n, m):
    Min = min(m, n - m)
    res = 1
    for i in range(0, Min):
        res = res * (n - i) / (Min - i)
    return int(res)


# 末位淘汰制
def eliminate_half(lst):
    lst.sort(reverse=True, key=lambda x: x[0])  # 根据每个子列表中的第一个数字排序
    half_idx = len(lst) // 2  # 计算中间位置
    lst = lst[:half_idx]  # 删除排名靠后的50%的元素
    return lst


# 定义遗传操作
# def crossover(parent1, parent2):
#     # 单点交叉
#     crossover_point = random.randint(0, len(parent1) - 1)
#     child1 = parent1[:crossover_point] + parent2[crossover_point:]
#     child2 = parent2[:crossover_point] + parent1[crossover_point:]
#     return child1, child2
#
#
# def mutation(individual):
#     # 随机变异一个变量
#     mutation_index = random.randint(0, len(individual) - 1)
#     mutation_range = var_ranges[var_names[mutation_index]]
#     mutation_value = random.uniform(mutation_range[0], mutation_range[1])
#     individual[mutation_index] = mutation_value
#     return individual
#
#
# 初始化种群

# print(df)

population = [df['close'], df['open'], df['high'], df['low'], df['pre_close'], df['vol']]
print(population[0])
score = []
# 第一代进化
for i in range(Combinatorial(len(population), 2)):
    for k in range(len(population)):
        p = k + 1
        while p < len(population):
            for j in function_Two:
                score.append([fitness(j(population[k], population[p]), dfy['pct_chg']), j, p, k])

            p = p + 1
print(score)
new_list = eliminate_half(score)
print(new_list)
print(fitness(list(map(sigmoid,new_list[0][1](population[new_list[0][2]],population[new_list[0][3]]))),dfy['pct_chg']))

score2 = []

# 第二代进化
# for i in new_list:
#     for keo in function_LastSet:
#         score2.append([fitness(keo(i[1](i[2], i[3])), dfy['pct_chg'])])
#
# print(score2)
# new_list2 = eliminate_half(score2)
# print(new_list2)
# # 迭代遗传规划算法
# for generation in range(num_generations):
#     # 计算适应度分数
#     fitness_scores = [fitness(individual) for individual in population]
#
#     # 选择一组父代
#     parents = []
#     for i in range(2):
#         parent_index = fitness_scores.index(max(fitness_scores))
#         parent = population[parent_index]
#         parents.append(parent)
#         fitness_scores[parent_index] = -1
#
#     # 使用遗传操作创建一组子代
#     children = []
#     for i in range(population_size - 2):
#         child1, child2 = crossover(random.choice(parents), random.choice(parents))
#         child1 = mutation(child1)
#         child2 = mutation(child2)
#         children.append(child1)
#         children.append(child2)
#
#     # 替换种群中的最劣个体
#     fitness_scores = [fitness(individual) for individual in population]
#     min_fitness_index = fitness_scores.index(min(fitness_scores))
#     population[min_fitness_index
