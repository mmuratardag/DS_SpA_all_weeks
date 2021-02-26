
import numpy as np
import pandas as pd
from fbprophet import Prophet


Charlottenburg_Wilmersdorf = pd.read_csv('DFs/TG_Charlottenburg-Wilmersdorf.txt', sep=",", header=0)
Friedrichshain_Kreuzberg = pd.read_csv('DFs/TG_Friedrichshain-Kreuzberg.txt', sep=",", header=0)
Lichtenberg = pd.read_csv('DFs/TG_Lichtenberg.txt', sep=",", header=0)
Marzahn_Hellersdorf = pd.read_csv('DFs/TG_Marzahn-Hellersdorf.txt', sep=",", header=0)
Mitte = pd.read_csv('DFs/TG_Mitte.txt', sep=",", header=0)
NeuKoln = pd.read_csv('DFs/TG_NeuKoln.txt', sep=",", header=0)
Pankow = pd.read_csv('DFs/TG_Pankow.txt', sep=",", header=0)
Reinickendorf = pd.read_csv('DFs/TG_Reinickendorf.txt', sep=",", header=0)
Spandau = pd.read_csv('DFs/TG_Spandau.txt', sep=",", header=0)
Steglitz_Zehlendorf = pd.read_csv('DFs/TG_Steglitz-Zehlendorf.txt', sep=",", header=0)
Tempelhof_Schoeneberg = pd.read_csv('DFs/TG_Tempelhof-Schoeneberg.txt', sep=",", header=0)
Treptow_Koepenick = pd.read_csv('DFs/TG_Treptow-Koepenick.txt', sep=",", header=0)


def trans_df(df):
    df = df.copy()
    df['DATE'] = pd.to_datetime(df['DATE'].astype(str))
    df['TG'].replace(to_replace = -9999, value = np.nan, inplace=True)
    df.dropna(inplace=True)
    df['TG'] = df['TG']*0.1
    df = df[df['DATE'] >= 'January 1961'].copy()
    df = df[['DATE', 'TG']]
    df = df.rename(columns={"DATE": "ds", "TG": "y"})
    return df


Charlottenburg_Wilmersdorf = trans_df(Charlottenburg_Wilmersdorf)
Friedrichshain_Kreuzberg = trans_df(Friedrichshain_Kreuzberg)
Lichtenberg = trans_df(Lichtenberg)
Marzahn_Hellersdorf = trans_df(Marzahn_Hellersdorf)
Mitte = trans_df(Mitte)
NeuKoln = trans_df(NeuKoln)
Pankow = trans_df(Pankow)
Reinickendorf = trans_df(Reinickendorf)
Spandau = trans_df(Spandau)
Steglitz_Zehlendorf = trans_df(Steglitz_Zehlendorf)
Tempelhof_Schoeneberg = trans_df(Tempelhof_Schoeneberg)
Treptow_Koepenick = trans_df(Treptow_Koepenick)


def make_forecast_with_prophet(df):
    m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
    m.fit(df)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    #forecast = forecast[forecast['ds'] >= 'March 2020'].copy()
    forecast = forecast[['ds', 'yhat']]
    forecast = forecast.rename(columns={"ds": "date", "yhat": "predicted_tempreature"})
    return forecast


Charlottenburg_Wilmersdorf_forecast = make_forecast_with_prophet(Charlottenburg_Wilmersdorf)
Friedrichshain_Kreuzberg_forecast = make_forecast_with_prophet(Friedrichshain_Kreuzberg)
Lichtenberg_forecast = make_forecast_with_prophet(Lichtenberg)
Marzahn_Hellersdorf_forecast = make_forecast_with_prophet(Marzahn_Hellersdorf)
Mitte_forecast = make_forecast_with_prophet(Mitte)
NeuKoln_forecast = make_forecast_with_prophet(NeuKoln)
Pankow_forecast = make_forecast_with_prophet(Pankow)
Reinickendorf_forecast = make_forecast_with_prophet(Reinickendorf)
Spandau_forecast = make_forecast_with_prophet(Spandau)
Steglitz_Zehlendorf_forecast = make_forecast_with_prophet(Steglitz_Zehlendorf)
Tempelhof_Schoeneberg_forecast = make_forecast_with_prophet(Tempelhof_Schoeneberg)
Treptow_Koepenick_forecast = make_forecast_with_prophet(Treptow_Koepenick)


Charlottenburg_Wilmersdorf_forecast['name'] = "Charlottenburg-Wilmersdorf"
Friedrichshain_Kreuzberg_forecast['name'] = "Friedrichshain-Kreuzberg"
Lichtenberg_forecast['name'] = "Lichtenberg"
Marzahn_Hellersdorf_forecast['name'] = "Marzahn-Hellersdorf"
Mitte_forecast['name'] = "Mitte"
NeuKoln_forecast['name'] = "Neukölln"
Pankow_forecast['name'] = "Pankow"
Reinickendorf_forecast['name'] = "Reinickendorf"
Spandau_forecast['name'] = "Spandau"
Steglitz_Zehlendorf_forecast['name'] = "Steglitz-Zehlendorf"
Tempelhof_Schoeneberg_forecast['name'] = "Tempelhof-Schöneberg"
Treptow_Koepenick_forecast['name'] = "Treptow-Köpenick"


berlin_forecast = pd.concat([Charlottenburg_Wilmersdorf_forecast,
                             Friedrichshain_Kreuzberg_forecast,
                             Lichtenberg_forecast,
                             Marzahn_Hellersdorf_forecast,
                             Mitte_forecast,
                             NeuKoln_forecast,
                             Pankow_forecast,
                             Reinickendorf_forecast,
                             Spandau_forecast,
                             Steglitz_Zehlendorf_forecast,
                             Tempelhof_Schoeneberg_forecast,
                             Treptow_Koepenick_forecast
                            ]).reset_index().drop(columns=['index'])
berlin_forecast['predicted_tempreature'] = berlin_forecast['predicted_tempreature'].round(2)

berlin_forecast['year'] = berlin_forecast['date'].dt.year
berlin_forecast['week'] = berlin_forecast['date'].dt.isocalendar().week
berlin_forecast = berlin_forecast[['date','year','week','name','predicted_tempreature']]

berlin_forecast.to_csv('berlin_weather_forecast.csv', index=False)
