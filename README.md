# Bienvenue à la documentation de notre Module!   

Réalisation du projet finale de POO   
Rayane JAFFAL et Jennifer NGOUNA   
Prof. Jacquelin Charbonel   
Université d'Angers        

    

## Projet-POO : Collecte de livre   

L’objectif de ce projet est de concevoir une application pour constituer et suivre une bibliothèque de livres. L’idée est de pouvoir collecter des livres (au format _EPUB_ et _PDF_) sur le web (_web scraping_) pour constituer une bibliothèque, et générer divers catalogues de cette bibliothèque.

Page d'accueil : https://github.com/NJFresnay/Projet-POO.git     

   



[](#introduction)Introduction  
-----------------------------
Ce module se compose de quatre classes: la classe `base_livre` qui englobe les sous-classes `PDF` et `EPUB`, la classe `base_bibli` avec la sous-classe `simple_bibli`, la classe `bibli`, et enfin la classe `bibli_scrap`.   

    

[](#_librairies_python)Librairies Python   
----------------------------------------
Les librairies Python utilisées dans notre module:
- `pypdf` qui interagit avec les fichiers de format PDF [description](https://pypi.org/project/pypdf/)
- `EbookLib` qui interagit avec les fichiers de format EPUB [description](https://pypi.org/project/EbookLib/)  
- `requests` qui envoie des demandes HTTP [description](https://pypi.org/project/requests/)
- `BeautifulSoup` qui scrape les informations des pages HTML [description](https://pypi.org/project/BeautifulSoup/)




[](#_les_méta-données)Les méta-données   
--------------------------------------

La classe `base_livre` utilise principalement les librairies `pypdf` et `EbookLib` pour récupèrer les méta-données des livres en format PDF ou EPUD. Soit à partir d'un path local, soit à partir d'un URL. D'abord, on vérifie l'extension de la ressource pour savoire le type du fichier, puis selon le type on appelle soit la sous-classe `PDF`, soit la sous-classe `EPUB`.   
Ensuite, on vérifie le type de la ressource, parce que les librairies utilisées ne peuvent lire les fichiers qu'à partir d'un path local. Alors si la ressource est un URL on utilise la méthode `BytesIO` de la librarie `io` pour conserver le fichier dans une mémoire temporaire pour pouvoire récupérer les méta-données. 

les méthodes pour récupérer les méta-données de chaque librarie:   
```python
#EbookLib
#Pour les fichiers EPUB
from ebooklib import epub 
f = epub.read_epub(ressource)

f.get_metadata("DC","title") #DC pour Dublin Core metadata: les meta-données essentielles 
f.get_metadata("DC","creator")
f.get_metadata("DC","language")
f.get_metadata("DC","date")

#pypdf
#Pour les fichiers PDF
from pypdf import PdfReader
f = PdfReader(ressource)

f.metadata.title
f.metadata.author
f.metadata.subject
f.metadata.creation_date

````

   
[](#_la_bibliothèque)La Bibliothèque   
------------------------------------


      

[](#les_rapports)Les Rapports    
-----------------------------    


      

[](#web_scraping)Web Scraping   
-----------------------------   
La classe `bibli_scrap` réalise un web scraping destiné à alimenter la bibliothèque. Cette classe est dotée d'une méthode `scrap` qui a 3 paramètres : `url`, `profondeur` et `nbmax`. Elle récupère la page web référencée par url, puis télécharge tous les ressources PDF et EPUB qui y sont référencées. Ensuite, elle extrait de cette page tous les liens vers d’autres pages web, et réitère le processus précédent sur chacune d’elles. Le processus se réitère jusqu’à ce que l’un des critères d’arrêt soit vérifié.
`url` est l’URL de départ du scraping. `profondeur` est le nombre maximal de sites à parcourir. `nbmax` est le nombre maximal de documents à télécharger.   
Cette classe utilise principalement la librairie `BeautifulSoup`. Avec la méthode `find_all` on cherche les liens dans la page qui appartiennent aux fichiers PDF et EPUB. Ensuite on télécharge les fichiers:  
   
````python
#téléchargement
with open(filename, mode="wb") as file: #télechargement
                            file.write(reponse.content)
````

il me reste la partie profondeur
