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
Exemple d'utilisation de cette classe:  

````python
livre = base_livre("path or URL")
livre.type()
livre.titre()
livre.auteur()
livre.langue()
livre.sujet()
livre.date()
````

   
[](#_la_bibliothèque)La Bibliothèque   
------------------------------------


      

[](#les_rapports)Les Rapports    
-----------------------------    


      

[](#web_scraping)Web Scraping   
-----------------------------   
La classe `bibli_scrap` est responsable de réaliser le web scraping destiné à alimenter la bibliothèque. Elle est dotée d'une méthode nommée `scrap` qui prends trois paramètres : `url`, `profondeur` et `nbmax`. Cette méthode récupère la page web référencée par url, puis télécharge tous les fichiers PDF et EPUB qui y sont référencés. Ensuite, elle extrait tous les liens vers d’autres pages web de cette page, répetant le processus sur chacune d’entre elles. Ce cycle se répète jusqu’à ce que l’un des critères d’arrêt soit satisfait.  

Le paramètre `url` représente l’URL de départ pour le scraping, `profondeur` détermine le nombre maximal de sites à explorer, et `nbmax` indique le nombre maximal de documents à télécharger.   

Cette classe utilise principalement la librairie `BeautifulSoup`. En particulier, la méthode `find_all` pour rechercher les liens dans la page qui appartiennent aux fichiers PDF et EPUB.  
Ensuite, les fichiers sont téléchargés:  
   
````python
#téléchargement
with open(filename, mode="wb") as file: #télechargement
    file.write(reponse.content)
````

Exemple d'utilisation de cette classe:  

````python
path = bibli_scrap(r"C:\Users\jaffa\OneDrive\Desktop\Bibliotheque") #le directoire où sauvegarder les fichiers
path.scrap("https://math.univ-angers.fr/~jaclin/biblio/livres/", 1, 2) #récupérer de cette page web
````

il me reste le profondeur....
