import requests
 
def googleAPI(address):
    GOOGLE_MAPS_API = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        'region': 'aus'
    }
    params['address'] = address

    res = requests.get(GOOGLE_MAPS_API, params=params)

    while 'error_message' in res.json():
        res = requests.get(GOOGLE_MAPS_API, params=params)
       
    res = res.json()

    return res

def getLatLong(address):
    res = googleAPI(address)

    lat = res["results"][0]["geometry"]["location"]["lat"]
    lng = res["results"][0]["geometry"]["location"]["lng"]

    return lat, lng

def getSuburbFromString(address):
    res = googleAPI(address)
    
    address = res["results"][0]["address_components"]
    suburb = next((c["long_name"] for c in address if "locality" in c["types"]))
    
    return suburb

def getSuburb(lat, lng):
    return getSuburbFromString(str(lat) + ", " + str(lng))
