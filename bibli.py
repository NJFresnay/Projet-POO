import base_bibli
from bs4 import BeautifulSoup
#pourquoi t a pas juste hériter de bibli_scrap parce que bibli_scrap hérite de base_bibli, tu as juste répeter le code de scrapping. No?

class bibli(base_bibli):
    def ___init__(self, path):
        super().__init__(path)

    def alimenter(self, url, profondeur=1, nbmax):
        i = 0 
        if profondeur == 0 or nbmax == 0: #si les arguments sont nuls en sortie
            return "??????"
          
        if not os.path.exists(self.path):     #si le répertoire n'existe pas on le crée
            os.makedirs(self.path)
        
        try:
            html_page = requests.get(url, verify=False).content
            soup = BeautifulSoup(html_page, "html.parser")

            for l in soup.find_all("a"):    #ici on cherche tous les liens
                lien = l.get('href', [])     #puis on les extrait
                if lien.endswith('.pdf') or lien.endswith('.epub'): 
                    try:
                        if 'https://' not in lien:
                            lien = url + lien # on rajoute le nom du serveur au lien incomplet
                        reponse = requests.get(lien, verify =False)
                        
                        filename = os.path.join(self.path, os.path.basename(lien)) 
                        
                        with open(filename, mode="wb") as file: #télechargement
                            file.write(reponse.content)
                        i +=1
                    except requests.exceptions.RequestException as e:
                        print(f"Erreur du téléchargement {lien}: {e}")
                        
        except requests.exceptions.RequestException as e:
            print(f"Un erreur inattendu: {e}")
