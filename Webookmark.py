from tinydb import TinyDB, Query
donnees = TinyDB('data.json')
User = Query()



def affichage():
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
    print(ajout())
    print(affichage())

main()