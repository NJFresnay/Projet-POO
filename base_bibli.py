import base_livre
import shutil
import pdfkit
import urllib3
import os
import pandas as pd
from ebooklib import epub
from weasyprint import HTML

# la classe base_bibli

class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        self.path = path

    def ajouter(self,livre):
        """Ajoute le livre à la bibliothèque """
        if isinstance(livre, Base_livre.PDF) or  isinstance(livre, Base_livre.EPUB):
            shutil.copy(livre.ressource, self.path)
            print(" Ajout effectué avec succès! ")
        raise NotImplementedError(" format non pris en charge ")

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


class simple_bibli(base_bibli):

    def __init__(self,path):
        super().__init__(path)

    def rapport_livres(self, Format, fichier):
        try:
            if format == "PDF":
                HTML(string = self._generer_contenu_html()).write_pdf(fichier)
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

            elif format == "EPUB":
                book = epub.EpubBook() # crée l'objet  de type EPUB

                #Ajout des metadonnées à notre livre
                book.set_title("Rapport EPUB")
                book.set_language("fr")
                book.add_author("Rayane JAFFAL et Jennifer NGOUNA")

                # Créez une section pour le rapport
                section = epub.EpubHtml(title="Rapport Livres", file_name="rapport.html", lang="fr")
                section.content = self._generer_contenu_html() # defini le contenu de la section
                # Ajoutez la section au livre
                book.add_item(section)
                # Ajoutez la section au livre comme une sorte de contenu
                book.spine = [section]
                # Ecriture du fichier EPUB
                epub.write_epub(fichier, book, {})

                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")
        except IOError:
            raise NotImplementedError(" format non pris en charge ")




    def _generer_contenu_html1(self):
        book_metadata = []
        book_paths = []
        for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
            chemin_file = os.path.join(self.path, i)
            book_paths.append(chemin_file)

            for path in book_paths:
                try:
                    livre = base_livre.base_livre(chemin_file)
                    book_metadata.append([livre.titre(), livre.auteur(), livre.type().__name__,livre.ressource[len(self.path)+1:]])


                except Exception as e:
                    print(f"Error processing {chemin_file}: {str(e)}")

                df = pd.DataFrame(book_metadata, columns=['titre','auteur','type', 'nom du fichier'])
        return df




    def rapport_auteurs(self,Format, fichier):
          try:
            g_by = _generer_contenu_html1(self).groupby('auteur').agg({
                        'titre': lambda x : ', '.join(x),
                        'type': lambda x : ', '.join(x),
                        'nom du fichier': lambda x : ', '.join(x),
                        }).reset_index()

            contenu_html = """
                        <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Author Information</title>
                    </head>
                    <body>

                    <h1>Author Information</h1>

                    <!-- Assuming result_df is the DataFrame containing the aggregated information -->

                    for index, row in g_by.iterrows()

                        <h2>{{ row['auteur'] }}</h2>

                        <ul>
                            {% for book, date, title in zip(row['titre'], row['type'], row['nom du fichier']) %}
                                <li>
                                    <strong>Book:</strong> {{ book }}<br>
                                    <strong>Date:</strong> {{ date }}<br>
                                    <strong>Title:</strong> {{ title }}<br>
                                </li>
                            {% endfor %}
                        </ul>

                    </body>
                    </html>
                """

            if format == "PDF":
                    HTML(string = contenu_html.write_pdf(fichier)
                    print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

                elif format == "EPUB":
                    book = epub.EpubBook() # crée l'objet  de type EPUB

                    #Ajout des metadonnées à notre livre
                    book.set_title("Rapport EPUB")
                    book.set_language("fr")
                    book.add_author("Rayane JAFFAL et Jennifer NGOUNA")

                    # Créez une section pour le rapport
                    section = epub.EpubHtml(title="Rapport Livres", file_name="rapport.html", lang="fr")
                    section.content = contenu_html # defini le contenu de la section
                    # Ajoutez la section au livre
                    book.add_item(section)
                    # Ajoutez la section au livre comme une sorte de contenu
                    book.spine = [section]
                    # Ecriture du fichier EPUB
                    epub.write_epub(fichier, book, {})

                    print(f"Rapport généré au format {format}, nom du fichier : {fichier}")
            except IOError:
                raise NotImplementedError(" format non pris en charge ")














    def _generer_contenu_html(self):
        # Récupération de nos livres:
        contenu_html = "<style>.li {border-bottom: 50px}</style>"
        contenu_html += "<h1> Etat des livres</h1>"
        livres = []
        for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
            chemin_file = os.path.join(self.path, i)
            livre = base_livre.base_livre(chemin_file)
        for livre in livres:
            contenu_html+="<ul>"
            contenu_html += "<li>"
            contenu_html += f"<div><strong>{livre.titre()}</strong></div>"
            contenu_html += f"<div> Auteur : {livre.auteur()}</div>"
            contenu_html += f"<div> format :{livre.type().__name__}</div>"
            contenu_html += f"<div>nom du fichier : {livre.ressource[len(self.path)+1:]}</div>"
            contenu_html += "</li>"
            contenu_html += "</ul>"
            contenu_html += "<div></div>"
        return contenu_html
