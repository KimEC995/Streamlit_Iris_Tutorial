# -*- coding utf-8 -*-

import streamlit as st


def main():
    st.markdown("# Hello World")

    menu=["Home", "탐색적 자료 분석", "머신러닝", "About"]
    choice = st.sidebar.selesctbox("메뉴",menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "탐색적 자료 분석":
        st.subheader("탐색적 자료 분석")
    elif choice == "머신러닝":
        st.subheader("머신러닝")
    else:
        pass
    

if __name__=="__main__":
    main()