import pandas as pd
import streamlit as st

@st.experimental_memo
def load_data() -> pd.DataFrame:
    # Load dataframe from pickle
    df = pd.read_pickle('data/df.pkl')
    df = df['2021-01-01 00:00:00':]
    return df