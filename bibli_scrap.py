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
        self.bibli_path = bibli_path # ok
        
    def scrap(self, url, profondeur, nbmax): #pour le moment profondeur = 1, nbmax est le nombre maximal de fichiers à télécharger 
        i = 0 #initialisation du compteur
        if profondeur == 0 or nbmax == 0: #si les arguments sont nuls on sortie
            return "??????"
        
        #directory = self.bibli_path # on determine le répertoire de travail 
        #ligne pas très utile à mon avis car on a toujours accès à cette donnée
        
        if not os.path.exists(self.bibli_path): #si le répertoire n'existe pas on le crée
            os.makedirs(dself.bibli_path)
        
        try:
            html_page = requests.get(url, verify=False).content
            soup = BeautifulSoup(html_page, "html.parser")

            for l in soup.find_all("a"): #ici on cherche tous les liens
                lien = l.get('href', []) #puis on les extrait
                if lien.endswith('.pdf') or lien.endswith('.epub'): 
                    try:
                        if 'https://' not in lien:
                            lien = url + lien # on rajoute le nom du serveur au lien incomplet
                        reponse = requests.get(lien, verify =False)
                        
                        filename = os.path.join(self.bibli_path, os.path.basename(lien)) #nommer le fichier de chaque livre selon le nom du base du lien
                        
                        with open(filename, mode="wb") as file: #télechargement
                            file.write(reponse.content)
                        i +=1
                        if i >= nbmax:
                            break
                        
                    except requests.exceptions.RequestException as e:
                        print(f"Erreur du téléchargement {lien}: {e}")
                        
        except requests.exceptions.RequestException as e:
            print(f"Un erreur inattendu: {e}")
            
