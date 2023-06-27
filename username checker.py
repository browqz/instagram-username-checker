import requests

def disponible(pseudo):
    url = f"https://www.instagram.com/{pseudo}/"
    response = requests.get(url)
    
    if response.status_code == 404:
        return True 
    else:
        return False  

username = input("Entre le pseudo de ton choix : ")

if disponible(username):
    print("Le pseudo est disponible.")
else:
    print("Le pseudo n'est pas disponible.")
