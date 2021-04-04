# <==== MAIN ====>

import sys as sys
import requests as requests
import csv as csv
import json as json


# current_ip = input("IP Address: ")
current_ip = '202.44.76.8';             # =================>>   Input
RAPIDAPI_KEY = 'f2f518c7c6msh41fb74a31c2d77bp13e751jsnc3050cb54120'


def trigger_api(ip):
    querystring = { 
        "ip": ip
        }
    headers = {
        'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
        'x-rapidapi-key': RAPIDAPI_KEY
    }
    url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if (response.status_code == 200):
        return json.loads(response.text)
    else:
        return None



if __name__ == "__main__":

    try: 
        api_response = trigger_api(current_ip)
        print(api_response)
    except TypeError as e:
        print(e)
        print("Type Error...Aborting")
    except csv.Error as e:
        print(e)
        print("CSV Error...Aborting")
    except Exception as e:
        print("Major Exception ...Aborting")
        sys.exit(e)


