# -*- coding utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib 
import sklearn
import plotly

def main():

    st.markdown("# Hello World")
    st.write("Numpy:", np.__version__)
    st.write("Pandas:", pd.__version__)
    st.write("Seaborn:", sns.__version__)
    st.write("Matplotlib:", matplotlib.__version__)
    st.write("Sklearn:", sklearn.__version__)
    st.write("Plotly:", plotly.__version__)

if __name__=="__main__":
    main()