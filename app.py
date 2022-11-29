import streamlit as st
import plotly.express as px

from datetime import datetime
from utils.model_dict import model_dict
from utils.data_loader import load_data
from utils.model_loader import load_model
from utils.forecaster import get_forecast
from utils.metrics_calc import get_metrics

st.set_page_config(page_title = "Wind Power Forecasting", page_icon="🌀", layout="wide")

st.title('Wind Power Forecasting 🌀')
st.markdown(
    '''
    Wind power forecasting using machine learning for day-ahead energy trading.  
    Dataset: [Kelmarsh Wind Farm Data](https://zenodo.org/record/7212475)
    '''
)

# Sidebar controls
st.sidebar.markdown('')
st.sidebar.header('Controls')
model_name = st.sidebar.radio(
    'Select model', 
    options=model_dict.keys(), 
    index=7)
fd = st.sidebar.slider(
    'Forecast date', 
    min_value=datetime(2021, 4, 1), 
    max_value=datetime(2021, 6, 30), 
    value=datetime(2021, 5, 1))
fh = st.sidebar.slider(
    'Forecast horizon (hours)', 
    min_value=1, 
    max_value=168, 
    value=24) * 6 # in relative periods

# Sidebar links
st.sidebar.header('Links')
st.sidebar.markdown('[GitHub repository](https://github.com/eduard-ignatev/wind-power-forecasting/)')
st.sidebar.markdown('[LinkedIn profile](https://www.linkedin.com/in/eduard-ignatev-601334120/)')

# Load data
df = load_data()

# Load model
model = load_model(model_dict[model_name])

# Get forecast
df_forecast = get_forecast(fd, fh, df, model)

# Plot graphs
fig = px.line(df_forecast, labels={'index': '', 'value': 'Power (kW)'})
st.plotly_chart(fig)

# Show metrics
metrics = get_metrics(df_forecast)
col1, col2, col3, col4, col5 = st.columns(5)
col2.metric(label='MAE', value=round(metrics['mae'], 2))
col3.metric(label='RMSE', value=round(metrics['rmse'], 2))
col4.metric(label='MASE', value=round(metrics['mase'], 2))