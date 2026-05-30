# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:02:16 2026

@author: xfq
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from streamlit_mic_recorder import mic_recorder

# 页面设置
st.title("语音频率分析工具")

# 调用麦克风录音（云端兼容）
audio = mic_recorder(
    start_prompt="点击开始录音（说'今天天气不错'）",
    stop_prompt="点击停止",
    key="recorder"
)

if audio:
    # 保存录音
    with open("temp.wav", "wb") as f:
        f.write(audio['bytes'])
    
    # 读取音频数据
    sr, data = read("temp.wav")
    data = data.astype(np.float32)
    
    # 傅里叶变换
    n = len(data)
    yf = np.fft.fft(data)
    xf = np.fft.fftfreq(n, 1/sr)
    xf_pos = xf[xf >= 0]
    yf_pos = np.abs(yf[xf >= 0])
    
    # 画图
    st.subheader("频率频谱图")
    plt.figure(figsize=(10,4))
    plt.plot(xf_pos, yf_pos)
    plt.xlim(0, 5000)
    plt.xlabel("频率(Hz)")
    plt.ylabel("振幅")
    st.pyplot(plt)