# 因子库
import numpy as np
import pandas as pd


def Macd(df, fast=12, slow=26, signal=9):
    ema_fast = df['close'].ewm(span=fast, min_periods=fast).mean()
    ema_slow = df['close'].ewm(span=slow, min_periods=slow).mean()
    df['dif'] = ema_fast - ema_slow
    # print(df['dif'])
    df['dea'] = df['dif'].ewm(span=signal, min_periods=signal).mean()
    df['macd'] = (df['dif'] - df['dea']) * 2
    # macd_rank = df['macd'].rolling(window=14).apply(lambda x: (x[-1] - np.min(x)) / (np.max(x) - np.min(x)))
    return df['macd'], df['dea'], df['dif']


def Cci(df, n, c=0.015):
    typical_price = (df['high'] + df['low'] + df['close']) / 3
    mean_deviation = np.abs(typical_price - typical_price.rolling(n).mean()).rolling(n).mean()
    df['cci'] = (typical_price - typical_price.rolling(n).mean()) / (c * mean_deviation)
    # cci_rank = df['cci'].rolling(window=14).apply(lambda x: (x[-1] - np.min(x)) / (np.max(x) - np.min(x)))
    clean_data = df['cci'].dropna()
    return clean_data

def calculate_RVI(df, n1=10, n2=10):
    # 读取csv文件数据

    # 定义函数计算上升波动率（UM）和下降波动率（DM）
    def UM(price, n):
        um = pd.Series(np.where(price > price.shift(1), price - price.shift(1), 0))
        return um.rolling(n).std()

    def DM(price, n):
        dm = pd.Series(np.where(price < price.shift(1), price.shift(1) - price, 0))
        return dm.rolling(n).std()

    # 定义函数计算相对强弱指标（RVI）
    def RVI(price, n1, n2):
        um = UM(price, n1)
        dm = DM(price, n1)
        rvi = um.rolling(n2).mean() / (um.rolling(n2).mean() + dm.rolling(n2).mean())
        return rvi * 100

    # 计算相对强弱指标（RVI）
    return RVI(df['close'], n1, n2)



def liangbi(df):
    return np.log(df['close']) / np.log(df['vol'])

def alpha1(df):
    return ((df['high']+df['low'])/df['close']).rolling(5).mean()

def alpha2(df):
    return (df['low']+df['vol'])


def relative_strength_index(data, n=14):
    """
    计算n日相对强弱指标
    :param data: 股价序列，DataFrame类型，包含'close'列
    :param n: RSI周期
    :return: RSI序列，np.array类型
    """
    close = data['close'].values
    deltas = np.diff(close)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = 0
    if down != 0:
        rs = up / down
    rsi = np.zeros_like(close)
    rsi[:n] = 100. - 100. / (1. + rs)
    for i in range(n, len(close)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n
        rs = 0
        if down != 0:
            rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)
    return rsi


def moving_average(data, n):
    """
    计算n日移动平均线
    :param data: 股价序列，list或np.array类型
    :param n: 移动平均线周期
    :return: 移动平均线序列，np.array类型
    """
    weights = np.ones(n) / n
    return np.convolve(data, weights, mode='valid')


def bollinger_bands(data, n=20, k=2):
    """
    计算n日布林带
    :param data: 股价序列，list或np.array类型
    :param n: BB周期
    :param k: BB系数
    :return: 布林带上下轨序列，np.array类型
    """
    sma = moving_average(data, n)
    std = np.std(data[-n:])
    upper_band = sma + k * std
    lower_band = sma - k * std
    return upper_band, lower_band
