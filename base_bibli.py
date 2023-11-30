import base_livre
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import pdfkit
import urllib3
import os
import pandas as pd
from ebooklib import epub

# la classe base_biblio
class base_bibli:
    def __init__(self,path):
        """ path désigne le répertoire contenant les livres de cette bibliothèque """
        self.path = path

    def ajouter(self,livre):
        """Ajoute le livre à la bibliothèque """
        if isinstance(livre, Base_livre.PDF):
            un_livre = Base_livre.PDF(livre.ressource)
            self.livres.append(un_livre)

        elif isinstance( livre, Base_livre.EPUB):
            un_livre = Base_livre.EPUB(livre.ressource)
            self.livres.append(un_livre)


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


    def rapport_livres(self, format, fichier):
        try:
            if format == "PDF":
                c = canvas.Canvas(fichier)
                # Ajouter du texte avec une police spécifique et une taille de police
                c.setFont("Helvetica", 30)
                c.drawString(200, 790, " Etat des livres")
                c.setFont("Helvetica", 12)
                x_pos = 50
                y_pos = 750
                # Taille de la police
                font_size = 11
                c.setFont("Helvetica", font_size)

                livres = []
                lines= []
                k = 0
                for i in os.listdir(self.path): # permet d'accéder aux éléments de mon répertoire
                    chemin_file = os.path.join(self.path, i)
                    livre = base_livre.base_livre(chemin_file)
                    livres.append(livre)
                for livre in livres:
                    ll = [
                        f"{livre.titre()}",
                        f"{livre.auteur()}",
                        f"{livre.sujet()}",
                        f"{livre.langue()}"
                    ]
                    lines.append(ll)

                for line in lines:
                    c.drawString(x_pos, y_pos,', '.join(line))
                    # Déplacer la position verticalement pour la prochaine ligne
                    y_pos -= 20  # Ajouter un espace entre les lignes
                    #c.line(50, 700 - k, 550, 700 -k)
                    k += 60
                # Enregistrer le fichier PDF
                c.save()
                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

            elif format == "EPUB":

                def _generer_contenu_html(self):
                     # Récupération de nos livres:
                    contenu_html = "<style>.li {border-bottom: 50px}</style>"
                    contenu_html += "<h1> Etat des livres</h1>"
                    contenu_html+="<ul>"
                    livres = []
                    for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
                        chemin_file = os.path.join(self.path, i)
                        livre = base_livre.base_livre(chemin_file)
                        livres.append(livre)

                    for livre in livres:
                        contenu_html += f"<li><div> <strong>{livre.titre()}</strong></div><div> Auteur : {livre.auteur()}</div> <div> Type :{livre.type()}</div> <div>nom_fichier : {livre.ressource}</div></li>"
                    contenu_html += "</ul>"
                    return contenu_html

                book = epub.EpubBook() # crée l'objet  de type EPUB

                #Ajout des metadonnées à notre livre
                book.set_title("Rapport EPUB")
                book.set_language("fr")
                book.add_author("Rayane JAFFAL et Jennifer NGOUNA")

                # Créez une section pour le rapport
                section = epub.EpubHtml(title="Rapport Livres", file_name="rapport.html", lang="fr")
                section.content = _generer_contenu_html(self) # defini le contenu de la section
                # Ajoutez la section au livre
                book.add_item(section)
                # Ajoutez la section au livre comme une sorte de contenu
                book.spine = [section]
                # Ecriture du fichier EPUB
                epub.write_epub(fichier, book, {})

                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

        except IOError:
            raise NotImplementedError(" format non pris en charge ")



