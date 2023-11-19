# Projet-POO
Réalisation du projet de fin  de POO ( Rayane JAFFAL et Jennifer NGOUNA).

Collecte de livres
==================

L’objectif est de concevoir une application pour constituer et suivre une bibliothèque de livres. L’idée est de pouvoir collecter des livres sur le web (_web scraping_) pour constituer une bibliothèque, et générer divers catalogues de cette bibliothèque. On s’intéresse ici aux livres au format _EPUB_ et _PDF_. Mais l’application doit être extensible de façon à pouvoir facilement ajouter d’autres formats.

[](#_modalités)Modalités
------------------------

Le projet est à réaliser en binôme. Il se compose de 3 étapes bien définies dans le temps. La première consiste à concevoir une bibliothèque de classes. La deuxième consiste à évaluer le code réalisé et à le comparer au code réalisé par les autres binômes. La troisième consiste à créer une application en utilisant la bibliothèque précédente.

Chaque binôme peut utiliser la bibliothèque d’un autre binôme pour réaliser son application.

Respecter scrupuleusement les dates, il ne pourra pas y avoir de prolongation.

[](#_pré_requis)Pré-requis
--------------------------

La classe abstraite ci-dessous modélise un livre :

    class base_livre:
      def __init__(self,ressource):
        """
            ressource désigne soit le nom de fichier (local) correspondant au livre,
            soit une URL pointant vers un livre.
        """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def type(self):
        """ renvoie le type (EPUB, PDF, ou autre) du livre """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def titre(self):
        """ renvoie le titre du livre """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def auteur(self):
        """ renvoie l'auteur du livre """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def langue(self):
        """ renvoie la langue du livre """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def sujet(self):
        """ renvoie le sujet du livre """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def date(self):
        """ renvoie la date de publication du livre """
        raise NotImplementedError("à définir dans les sous-classes")

Elle est destinée à servir de classe de base aux différents types de livres pouvant se trouver dans la bibilothèque (donc des livres au format EPUB et PDF dans un premier temps).

La classe abstraite ci-dessous modélise la bibliothèque :

    class base_bibli:
      def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def ajouter(self,livre):
        """
          Ajoute le livre à la bibliothèque """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def rapport_livres(self,format,fichier):
        """
            Génère un état des livres de la bibliothèque.
            Il contient la liste des livres,
            et pour chacun d'eux
            son titre, son auteur, son type (PDF ou EPUB), et le nom du fichier correspondant.
    
            format: format du rapport (PDF ou EPUB)
            fichier: nom du fichier généré
        """
        raise NotImplementedError("à définir dans les sous-classes")
    
      def rapport_auteurs(self,format,fichier):
        """
            Génère un état des auteurs des livres de la bibliothèque.
            Il contient pour chaque auteur
            le titre de ses livres en bibliothèque et le nom du fichier correspondant au livre.
            le type (PDF ou EPUB),
            et le nom du fichier correspondant.
    
            format: format du rapport (PDF ou EPUB)
            fichier: nom du fichier généré
        """
        raise NotImplementedError("à définir dans les sous-classes")

Elle est destinée à servir de classe de base à la classe qui implémentera réellement les traitements.

[](#_étape_i)Étape I
--------------------

Créer un dépot privé sur github pour le projet (1 dépot par binôme). Affecter les droits de lecture et d’écriture au binôme.

Créer les sous-classes de `base_livre` utiles et nécessaires à l’application.

Créer une sous-classe `simple_bibli` de `base_bibli`, et l’alimenter avec quelques livres matérialisés sous forme de fichiers situés sur la machine locale.

Créer une nouvelle classe `bibli` identique à la précédente, dotée d’une méthode supplémentaire `alimenter(self,url)` à qui on fournit une URL, et qui ajoute tous les livres référencés dans la page web correspondant à l’URL \[[1](#_footnotedef_1 "View footnote.")\].

Créer une nouvelle classe `bibli_scrap` dotée d’une méthode `scrap(self,url,profondeur,nbmax)`, qui réalise un web scraping destiné à alimenter la bibliothèque. Cette méthode a 3 paramètres : `url`, `profondeur` et `nbmax`. Elle récupère la page web référencée par `url`, puis télécharge tous les ressources `PDF` et `EPUB` qui y sont référencées. Ensuite, elle extrait de cette page tous les liens vers d’autres pages web, et réitère le processus précédent sur chacune d’elles. Le processus se réitère jusqu’à ce que l’un des critères d’arrêt soit vérifié.

`url` est l’URL de départ du scraping. `profondeur` est le nombre maximal de sites à parcourir. `nbmax` est le nombre maximal de documents à télécharger.

Implémentez ces classes en optimisant la clarté, la réutilisabilité et la maintenabilité. A la fin de cette partie, vous devez disposer de toutes les briques nécessaires au développement de l’application.

Rédiger une petite documentation (maximum 3 pages au format PDF ou EPUB) à destination des développeurs qui souhaiteraient utiliser ces classes (manuel technique).

Avant le 4/12/2023, chacun des 2 binômes dépose les codes sources et la documentatin sur son espace Moodle.

Le 4/12/2023, le binôme rend public son dépot sur github, de telle sorte que toute la promo puisse étudier son code.

[](#_étape_ii)Étape II
----------------------

Entre le 4/12/2023 et le 6/12/2023,

Parcourez le travail réalisé par les autres binômes. Vous allez peut-être découvrir que certains ont fait un travail plus clair, plus réutilisable, plus maintenable ou plus performant que le vôtre. Ce n’est pas grave, c’est comme cela que l’on progresse. C’est pourquoi vous avez ici la possibilité de réaliser l’étape III en utilisant l’étape I d’un autre binôme. Dans ce cas, intégrez son code dans votre dépot git \[[2](#_footnotedef_2 "View footnote.")\].

Enfin, chaque binôme rebascule son dépot github en privé le 6/12/2023.

[](#_étape_iii)Étape III
------------------------

En utilisant la bibliothèque choisie, concevoir une application `bibli` s’utilisant comme :

$ ./bibli https://math.univ-angers.fr/~jaclin/biblio/livres 1

pour lancer une collecte de profondeut 1 visant à compléter la bibliothèque, et :

$ ./bibli rapports

pour générer les 2x2 rapports au format EPUB et PDF \[[3](#_footnotedef_3 "View footnote.")\].

L’application utilise un fichier de configuration `bibli.conf` contenant :

*   le nom du répertoire destiné à recevoir les livres récoltés,
    
*   le nom du répertoire destiné à recevoir les rapports,
    
*   le nombre max de livres à rapatrier à chaque collecte (sécurité pour ne pas exploser le disque).
    

Exemple :

fichier biblio.conf

bibliotheque=/tmp/bibli/livres
etats=/tmp/bibli/etats
nbmax=1000

Pour permettre à l’application de pouvoir gérer plusieurs jeux de paramètres (par exemple plusieurs bibliothèques), le nom du fichier de configuration peut être spécifié avec l’option `-c`. Par exemple :

$ ./bibli -c bibli2.conf https://math.univ-angers.fr/~jaclin/biblio/livres 1

ou bien

$ ./bibli -c bibli2.conf rapports

Rédiger une petite documentation d’une page pour les utilisateurs de l’application (guide d’utilisation). Ne pas oublier de mentionner le binôme auprès duquel la partie I a été récupérée.

Chacun des 2 binômes dépose alors ses codes sources, le fichier de configuration et la documentation sur son espace Moodle, et part en vacance de Noël la tête vidée.

* * *
