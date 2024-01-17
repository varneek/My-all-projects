import tkinter as tk 
import requests
from tkinter import messagebox


api_key = '4a29ff08445ca33653d638a16b3e7911'


def get_weather(city):
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    if data:
        city = data.json()['name']
        country = data.json()['sys']['country']
        weather = data.json()['weather'][0]['main']
        temp = data.json()['main']['temp']
        temp = round(temp - 273.15, 2)
        icon = data.json()['weather'][0]['icon']
        result = (city, country, weather, temp, icon)
        return result


def search():
    city = main_city.get()
    weather = get_weather(city)
    if weather:
        location['text'] = f'{weather[0]}, {weather[1]}'
        main_weather['text'] = f'{weather[2]}'
        main_temp['text'] = f'{weather[3]}°C'
        image['image'] = f'E:/code/weather_app/icons/{weather[4]}.png'
        
    else:
        messagebox.showerror('Error', f'{city} city not found')
        

app = tk.Tk()
app.title('Weather app')
app.geometry('600x350')

main_city = tk.StringVar()
city_entry = tk.Entry(app, textvariable=main_city, width=30)
city_entry.pack()

search_bt = tk.Button(app, text='search weather', width= 15, command= search)
search_bt.pack()

location = tk.Label(app, text='', font=('bold', 20))
location.pack()

image = tk.Label(app, image='')
image.pack(padx=20,pady=30)

main_temp = tk.Label(app, text='', font=('bold'))
main_temp.pack()

main_weather = tk.Label(app, text='', font=('bold'))
main_weather.pack()


app.mainloop()