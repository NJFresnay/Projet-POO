from bs4 import BeautifulSoup
import requests

class bibli_scrap:
    
    def __init__(self):
        pass

    def scrap(self, url, profondeur, nbmax):
        
        if profondeur == 0 or nbmax == 0:
            return

        html_page = requests.get(url, verify=False).content
        soup = BeautifulSoup(html_page, "html.parser")
        livres_urls = []
    
        for l in soup.find_all("a",) and for i in range(self.nbmax):
            lien = l.get('href', [])
            if lien.endswith('.pdf') or lien.endswith('.epub'):
                try:
                    if 'http' not in lien:
                        lien = '{}{}'.format(site,lien) #to handle schema invalid error
                    reponse = requests.get(lien)
                    with open(l.title, mode="wb") as file:
                        file.write(reponse.content)
                    livres_urls.append(lien)
                    self.nbmax -= 1
                    
                except NotImplementedError as e:
                    print(f"Error downloading {lien}: {e}")

                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

