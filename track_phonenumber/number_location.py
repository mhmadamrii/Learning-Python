import phonenumbers

import folium

from my_number import number

from phonenumbers import geocoder

Key = '87dc059675ce4d1c8c91c806039ce7f5'

san_number = phonenumbers.parse(number)

your_location = geocoder.description_for_number(san_number, 'en')
print(your_location)

## get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(your_location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

my_map = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng], popup= your_location).add_to((my_map))

## save map in html file
my_map.save("myLocation.html")