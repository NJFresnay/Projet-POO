import base_bibli, bibli_scrap

# La classe bibli sert à alimenter notre bibliothèque à l'aide du web scraping.
# Pour se faire, elle hérite des méthodes de "base_bibli" pour la génération des rapports
# et de "bibli_scrap" pour récupérer les documents depuis l'url directement 

class bibli(base_bibli, bibli_scrap):
    
    def ___init__(self, path):
        """ Vous devez lui passer en arguments le chemin vers le répertoire
            qui vous servira de bibliothèque"""
        base_bibli.__init__(path)
        bibli_scrap.__init__(path)

    def alimenter(self, url, profondeur=1, nbmax):
        if os.path.exists(url): #si c'est un fichier sur notre machine appelle 'ajouter()'
            return self.ajouter(url)
        else:  #sinon c'est une url, appelle 'scrap()'
            return self.scrap(url, profondeur, nbmax)        
