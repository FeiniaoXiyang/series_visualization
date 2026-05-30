# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:02:16 2026

@author: xfq
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from streamlit_audio_recorder import audio_recorder

# 页面设置
st.title("语音频率分析工具")
st.write("点击下方麦克风录制'今天天气不错'，分析后显示频率频谱图")

# 调用浏览器录音（云端可用）
audio_bytes = audio_recorder(
    text="点击麦克风录音",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone-lines",
    icon_size="3x"
)

if audio_bytes:
    # 保存录音为临时WAV文件
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_bytes)
    
    # 读取WAV文件的采样率和音频数据
    sampling_rate, audio_data = read("temp_audio.wav")
    audio_data = audio_data.astype(np.float32)  # 转成float格式

    # 傅里叶变换（时域转频域）
    n = len(audio_data)
    yf = np.fft.fft(audio_data)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)

    # 只取正频率部分
    positive_mask = xf >= 0
    xf_positive = xf[positive_mask]
    yf_positive = np.abs(yf[positive_mask])

    # 绘制频谱图
    st.subheader("语音频率频谱图")
    plt.figure(figsize=(10, 4))
    plt.plot(xf_positive, yf_positive)
    plt.xlabel("频率 (Hz)")
    plt.ylabel("振幅")
    plt.xlim(0, 5000)  # 人声主要频率范围
    plt.grid(True)
    st.pyplot(plt)

    st.info("图中峰值对应声音的主要频率（人声基频一般在100-500Hz）")