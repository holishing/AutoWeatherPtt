# AutoWeatherPtt

Post daily weather information on pttbbs or any other bbs.

# Install

Install requirement from requirements.txt
```
$ pip install -r requirements.txt
```

Run weather.py with Python(>=3.7) and load config from command line
```
./weather.py exec -k APIKEY
```

Run weather.py with Python(>=3.7) and load config from config.json
```
./weather.py config [-h] filepath
```

## Argument Information

Argument Name | Alias  | Description
--------------|--------|-------------------------
--apikey      | -k     | apikey of cwb opendata

## Config Spec

A JSON file as below is required

```json
{
    "apikey": "CWB-********-****-****-****-************",
}
```
