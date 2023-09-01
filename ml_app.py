# -*- coding utf-8 -*-

import streamlit as st
import joblib
import os
import numpy as np

def run_ml_app():
    st.subheader("Machine Learning Page")
    
    # layout
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("수치입력")
        sepal_length = st.select_slider("Sepal Length", options = np.arange(1,11))
        sepal_width = st.select_slider("Sepal Width", options = np.arange(1,11))
        petal_length = st.select_slider("Petal Length", options = np.arange(1,11))
        petal_width = st.select_slider("Petal Width", options = np.arange(1,11))

        sample_list = [sepal_length, sepal_width, petal_length, petal_width]
        st.write(sample_list)

    with col2:
        st.subheader("모델 결과를 확인하셈요")

        # 모델 불러오기
        model_file = "models/lgr_model_iris230901.pkl"
        model = joblib.load(open(os.path.join(model_file), "rb"))
        st.write(model)