import inscript
import json
def historique():
    with open('data_user.json','r') as f:
        data=json.load(f) 
    print(data)