import base_livre
import shutil
import os
import pandas as pd
from ebooklib import epub
import pdfkit
from IPython.core.display import HTML


""""  Afin de créer une instance de la classe base_bibli il faudra lui passer en argument le chemin vers 
        le répertoire qui vous servira de bibliothèque"""

class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        self.path = path

    def ajouter(self,livre): 
        """Ajoute le livre à la bibliothèque """
        try:
            if os.path.exists(livre):
                return "Le fichier existe déja dans le répertoire"
            elif not os.path.exists(livre):
                shutil.copy(livre, self.path)# on copie le livre directement dans la bibliothèque depuis sa source
        except:
            raise NotImplementedError(" format non pris en charge ")
        
        
    def _donnees_bibliotheque(self):
        try:
            book_metadata = []
            book_paths = []
            for file in os.listdir(self.path): # pour parcourir les éléments du répertoire 
                file_path = os.path.join(self.path, file)#concatène le chemin du répertoire a celui de l'element pour déterminer le chemin du livre
                book_paths.append(file_path)
            for path in book_paths:
                livre = base_livre(path)
                book_metadata.append(livre)
            df = pd.DataFrame(book_metadata, columns=['titre','auteur','type', 'nom'])          
            return df
        except:
            raise NotImplementedError (f" Error processing {path}")      
        

    def _genere_rapport(self,html_content,format,fichier):
        try:
            if format == "PDF":
                #on transforme le texte html directement en fichier pdf
                pdfkit.from_string(html_content, fichier)
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

            elif format == "EPUB":
                book = epub.EpubBook() # crée l'objet  de type EPUB
                # on crée une section pour le rapport
                section = epub.EpubHtml(title="Rapport Livres", file_name="rapport.html", lang="fr")
                section.content = html_content #  on defini le contenu de la section
                # On ajoute la section au rapport
                book.add_item(section)
                # On rajoute la section au rapport comme contenu
                book.spine = [section]
                #on ajoute nos diférentes sections au fichier EPUB
                epub.write_epub(fichier, book, {})
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")
        except:
            raise NotImplementedError(" format non pris en charge ")


    def rapport_livres(self, format, fichier):
        html_content = HTML(contenu_html)
        return self._genere_rapport_livres(html_content)

    def rapport_auteurs(self,format, fichier):
        #le df_authors est le dataframe des auteurs et de tous leurs livres présents dans la bibilothèque
        res = self._donnees_bibliotheque()
        #html_table est notre dataframe de données transformer en fichier html
        #contenu =f" <!DOCTYPE html> <html lang=\"fr\"><head><meta charset=\"UTF-8\"> "
        contenu = res.to_html()
    
        html_content = HTML(contenu)
        return self._genere_rapport(html_content,format,fichier)


class simple_bibli(base_bibli):

    def __init__(self,path):
        super().__init__(path)
