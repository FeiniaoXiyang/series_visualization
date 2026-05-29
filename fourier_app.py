# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:07:58 2026

@author: xfq
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 加载本地的微软雅黑字体
plt.rcParams['font.sans-serif'] = ['msyh.ttc']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

st.title("傅里叶级数的周期分解演示")

# 生成x轴数据（覆盖4个周期）
x = np.linspace(0, 8 * np.pi, 1000)

# 定义周期方波信号
def square_wave(x):
    # 0到π区间值为1，π到2π区间值为-1，循环重复
    return np.where(np.mod(x, 2*np.pi) < np.pi, 1, -1)

original_wave = square_wave(x)

# 学生可操作的滑块：选择叠加的正弦波数量
n_harmonics = st.slider("选择叠加的正弦波个数", 1, 20, 3)

# 计算傅里叶级数（方波的傅里叶展开是奇数谐波的叠加）
fourier_sum = 0
for k in range(1, n_harmonics + 1, 2):
    # 方波的傅里叶级数公式：4/π * (sinx + sin3x/3 + sin5x/5 + ...)
    term = (4 / np.pi) * (1 / k) * np.sin(k * x)
    fourier_sum += term

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, original_wave, label="原信号（方波）", color='blue', linewidth=2)
plt.plot(x, fourier_sum, label=f"{n_harmonics}个正弦波叠加", color='green', linestyle='--', linewidth=2)
plt.xlabel("x值（时间）")
plt.ylabel("信号强度")
plt.legend()
plt.title("傅里叶级数：叠加的周期波越多，越接近原周期信号")
st.pyplot(plt)