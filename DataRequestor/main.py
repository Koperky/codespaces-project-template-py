from time import sleep
#from snap7.server import mainloop
import requests
lat = 0
lng = 0

res = requests.get("https://api.openaq.org/v2/measurements?location_id=10566&parameter=no2&parameter=co&parameter=o3&parameter=so2&parameter=pm10&parameter=pm25&parameter=bc&date_from=2023-11-07T10:19:10+01:00&date_to=2023-11-08T10:19:10+01:00&limit=1000").json()

#https://docs.openaq.org/docs/getting-started
def Check_stations():
    lat = input("podaj szerokos geograficzna szukanych stacji: ")
    lng = input("podaj dlugosc geograficzna szukanych stacji")






while (True):
    print(res['results'][8]['location'])
    print(res['results'][8]['parameter'],"=",res['results'][8]['value'],res['results'][8]['unit'])

    sleep(2)


