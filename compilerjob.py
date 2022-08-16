import pandas as pd
import folium

# imports dataset from google sheets which contains the data for the Total Energies stations that use WiCodes
url = 'https://docs.google.com/spreadsheets/d/1Wl2gNBVNpQPgwG0Dl6akGxsIjdrMxerpct7jYSpuVQE/edit#gid=0'.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url)

# add google maps direction link to the dataframe
df['Google Maps Direction'] = 'https://www.google.com/maps/dir/?api=1&destination=' + df['Address'] +'&travelmode=driving'

# creates a map of the Total Energies stations that use WiCodes
map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)

# adds a marker for each station
for lat, lon, data in zip(df['Latitude'], df['Longitude'], '<h4>'+df['Store Name']+"</h4>\n"+df['Address']+'<br><a href="'+df['Google Maps Direction']+'">Get Directions</a>'):
    #make red petrol station marker
    folium.Marker([lat, lon]
    , popup=data,
    icon=folium.features.CustomIcon('3448636.png', icon_size=(35, 35))   
        ).add_to(map)

map.save('index.html')