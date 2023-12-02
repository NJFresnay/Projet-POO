from bs4 import BeautifulSoup #Python library for pulling data out of HTML
import requests
import os

class bibli_scrap:
    """
    exemple d'utilisation:
    
    path = bibli_scrap(r"C:\Users\jaffa\OneDrive\Desktop\Bibliotheque")

    path.scrap("https://math.univ-angers.fr/~jaclin/biblio/livres/", 1, 2)
    """

    def __init__(self,bibli_path):
        self.bibli_path = bibli_path ##juste modifiez cette fonction d'une facon qu'elle hérite le path du folder de la bibliotheque de l'autre class
        
    def scrap(self, url, profondeur, nbmax):
        i = 0 #initialiser le compteur
        if profondeur == 0 or nbmax == 0: #si les arguments sont zero on sortie
            return
        
        directory = self.bibli_path #je détermine le directoire
        
        if not os.path.exists(directory): #si le directoire n'existe pas on la créer
            os.makedirs(directory)
        
        try:
            html_page = requests.get(url, verify=False).content
            soup = BeautifulSoup(html_page, "html.parser")

            for l in soup.find_all("a"): #ici on cherche les lien
                lien = l.get('href', []) #on extract les liens
                if lien.endswith('.pdf') or lien.endswith('.epub'): 
                    try:
                        if 'https://' not in lien:
                            lien = url + lien #ajouter le nom du server au lien incomplet
                        reponse = requests.get(lien, verify =False)
                        
                        filename = os.path.join(directory, os.path.basename(lien)) #nommer le fichier de chaque livre selon le nom du base du lien
                        
                        with open(filename, mode="wb") as file: #télechargement
                            file.write(reponse.content)
                        i +=1
                        if i >= nbmax: #on a dépasser le nombre maw des fichier à télécharger
                            break
                        
                    except requests.exceptions.RequestException as e:
                        print(f"Erreur du téléchargement {lien}: {e}")
                        
        except requests.exceptions.RequestException as e:
            print(f"Un erreur inattendu: {e}")
            
