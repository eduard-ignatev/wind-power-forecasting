import pandas as pd
from sktime.performance_metrics.forecasting import mean_absolute_error, mean_squared_error, mean_absolute_scaled_error

def get_metrics(df_forecast: pd.DataFrame) -> dict:
    metrics = dict()

    metrics['mae'] = mean_absolute_error(
        y_true=df_forecast['true'].dropna(), 
        y_pred=df_forecast['forecast'].dropna())

    metrics['rmse'] = mean_squared_error(
        y_true=df_forecast['true'].dropna(), 
        y_pred=df_forecast['forecast'].dropna(), 
        square_root=True)

    metrics['mase'] = mean_absolute_scaled_error(
        y_true=df_forecast['true'].dropna(), 
        y_pred=df_forecast['forecast'].dropna(), 
        y_train=df_forecast['observed'].dropna())
    
    return metrics