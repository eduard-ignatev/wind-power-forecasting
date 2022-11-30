# Wind Power Forecasting

This is a wind power forecasting application using machine learning algorithms for day-ahead energy trading.

[![Wind Power Forecasting Streamlit App](https://user-images.githubusercontent.com/97912967/204868421-0840f34c-90c3-4347-8fba-05b4850cd507.png)](https://wind-power-forecasting.streamlit.app/)

## Why?

My initial motivation was to explore the topic of time series analysis and forecasting through practice. I picked the wind power forecasting from a vast amount of challenges in energy domain related to time series. A power output of a specific wind farm is quite intermittent in nature, therefore it is really important for assets owner or energy trader to have an accurate prediction to participate in a day-ahead market. I later decided to set up a simple web application for demonstration purposes.

## Assumptions
- Dataset: [Kelmarsh Wind Farm Data](https://zenodo.org/record/7212475)  
- Turbine №5 is used for analysis
- Train data: [2019.01.01 - 2021.03.26]  
- Validation: [2021.03.27 - 2021.03.31]  
- Demo data: [2021.04.01 - 2021.06.30]  
- ERA5 weather data is taken as historical weather forecasts
- The turbine forced downtime is known in advance

## Usage
To reproduce results in `Kelmarsh_data_analysis.ipynb` notebook you need to download the dataset and put the following files in the data folder:
```
├── data
│   ├── Kelmarsh_era5.csv
│   ├── Status_Kelmarsh_5_2019-01-01_-_2020-01-01_232.csv
│   ├── Status_Kelmarsh_5_2020-01-01_-_2021-01-01_232.csv
│   ├── Status_Kelmarsh_5_2021-01-01_-_2021-07-01_232.csv
│   ├── Turbine_Data_Kelmarsh_5_2019-01-01_-_2020-01-01_232.csv
│   ├── Turbine_Data_Kelmarsh_5_2020-01-01_-_2021-01-01_232.csv
│   └── Turbine_Data_Kelmarsh_5_2021-01-01_-_2021-07-01_232.csv
```
