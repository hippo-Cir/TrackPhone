import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode



pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,'fr')
print(location)
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,'fr'))

key='your key'
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
#print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker(location=[lat, lng], popup=location).add_to(myMap)

myMap.save('mylocation.html')
