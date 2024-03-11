import requests
import time

with open('compromisedEmail.txt', 'w'):
    pass

def check_mail(email):
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {
            'hibp-api-key': 'your-api-token'
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"\n⛔ Adresse e-mail {email} compromise. Changez immédiatement les mots de passe.")
        print("Services compromis associés : ")

        with open('compromisedEmail.txt', 'a') as compromised_file:
            compromised_file.write('\n '+ "[!]" + email + '\n')
            for breach in data:
                print(f"- {breach['Name']}")
                compromised_file.write(f"   - {breach['Name']} \n")

    elif response.status_code == 404:
        print(f"🟢 Adresse e-mail : {email} non compromise. Restez vigilant ! \n")
    else:
        print(f"Erreur lors de la requête. Code de statut : {response.status_code}")
        exit("Fin du script.")
    


print("Vérification de la liste d'email en cours : \n")
with open('list_mail.txt', 'r') as file:
    emailToCkech = file.read().splitlines()

    
requests_per_minute_limit = 10
second_per_request = 60 / requests_per_minute_limit

for email in emailToCkech:
    check_mail(email)
    time.sleep(second_per_request)
input("\n\nAppuyez sur entrée pour quitter...")
