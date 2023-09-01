# -*- coding utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib 
import scikitlearn
import plotly

def main():

    st.markdown("# Hello World")
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(sns.__version__)
    st.write(matplotlib.__version__)
    st.write(scikitlearn.__version__)
    st.write(plotly.__version__)

if __name__=="__main__":
    main()