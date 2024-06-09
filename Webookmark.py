from tinydb import TinyDB, Query
donnees = TinyDB('data.json')
User = Query()



def affichage():
    print("Tableau des entrer :")
    for element in donnees:
        print(element)

def ajout():
    nom = input("Saisie le nom du site : ")
    sujet = input("Saisie le sujet : ")
    lien = input("Saisie l'URL du lien : ")
    print("Est-ce correct : \n"+nom+"\n"+sujet+"\n"+lien)
    donnees.insert({'Nom': nom, 'Sujet':sujet, 'Lien': lien})

def main():
    print("Bienvenue sur ton webookmarks")
    while True:
        print("""\n-----------------------------
add : Ajouter une entrer\nshow : Afficher le tableau
-----------------------------\n """)
        choix = input("Option : ")
        if(choix == "add"):
            print(ajout())
        elif(choix == "show"):
            print(affichage())
            

main()
