import base_livre
import shutil
import os
import pandas as pd
from ebooklib import epub
from weasyprint import HTML #librairie utiliser pour transformer du contenu html en pdf


""""  Afin de créer une instance de la classe base_bibli il faudra lui passer en argument le chemin vers 
        le répertoire qui vous servira de bibliothèque"""

class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        self.path = path

    def ajouter(self,livre):
        """Ajoute le livre à la bibliothèque """
        if isinstance(livre, base_livre.PDF) or  isinstance(livre, base_livre.EPUB):
            shutil.copy2(livre.ressource, self.path)  # on copie le livre directement dans le répertoire courant
            print(" Ajout effectué avec succès! ")
        raise NotImplementedError(" format non pris en charge ")

    def rapport_livres(self, format, fichier):
        contenu_html = """
                    <!DOCTYPE html>
                    <html lang="fr">
                    
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    
                    <body>
                    <h1>  Etat des livres </h1>
                        <div> self.donnees_bibliotheque().to_html() </div>
                    </body>
                    </html>
                """
        return self.genere_rapport(contenu_html,format,fichier)

    def rapport_auteurs(self,format, fichier):
        #le df_authors est le dataframe des auteurs et de tous leurs livres présents dans la bibilothèque
        df_authors = self.donnees_bibliotheque().groupby('auteur').agg({
                        'titre': lambda x : ', '.join(x),
                        'type': lambda x : ', '.join(x),
                        'nom du fichier': lambda x : ', '.join(x),
                        }).reset_index()
        
        #html_table est notre dataframe de donnees transformer en fichier html
        contenu_html = """
                    <!DOCTYPE html>
                    <html lang="fr">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>  Etat des livres </h1>
                        {% for index, row in df_authors.iterrows() %}
                        <ul>
                            {% for t, f, n in zip(row['titre'], row['type'], row['nom du fichier']) %}
                            <div> <li>
                               <p> <strong>{{ row['auteur'] }}</strong></p>
                                <p> titre: {{ book }}</p>
                                <p>: {{ date }}</p>
                                <p>Title: {{ title }}</p>
                            </li> </div>
                            {% endfor %}
                        </ul>
                        {% endfor %}
                    </body>
                    </html>
                    """
        return self.genere_rapport(contenu_html,format,fichier)

    def donnees_bibliotheque(self):
        """ Cette méthode récupère les éléments du répertoire courant et les stocke dans un dataframe, afin de faciliter
            l'extraction d'informations utiles pour le rapport"""
        
        book_metadata = []
        book_paths = []
        for i in os.listdir(self.path): # pour parcourir les éléments du répertoire 
            chemin_file = os.path.join(self.path, i)#concatène le chemin du répertoire a celui de l'element pour déterminer le chemin du livre
            book_paths.append(chemin_file)
            for path in book_paths:
                try:
                    if path.endswith(".pdf"):
                        livre = base_livre.PDF(path)
                    elif path.endswith('.epub'):
                        livre= base_livre.EPUB(path)      
                    book_metadata.append([livre.titre(), livre.auteur(), livre.type().__name__,livre.ressource[len(self.path)+1:]])
                    df = pd.DataFrame(book_metadata, columns=['titre','auteur','type', 'nom du fichier'])
                    df_sort = df.sort_value(by='titre')
                except:
                    raise IOError(f" Error processing {path}")      
        return df_sort

    def genere_rapport(self,contenu_html,format,fichier):
        """Cette méthode génère un rapport au format pdf ou epub selon l'utilisateur. Elle prend en argument
            repetoire de ce dernier, du contenu HTML sous forme de chaine de caractères, un format de sortie et le nom du fichier
            à générer"""
        try:
            if format == "PDF":
                HTML(string = contenu_html.write_pdf(fichier)) #on transforme le texte html directement en fichier pdf
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

            elif format == "EPUB":
                book = epub.EpubBook() # crée l'objet  de type EPUB
                # on crée une section pour le rapport
                section = epub.EpubHtml(title="Rapport Livres", file_name="rapport.html", lang="fr")
                section.content = contenu_html #  on defini le contenu de la section
                # On ajoute la section au rapport
                book.add_item(section)
                # On rajoute la section au rapport comme contenu
                book.spine = [section]
                #on ajoute nos diférentes sections au fichier EPUB
                epub.write_epub(fichier, book, {})
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")
        except IOError:
            raise NotImplementedError(" format non pris en charge ")

class simple_bibli(base_bibli):

    def __init__(self,path):
        super().__init__(path)
