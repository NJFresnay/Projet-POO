from base_bibli import base_bibli
import os

# La classe bibli sert à alimenter notre bibliothèque à l'aide du web scraping.
# Pour se faire, elle hérite des méthodes de "base_bibli" pour la génération des rapports
# et de "bibli_scrap" pour récupérer les documents depuis l'url directement 

class bibli(base_bibli):
    
    def __init__(self, path):
        """ Vous devez lui passer en arguments le chemin vers le répertoire
            qui vous servira de bibliothèque"""
        super().__init__(path)
        from bibli_scrap import bibli_scrap  
        self.scrap_instance = bibli_scrap(path)

    def alimenter(self, url, nbmax):
        if os.path.exists(url): #si c'est un fichier sur notre machine appelle 'ajouter()'
            return self.ajouter(url)
        else:  #sinon c'est une url, appelle 'scrap()'
            #selon le sujet elle ajoute tous les livres référencés dans la page web correspondant à l’URL
            profondeur = 1 #alors prof = 1
            return self.scrap_instance.scrap(url, profondeur, nbmax)        
