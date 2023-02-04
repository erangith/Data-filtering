#########################
# Author: <Dadayakkara Dewege poorna Erangith Wijesire> 
#####################

import requests


def getDataFromApi():
    url = "https://data.novascotia.ca/resource/2shh-dv8p.json"
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()
    else:
        return "Error Retrieving Data"

data = getDataFromApi()

userFavorites = []

while True:
    user_input = input("\nPlease enter a town or restaurant name (when finished type 'done'): ")

    if user_input == 'done':
        break

    results = [i for i in data if i.get('facility', '').lower() == user_input.lower() or i.get('facility_town', '').lower() == user_input.lower()]
    results = [i for i in results if i.get('permit_type', ' ') == "Eating Establishment"] # filtering out anything that isnt an eating establishment.
    
    for index, res in enumerate(results, start=1):
        print(f"{index} - {res['facility']} {res['facility_town']}")
        
    if len(results) < 1:
        print("There were no results found!")
        continue
        
    while True:
        
        fav = int(input("Please enter the index of the resturant you'd like to favourite (when done type -1): "))

        if fav == -1:
            break # loop is finished
            
        elif fav > len(results):
            print("That is not a valid index")
        
        elif results[fav - 1] in userFavorites:
            print("That resturant is already in your list of favorites")
            
        else:
            userFavorites.append(results[fav - 1])
            print("{0} from {1} was added to the favorites list.".format(results[fav - 1].get('facility', ''), results[fav - 1].get('facility_town', '')))
            
if userFavorites:
    print("Here are your favorites:")
    for i in userFavorites:
        print(f"{i['facility']} > {i.get('facility_town', '')} {i.get('facility_address')}")
    
else:
    print("You didn't pick any favorites!")        
            















