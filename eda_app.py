# -*- coding utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda_app():
    st.subheader("탐색적 자료분석 페이지")
    st.markdown("---")
    st.markdown("[마크다운추가하기](https://github.com/KimEC995)")
    st.subheader("잘 되는듯?")

    iris_df = pd.read_csv("data/iris.csv")

    st.dataframe(iris_df)