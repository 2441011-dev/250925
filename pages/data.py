import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 폰트 경로 지정 및 설정
font_path = '/workspaces/250925/fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False
st.subheader('Matplotlib 예시 (한글 폰트 적용)')
fig, ax = plt.subplots()
ax.plot(df['A'], label='A')
ax.plot(df['B'], label='B')
ax.set_title('예시 라인 그래프')
ax.set_xlabel('인덱스')
ax.set_ylabel('값')
ax.legend()
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np

st.title('간단한 데이터 시각화 예시')

# 임의의 데이터 생성
df = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['A', 'B', 'C']
)

st.subheader('Line Chart')
st.line_chart(df)

st.subheader('Bar Chart')
st.bar_chart(df)
