from bs4 import BeautifulSoup #Python library for pulling data out of HTML
import requests
import os

class bibli_scrap(base_bibli):

    def __init__(self,path):
        super().__init__(path) #hérite le lien du répertoire où télecharger les livres de la classe base_bibli 
        
    def scrap(self, url, profondeur, nbmax):
        i = 0 #initialiser le compteur
        if profondeur == 0 or nbmax == 0: #si les arguments sont zero on sort
            return #ça return None 
        
        directory = self.path #je détermine le répertoire 
        
        if not os.path.exists(directory): #si le répertoire n'existe pas on le crée
            os.makedirs(directory)
        
        try:
            html_page = requests.get(url, verify=False).content
            soup = BeautifulSoup(html_page, "html.parser")

            for l in soup.find_all("a"): #ici on cherche les liens
                lien = l.get('href', []) #on extract les liens
                if lien.endswith('.pdf') or lien.endswith('.epub'): 
                    try:
                        if 'https://' not in lien:
                            lien = url + lien #ajouter le nom du server au lien incomplet
                        reponse = requests.get(lien, verify =False)
                        
                        filename = os.path.join(directory, os.path.basename(lien)) #nommer le fichier de chaque livre selon le nom de base du lien
                        
                        with open(filename, mode="wb") as file: #télechargement
                            file.write(reponse.content)
                        i +=1
                        if i >= nbmax: #on a dépasser le nombre max des fichier à télécharger
                            break
                        
                    except requests.exceptions.RequestException as e:
                        print(f"Erreur du téléchargement {lien}: {e}")
                        
        except requests.exceptions.RequestException as e:
            print(f"Un erreur inattendu: {e}")
            
