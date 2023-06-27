import requests

def is_username_available(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 404:
        return True 
    else:
        return False  

username = input("Entre le pseudo de ton choix : ")

if is_username_available(username):
    print("Le pseudo est disponible.")
else:
    print("Le pseudo n'est pas disponible.")