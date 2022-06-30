#Import required modules
from asyncio import events
import discord
from discord.ext import commands
import requests
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

#print that bot is connected, with the bot's name
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

####### OpenWeatherMap info (to be changed) ####### 
api_key = "YOURKEYHERE"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"


#The start commands
@bot.event
async def on_message(message):
    global messaged
    global guild
    msg = message.content

    if message.content.lower() == "!weather.test": 
        await message.channel.send("Testing 1, 2, 3.")

    elif message.content.lower().startswith("!weather"):
            x = message.content.split(" ", 4)
            city_name = x[1]
            if city_name == None:
                message.channe.send("You need to add a city name!")
            else:
                await weatherembed1(message, city_name)


#defining the start commands
async def weatherembed1(message, city_name):
            city_name1 = city_name
            print(city_name1)
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name1
            response = requests.get(complete_url)
            x = response.json()
            print(x)

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"] - 273.15
                feels_like = y["feels_like"] - 273.15
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                regenofdroog = x["weather"]
                z = x["weather"]
                weather_description = z[0]["description"]
                cloud_icon = z[0]["icon"]

                u = x["wind"]
                windspeed = u["speed"] * 3.6

                if '10d' == cloud_icon:   
                    r = (":cloud_rain: Make it possible that it's gonna to rain!")
                else:
                    r = (":cloud: You will stay dry atm!")

                if current_temperature > 18: 
                    x = (":hot_face: Some sweet temps!")
                else:
                    x = (":cold_face: Youre better off with some long pants today!")
                if current_temperature < 10: 
                    x = ("Brrr, make sure you have your jacket with you!")
                if current_temperature < 0: 
                    x = ("Brrr, it's freezing!")  

                if feels_like > 18: 
                    gt = (":hot_face: Some sweet temps!")
                else:
                    gt = (":cold_face: Youre better off with some long pants today!")
                if feels_like < 10: 
                    gt = ("Brrr, make sure you have your jacket with you!")
                if feels_like < 0: 
                    gt = ("Brrr,it's freezing!")  

                if current_pressure > 1025: 
                    h = (":compression: This is currently a high pressure area!")
                else:
                    h = (":compression: This is currently a low pressure area!")       
        
                if current_humidity > 70:
                    d = (":sweat_drops: It's quite humid in the air!")
                else:
                    d = (":droplet: It's pretty dry in the air!")
###windspeed text                
                if ((windspeed>= 1) and (windspeed<= 2)):
                    wi = (":leaves: Windless: Smoke rises straight from chimneys.")
                elif ((windspeed>= 2) and (windspeed<= 5)):
                    wi = (":leaves: Weak wind, faint and quiet: Wind direction can be deduced from smoke plumes.")
                elif ((windspeed>= 6) and (windspeed<= 11)):
                    wi = (":leaves: Weak, faint coolness: Wind palpable in face, leaves move slightly.")    
                elif ((windspeed>= 12) and (windspeed<= 19)):
                    wi = (":leaves: Moderate wind, light coolness: Leaves are moving, flags fluttering.")
                elif ((windspeed>= 20) and (windspeed<= 28)):
                    wi = (":leaves: Moderate wind, moderate cool: Branches move, clothes flap.")    
                elif ((windspeed>= 29) and (windspeed<= 38)):
                    wi = (":wind_blowing_face: Fairly strong, fresh breeze: Moderate longer waves, small trees moving.")
                elif ((windspeed>= 39) and (windspeed<= 49)):
                    wi = (":wind_blowing_face: Strong, stiff breeze: Trees move, flags are taut.")    
                elif ((windspeed>= 50) and (windspeed<= 61)):
                    wi = (":wind_blowing_face: Strong, strong wind: Moderately large waves, slow running into the wind.")
                elif ((windspeed>= 62) and (windspeed<= 74)):
                    wi = (":wind_blowing_face: Stormy: Big waves, ridges begin to break, small branches break off.")             
                elif ((windspeed>= 75) and (windspeed<= 88)):
                    wi = (":cloud_tornado: Storm: High waves, waves roll and break combs, lots of spray, break branches.")
                elif ((windspeed>= 89) and (windspeed<= 102)):
                    wi = (":cloud_tornado: Severe storm: Very high waves, entire surface is white with spray, trees are uprooted.")    
                elif ((windspeed>= 103) and (windspeed<= 117)):
                    wi = (":cloud_tornado: Very severe storm, hurricane-like: Extremely high waves, extensive damage to forests/buildings.")
                elif windspeed > 117: 
                    wi = (":cloud_tornado: ahhhh! Hurricane: Air filled with foam and water, destruction of buildings and forests, extremely high waves.")   
###Weather icons
                if '01d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/sunedited.png")
                elif '01n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/01n@2x.png")
                elif '02d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/02d@2x.png")
                elif '02n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/02n@2x.png")
                elif '03d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/03d@2x.png")
                elif '03n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/03n@2x.png")      
                elif '04d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/04d@2x.png")
                elif '04n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/04n@2x.png")
                elif '09d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/09d@2x.png")
                elif '09n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/09n@2x.png")                            
                elif '10d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/10d@2x.png")
                elif '10n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/10n@2x.png")      
                elif '11d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/11d@2x.png")
                elif '11n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/11n@2x.png")
                elif '13d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/13d@2x.png")
                elif '13n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/13n@2x.png")                   
                elif '50d' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/50d@2x.png")
                elif '50n' == cloud_icon:
                    ci = ("https://kelvindereus.nl/images/weer/50n@2x.png")          
##making and sending a embed to Discord
                embedVar = discord.Embed(title="Weather information for: " +str (city_name1), description="Information by Openweathermap.", color=0x206694)
                embedVar.add_field(name="Temperature", value=x + str (" ") + str (round(current_temperature,1)) + str ("c"), inline=False)
                embedVar.add_field(name="Feeling temperature", value=gt + str (" ") + str (round(feels_like,1)) + str ("c"), inline=False)

                embedVar.add_field(name="Pressure", value=h + str (" ") + str (current_pressure) + str ("mbar"), inline=False)
                embedVar.add_field(name="Moisture", value=d + str (" ") + str (current_humidity) + str ("%"), inline=False)
                embedVar.add_field(name="Wind", value=wi + str (" ") + str (round(windspeed,2)) + str ("km/u"), inline=False)

                embedVar.set_image(url=ci)
                embedVar.add_field(name="Rain", value=r, inline=False) 
                embedVar.set_footer(text="By Kelvin",icon_url="https://kelvindereus.nl/CustomCPULOGO.png")

                await message.channel.send(embed=embedVar)
            else:
                await message.channel.send("I can't find this city!")



##The bot token
bot.run('YOURTOKENHERE')

