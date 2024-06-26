from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim(user_agent="Delivery Helper")


def location_prov(raw_addresses):
    for address in raw_addresses:
        end = address.find(",")
        if end != -1:
            address: str = address[:end]

        sleep(1)
        new_address = address.strip() + ", Baltimore, MD"
        location = geolocator.geocode(new_address)
        if location == None:
            address = " ".join(address.split()[:-1])
            new_address = address.strip() + ", Baltimore, MD"
            sleep(1)
            location = geolocator.geocode(new_address)
        print(location.latitude, location.longitude)


location_prov(
    [
        "1204 Sheridan Avenue",
        "1300 Airlie Way, Baltim",
        "6865 Queens Ferry Ro",
        "505 Tunbridge Rd, Bal",
        "1259 Limit Ave, Baltime",
        "GBMC",
    ]
)
