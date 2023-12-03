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
- `EbookLib` qui interagit avec les fichiers de format EPUB [description]([https://pypi.org//pypdf/](https://pypi.org/project/EbookLib/)  
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
ressource.get_metadata("DC","title") #DC pour Dublin Core metadata: les meta-données essentielles 
get_metadata("DC","creator")
get_metadata("DC","language")
get_metadata("DC","date")

#pypdf
#Pour les fichiers PDF
metadata.title
metadata.author
metadata.subject
metadata.creation_date

````

   
[](#_étape_ii)Étape II
----------------------

Entre le 4/12/2023 et le 6/12/2023,

Parcourez le travail réalisé par les autres binômes. Vous allez peut-être découvrir que certains ont fait un travail plus clair, plus réutilisable, plus maintenable ou plus performant que le vôtre. Ce n’est pas grave, c’est comme cela que l’on progresse. C’est pourquoi vous avez ici la possibilité de réaliser l’étape III en utilisant l’étape I d’un autre binôme. Dans ce cas, intégrez son code dans votre dépot git \[[2](#_footnotedef_2 "View footnote.")\].

Enfin, chaque binôme rebascule son dépot github en privé le 6/12/2023.

[](#_étape_iii)Étape III
------------------------

En utilisant la bibliothèque choisie, concevoir une application `bibli` s’utilisant comme :
````
$ ./bibli https://math.univ-angers.fr/~jaclin/biblio/livres 1
````
pour lancer une collecte de profondeut 1 visant à compléter la bibliothèque, et :
````
$ ./bibli rapports
````
pour générer les 2x2 rapports au format EPUB et PDF \[[3](#_footnotedef_3 "View footnote.")\].

L’application utilise un fichier de configuration `bibli.conf` contenant :

*   le nom du répertoire destiné à recevoir les livres récoltés,
    
*   le nom du répertoire destiné à recevoir les rapports,
    
*   le nombre max de livres à rapatrier à chaque collecte (sécurité pour ne pas exploser le disque).
    

Exemple :

fichier biblio.conf
````
bibliotheque=/tmp/bibli/livres
etats=/tmp/bibli/etats
nbmax=1000
````
Pour permettre à l’application de pouvoir gérer plusieurs jeux de paramètres (par exemple plusieurs bibliothèques), le nom du fichier de configuration peut être spécifié avec l’option `-c`. Par exemple :
````
$ ./bibli -c bibli2.conf https://math.univ-angers.fr/~jaclin/biblio/livres 1
````
ou bien
````
$ ./bibli -c bibli2.conf rapports
````
Rédiger une petite documentation d’une page pour les utilisateurs de l’application (guide d’utilisation). Ne pas oublier de mentionner le binôme auprès duquel la partie I a été récupérée.

Chacun des 2 binômes dépose alors ses codes sources, le fichier de configuration et la documentation sur son espace Moodle, et part en vacance de Noël la tête vidée.

* * *
