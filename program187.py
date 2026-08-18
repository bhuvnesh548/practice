import requests
city=input("enter a city : ")
url=f"https://wttr.in/{city}?format=3"
response=requests.get(url)
if response.status_code==200:
    print(response.text)
else:
    print("could not fetch weather data")