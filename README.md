# Weather
Service provides statistical information about the weather for the last few days in any city.
### Request parametrs
- city - string, name of the city
- days - int, number of days
### Responce
Example of responce in json:
```
{  
  "city": "Saint-Petersburg",  
  "from": "2021-09-10",  
  "to": "2021-09-15",  
  temperature_c": {  
    "average": 25.0,  
    "median": 24.5,  
    "min": 20.1,  
    "max": 29.3  
    },  
  "humidity": {  
    "average": 55.4,  
    "median": 58.1,  
    "min": 43.1,  
    "max": 82.4  
   },  
  "pressure_mb": {  
    "average": 1016.0,  
    "median": 1016.5,  
    "min": 1015.1,  
    "max": 1017.3  
  }  
}  
```

***
### Start progect
At first you need to get api key from [Visual Crossing](https://www.visualcrossing.com/weather-api).

To start progect with docker you should run next command using received api key.
```
docker run -dp 8080:5000 -e API_KEY=<your-api-key> gerdovika/weather_app
```
The service will be available at address:
- http://localhost:8080/
