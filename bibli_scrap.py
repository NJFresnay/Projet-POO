from bs4 import BeautifulSoup
import requests

class bibli_scrap:
    
    def __init__(self):
        pass

    def scrap(url, profondeur, nbmax):
        
        if profondeur == 0 or nbmax == 0:
            return
        
        directory = os.path.join(os.getcwd(), "Desktop", "Bibliotheque")

        if not os.path.exists(directory):
            os.makedirs(directory)

        html_page = requests.get(url, verify=False).content
        soup = BeautifulSoup(html_page, "html.parser")
        i = 0
    
        try:
            for i, l in enumerate(soup.find_all("a")):
                lien = l.get('href', [])
                if lien.endswith('.pdf') or lien.endswith('.epub'):
                    try:
                        lien = "https://math.univ-angers.fr/~jaclin/biblio/livres/" + lien
                        reponse = requests.get(lien)
                        filename = os.path.join(directory, os.path.basename(lien))
                        with open(l.title, mode="wb") as file:
                            file.write(reponse.content)
                        self.nbmax -= 1
                    
                    except requests.exceptions.RequestException as e:
                        print(f"Erreur du téléchargement {lien}: {e}")
                        
        except requests.exceptions.RequestException as e:
            print(f"Un erreur inattendu: {e}")

