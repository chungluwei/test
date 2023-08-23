import numpy as np
import pandas as pd
import streamlit as st

st.title("測試numpy/pandas")
if"a" not in st.session_state:
    st.session_state.a=np.array([89,71,96,77,59,30,90])
b=st.number_input("輸入成績:",key="num_b")

if st.button:
    st.session_state.a=np.append(st.session_state.a,b)
    st.write(st.session_state.a)