# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:21:17 2026

@author: xfq
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# 改用Windows默认的“微软雅黑”字体
plt.rcParams["font.family"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

st.title("泰勒级数的局部逼近演示")

x = np.linspace(-3, 3, 1000)
original_function = np.sin(x)  

n_terms = st.slider("选择泰勒展开项数", 1, 10, 2)

taylor_sum = 0
for i in range(n_terms):
    sign = (-1) ** i
    exponent = 2 * i + 1
    term = sign * (x ** exponent) / np.math.factorial(exponent)
    taylor_sum += term

plt.figure(figsize=(10, 6))
plt.plot(x, original_function, label="原函数 sin(x)", color='blue', linewidth=2)
plt.plot(x, taylor_sum, label=f"{n_terms}项泰勒展开", color='red', linestyle='--', linewidth=2)
plt.axvline(x=0, color='gray', linestyle=':')  
plt.xlabel("x值")
plt.ylabel("函数值")
plt.legend()
plt.title("泰勒级数：离展开点越近，逼近效果越好")
st.pyplot(plt)