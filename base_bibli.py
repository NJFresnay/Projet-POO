from base_livre import *
import shutil
import os
import pandas as pd
from ebooklib import epub
import pdfkit

""""  Afin de créer une instance de la classe base_bibli il faudra lui passer en argument le chemin vers 
        le répertoire qui vous servira de bibliothèque"""


class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        self.path = path

    def ajouter(self,livre): ##rayane: peux tu essayer cette méthode?
        """Ajoute le livre à la bibliothèque """
        if livre.endswith(".pdf") or livre.endswith(".epub"):
            shutil.copy(livre, self.path)# on copie le livre directement dans la bibliothèque depuis sa source
        raise NotImplementedError(" format non pris en charge ")

    def rapport_livres(self, format,fichier): #rayane: marche seulement avec les epub
        #contenu html du rapport_livres
        html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Rapport des livres</title>
            </head>
            <body>
                <h1>État des les livres</h1>
            """
        html_content += "<div> self.donnees().to_html() </div>"  #ici on recupère notre dataframe
        html_content += """
                            </body>
                        </html>
                    """
        return self.genere_rapport(format, fichier,html_content)
             
    def rapport_auteurs(self, format, fichier):
        df = self.donnees()
        # Construire le contenu HTML du rapport
        grouped_df = df.groupby('auteur').agg({
                    'titre': lambda x: ', '.join(x),
                    'type': 'count',  # compter le nombre de livres par auteur
                    'nom du fichier': lambda x: ', '.join(x)
                }).reset_index()
        
        html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Rapport des Auteurs</title>
            </head>
            <body>
                <h1>État des livres classés par auteurs</h1>
            """
        
        for index, row in grouped_df.iterrows():

                html_content += "<h4> {row['auteur']}</h4>"
                html_content += "<ul>"
        
                for t,f,n in zip(row['titre'], row['type'], row['nom du fichier']):
                
                        html_content += """
                            <li>
                                Titre : {t}
                                Format: {f}
                                nom du fichier :{{n}}<br>
                            </li>"""
                        html_content += "</ul>"
        html_content += """
                            </body>
                        </html>
                    """
        return self.genere_rapport(format, fichier, html_content)
          

    def donnees(self):
        try:
            file_data_list = []
            for file_name in os.listdir(self.path): # pour parcourir les éléments du répertoire 
                file_path = os.path.join(self.path, file_name)#concatène le chemin du répertoire a celui de l'element pour déterminer le chemin du livre
                book = base_livre(file_path)
                
                file_data= {
                    'titre': book.titre(),
                    'auteur': book.auteur(),
                    'type': book.type().__name__,
                    'nom du fichier': book.ressource[len(self.path)+1:-4]
                }
                file_data_list.append(file_data)
            df = pd.DataFrame(file_data_list, columns=['titre','auteur','type','nom du fichier'])
            return df    
        except:
            print(" Données non accessibles!")
            
            
    def genere_rapport(self,format,fichier,html_content):
        try:
            if format == "PDF":
                #on transforme le texte html directement en fichier pdf
                pdfkit.from_string(html_content, fichier)
                return f"Rapport généré au format {format}, nom du fichier : {fichier}"

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
                return f"Rapport généré au format {format}, nom du fichier : {fichier}"
        except:
            raise NotImplementedError(" format non pris en charge ")
    
   
            
