import requests
import json
import tkinter as tk

apikey = '9d745279179e47f3870202358232212'
url = "http://api.weatherapi.com/v1/current.json?key=" + apikey + "&q="


def weather(city):
    try:
        r = requests.get(url + city)
        wea = json.loads(r.text)
        return wea

    except Exception as e:
        print(e)
        print("Something error occurred..")
        print("Please try again later..")
        exit()


def display_weather():
    city = city_entry.get()
    data = weather(city)

    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, f"\n\t--The Current Weather Update for the City: {city} is--\n\n")
    result_text.insert(tk.END, f"\tName: {data['location']['name']}\n")
    result_text.insert(tk.END, f"\tRegion: {data['location']['region']}\n")
    result_text.insert(tk.END, f"\tTz-ID: {data['location']['tz_id']}\n")
    result_text.insert(tk.END, f"\tCountry: {data['location']['country']}\n")
    result_text.insert(tk.END, f"\tLatitude: {data['location']['lat']}\n")
    result_text.insert(tk.END, f"\tLongitude: {data['location']['lon']}\n\n")

    result_text.insert(tk.END, f"\tLocal Time: {data['location']['localtime']}\n")
    result_text.insert(tk.END, f"\tLast Updated: {data['current']['last_updated']}\n\n")

    result_text.insert(tk.END, f"\tTemperature in Celsius: {data['current']['temp_c']}\n")
    result_text.insert(tk.END, f"\tTemperature in Fahrenheit: {data['current']['temp_f']}\n")
    result_text.insert(tk.END, f"\tDay(1)/Night(0): {data['current']['is_day']}\n\n")

    result_text.insert(tk.END, f"\tWind in Miles Per Hour: {data['current']['wind_mph']}\n")
    result_text.insert(tk.END, f"\tWind in Kilometer Per Hour: {data['current']['wind_kph']}\n")
    result_text.insert(tk.END, f"\tWind Direction: {data['current']['wind_dir']}\n")
    result_text.insert(tk.END, f"\tWind Direction in Degrees: {data['current']['wind_degree']}\n")
    result_text.insert(tk.END, f"\tHumidity: {data['current']['humidity']}\n")


root = tk.Tk()
root.title("Weather App")
city_label = tk.Label(root, text="Enter the name of the city: ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather, bg="#4caf50", fg="black")
get_weather_button.pack()

result_text = tk.Text(root, height=23, width=70)
result_text.pack()

root.mainloop()
