import pandas as pd
import numpy as np
from datetime import date
from sktime.base import BaseEstimator
from sktime.forecasting.base import ForecastingHorizon

def get_forecast(fd: date, fh: int, df: pd.DataFrame, model: BaseEstimator) -> pd.DataFrame:

    # Get observed data
    y_observed = df.loc[df.index < fd, ['power']]
    X_observed = df.loc[df.index < fd].drop('power', axis=1)

    # Update model with observed data
    model.update(y_observed, X_observed, update_params=False)

    # Get true target for forecasting horizon
    y_true = df.loc[fd:].head(fh)[['power']]

    # Convert fh to sktime class for predict method
    # Edge case: fh cuts-off to available data only
    fh_sktime = ForecastingHorizon(np.arange(min(fh, y_true.shape[0])) + 1, is_relative=True)

    # Get forecast target for forecasting horizon
    X_forecast = df.loc[fd:].head(fh).drop('power', axis=1)
    y_forecast = model.predict(fh_sktime, X_forecast)

    # Put together in a dataframe
    df_forecast = pd.concat([y_observed.tail(fh*7), y_true, y_forecast], axis=1)
    df_forecast.columns = ['observed', 'true', 'forecast']

    return df_forecast