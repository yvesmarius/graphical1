
from inscript import inscription
from historique_client import historique
def call_function():
    menu="""
1-se ravitailler
2-effectuer livraison
3-ajouter client
4-Histoirique
"""
    print(menu)        
    print("bienvenue!!!!!")        
    choix=input("choisissez un option")
    if choix=="3":
        print("Incription")
        inscription(user_name=input("entre un nom"),pass_word=input("entre mot de passe"))


    if choix=="4":
        historique()



call_function()