import pandas as pd
import geopandas as gpd
import json
import plotly.express as px


df = pd.read_csv('berlin_weather_forecast.csv') 
df['date'] = pd.to_datetime(df['date'].astype(str))
df_gb = df.groupby(['name','year','week'])['predicted_tempreature'].mean().reset_index()
df_gb['predicted_tempreature'] = df_gb['predicted_tempreature'].round(2)
#df_gb['predicted_tempreature'] = df_gb['predicted_tempreature']*100
#df_gb['predicted_tempreature'].min(), df_gb['predicted_tempreature'].max() ### (-235.0, 2186.0)
df_gb = df_gb[df_gb['year']>= 2021]
df_gb = df_gb[df_gb['week']<= 10]


filename = "berlin_bezirke.geojson"
file = open(filename)
geo_json_file = gpd.read_file(file)
json_file = geo_json_file.to_json()
converted_json = json.loads(json_file)


interactive_map = px.choropleth_mapbox(
    mapbox_style = 'open-street-map',
    data_frame = df_gb,
    geojson = converted_json,
    featureidkey = 'properties.name',
    locations = 'name', 
    color = 'predicted_tempreature',
    center = {"lat": 52.5200, "lon": 13.4050},
    zoom = 10,
    animation_frame = 'week',
    animation_group = 'name',   
    color_continuous_scale = "thermal",
    range_color = (-2.35, 22),
    color_continuous_midpoint = 12,
    title = "Predicted Weekly Average Tempratures for each Berlin District. The period is from the 1st week of January 2021 to the 1st week of March 2021.")

interactive_map.write_html("berlin_interactive_map.html", include_plotlyjs='cdn')

