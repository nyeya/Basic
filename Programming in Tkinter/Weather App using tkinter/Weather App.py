from tkinter import *
import requests
from datetime import datetime as dt
import json
root = Tk() # Creates the Window Object
root.title("Weather App - Nyeya") # Give the window a title
root.resizable(width=False,height=False)
# This function gets the weather data from WeatherMap and displays the results in a readable format
def getWeather():
  city_name = city_ent.get()
  API_KEY = "c6s982sdf98998rfads9fw8fsdf98323" #REPLACE THIS VALUE WITH YOUR API KEY.
  weather_url =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
  try:
    results=requests.get(weather_url).json()
  except:
    results={"cod":0}
  display_output.delete("1.0","end")
  if results['cod']==200:
    zone = results['timezone']
    sun_set = results['sys']['sunset']
    sun_rise = results['sys']['sunrise']
    print(results)
    #display_output.insert("1.0",results['cod'])
    output = f"""
Location: {city_name}, {results['sys']['country'].upper()}
          Latitude: {results['coord']['lat']}
          Longitude: {results['coord']['lon']}
Current Conditions:
    Current temperature: {int(results['main']['temp']) - 273}° ({results['main']['temp']}K)
    Weather: {results['weather'][0]['description']}
    Humidity: {results['main']['humidity']}%
    Wind: {results['wind']['speed'] * 3.6:.2}km/h
Additional Info:
    Timezone: {zone}
    Sunrise: {dt.utcfromtimestamp(zone+sun_rise).time()}
    Sunset: {dt.utcfromtimestamp(zone + sun_set).time()}
    """
    display_output.insert("1.0",output)
  elif results['cod']=='404':
    display_output.insert("1.0","City not found")
  else:
    display_output.insert("1.0","Connect to the internet")
#Creating and Packing a label box for City
city_lbl = Label(root,text="Enter City Name",pady=10)
city_lbl.grid(row=0,column=0)

#Creating an entry box to receive name of city, then pack it in the window
city_ent = Entry(root,bg="#bbb",fg="black")
city_ent.grid(row=0,column=1,padx=10)

#Creating a get weather button to get the weather information using the api
display_btn = Button(root,text="Get Weather Info",bg="blue",fg="white",command=getWeather)
display_btn.grid(row=1,column=0,columnspan=2,sticky=EW,pady=10,padx=10)

# Creating a label with text 'Your Results Here'
results_lbl = Label(root,text="Your Output:")
results_lbl.grid(row=2,column=0,columnspan=2)
# Creating the display area using Text() and packing it on screen
display_output = Text(root,bg="darkgrey",fg="white",height=15,width=50)
display_output.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
