# Nearby Finder
Nearby finder that lets you find nearby restaurant, petrol pump etc using **Google** and **Foursquare** API. By simply passing location and what you wanna find in that location you can get a list of results.

## Pre-requisites
1. **Google API key:** Google API is used to convert name of the place to coordinates (latitudes and longitudes). You can get Google API key [here](https://developers.google.com/maps/documentation/geocoding/get-api-key).
2. **Foursquare Client key and secret:** This API is used to find nearby places like nearby restaurant etc. You can get client key and secret [here](https://foursquare.com/developers/apps) by clicking on create new app.
3. **python3:** You can Download python e [here](https://www.python.org/)

## setup
1. open `main.py`
2. In top of that file you will find some variables like `GOOGLE_API_KEY=''` , `FOURSQUARE_CLIENT_KEY=''` and `FOURSQUARE_CLIENT_SECRET=''` inside `''` paste your API key , client key, and client secret respectively.

## how to used
#### By importing
1. import `main.py`
2. call `find_nearby('type of place to find','where to find')`
example `find_nearby('restaurant', 'Mumbai')`
3. In return you will get list of dictionaries of prototype
`{'name': name of the place, 'contact': contact of that place, 'address': address of place}`

#### Running directly
##### in Windows
1. right click on `main.py`
2. click on open with idle(python3 idle)
3. press `F5`
##### in Linux
1. open terminal
2. `cd` to directory you have downloaded this module
3. Type `python3 main.py`

### Contact Details
**email:** randomways01@gmail.com
