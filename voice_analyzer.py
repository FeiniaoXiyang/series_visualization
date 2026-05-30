# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:02:16 2026

@author: xfq
"""

import streamlit as st
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# 页面设置
st.title("语音频率分析工具")
st.write("点击下方按钮录制'今天天气不错'（录制3秒），分析后会显示频率频谱图")

# 录音参数
sampling_rate = 44100  # 采样率（Hz）
duration = 3  # 录音时长（秒）

# 录音按钮
if st.button("开始录音"):
    with st.spinner("正在录音...请说'今天天气不错'"):
        # 录制音频（单声道）
        audio_data = sd.rec(
            int(duration * sampling_rate),
            samplerate=sampling_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()  # 等待录音结束

    # 傅里叶变换：时域转频域
    n = len(audio_data)
    yf = np.fft.fft(audio_data.flatten())  # 对音频数据做FFT
    xf = np.fft.fftfreq(n, 1 / sampling_rate)  # 计算频率轴

    # 只取正频率部分（因为FFT结果对称）
    positive_mask = xf >= 0
    xf_positive = xf[positive_mask]
    yf_positive = np.abs(yf[positive_mask])  # 取振幅的绝对值

    # 绘制频谱图
    st.subheader("语音频率频谱图")
    plt.figure(figsize=(10, 4))
    plt.plot(xf_positive, yf_positive)
    plt.xlabel("频率 (Hz)")
    plt.ylabel("振幅")
    plt.xlim(0, 5000)  # 人声频率主要在0-5000Hz
    plt.grid(True)
    st.pyplot(plt)

    # 提示：图中峰值对应的频率就是声音的主要频率成分
    st.info("图中峰值越高，说明该频率的声音成分越强（人声基频一般在100-500Hz）")