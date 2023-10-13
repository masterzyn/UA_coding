#!  /usr/bin/env python3

#importing folium in order to make the U.S map as well as dealing with markers
import folium

#importing pandas to read my excell file
import pandas as pd

#importing geopy in order to take a state name and turn it into latitude and longitude cordinates
from geopy.geocoders import Nominatim

#initilizing the map to be centered on the U.S
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

#my function to get the cordinates from a state input
def get_cords(state):

    #intializing Nominatim
    geolocator = Nominatim(user_agent="Myapp")

    #setting location equal to a geocode of our state that is in the U.S
    location = geolocator.geocode(state + ", USA")
    if location is not None:

        #returning the tuple of latitude and longitude
        return location.latitude, location.longitude
    else:
        return None, None
    

#using pandas to read our excel file
df = pd.read_excel('I-EDA_draft.xlsx', sheet_name='May_2022')

#creating an empty list to put in our data scientist info
data_science_data = []

#making for loop to get all of the information that we want into our list
for index, row in df.iterrows():

    #checks if the row shows data for a data scientist
    if row["OCC_TITLE"] == "Data_science":

        #if the data is for data science then it takes the job name the state where they cam from and also
        #an information section which will be put in the marker on the map
        job_info = {
            "Job": row['OCC_TITLE'],
            'Info': f'Data Scientists make {row["A_MEAN"]} on average in {row["AREA_TITLE"]}',
            'State': row['AREA_TITLE']
        }
        #it then appends all of that information to our list
        data_science_data.append(job_info)
    else:
        continue

#this for loop is what puts the markers on the map itself
for i in data_science_data:

    #using our get_cords function to get the cordinates of the state that the job belongs to
    lat, long = get_cords(i['State'])

    #using folium to make a marker on the map at the state to which the job belongs
    folium.Marker(location=[lat, long],
                  
                  #this adds the state name whenever you hover over the icon on the map
                  tooltip=i['State'], 

                  #actually adds the marker to the map with the .add_to
                  popup=f"{i['Info']}").add_to(us_map)

#saves the map to map_us.html
us_map.save('map_us.html')