import folium
import pandas as pd
m = folium.Map()

iraq = folium.Map(location = [33.330202,44.456559],zoom_start=5.5)

final_data = pd.read_csv("C:/2.csv")
final_data['State'] = final_data['code']
final_data['Death'] = final_data['Deaths'].astype(str)
final_data['Conf'] = final_data['Confirmed'].astype(str)

final_data['Total cases'] = final_data['Cumulative_Cases'].astype(str)

for state,lat,long,total_cases,Death,Conf,Date in zip(list(final_data['State']),list(final_data['Latitude']),list(final_data['Longitude']),list(final_data['Total cases']),list(final_data['Death']),list(final_data['Conf']),list(final_data['Date'])):
    folium.CircleMarker(location = [lat,long],
                       radius = 9,
                       color='red',
                       fill = True,
                       fill_color="red").add_to(iraq)
    folium.Marker(location = [lat,long],
              popup='<strong><b>' +Date+'</strong> <br>' +
              '<strong><b>Province : ' +state+'</strong> <br>' + 
              '<strong><b>Cumulative Cases : ' +total_cases+'</strong> <br>' +
              '<strong><b>Confirmed : ' +Conf+'</strong> <br>' +
              '<strong><b>Deaths : ' +Death+ '</strong> <br>').add_to(iraq)

iraq.save('C:/project/Covid_19_staticics/output/Covid Statistics.html')