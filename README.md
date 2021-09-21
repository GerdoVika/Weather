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
To add requirement do the next command:
```
python -m pip install -r requirements.txt
```
In config.py you need to replace 'your api key' with api key from [Visual Crossing](https://www.visualcrossing.com/weather-api)

To start the project locally you should do next command:
```
flask run
```
or
```
python app.py
```
