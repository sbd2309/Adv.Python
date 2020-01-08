from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
geolocator = Nominatim()
time.sleep(5)
city1=input("Enter City: ")
location = geolocator.geocode(city1)
#print((location.latitude, location.longitude))
x=location.latitude, location.longitude
#print (x)
city2=input("Enter Another City: ")
geolocator = Nominatim()
location = geolocator.geocode(city2)
y=location.latitude, location.longitude
#print (y)
print("The distance between {} {} is {} KM".format(city1,city2,geodesic(x,y).kilometers))



