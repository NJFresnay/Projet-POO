import base_livre
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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
        pass

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
        self.livres = []
        for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
            chemin_file = os.path.join(self.path, i)
            livre = base_livre.base_livre(chemin_file)
            self.livres.append(livre)
        #     print(livre)
        # #     # df = pd.DataFrame(self.livres,index=[i for i in range(0, len(os.listdir(self.path)))] ,columns=['titre','auteur','type', 'nom du fichier'])
        # #     # df.reset_index(inplace=True)
        # print(self.livres)

    def rapport_livres(self, format, fichier):
        try:
            if format == "PDF":
                # with open(fichier, "w", encoding='utf-8') as pdfFile:
                #     pdfFile.write("Etat des livres de la bibliotheque:")
                #     for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
                #         chemin_file = os.path.join(self.path, i)
                #         livre = base_livre.base_livre(chemin_file)
                #         ll = f"{livre.titre()}, {livre.auteur()}, {livre.sujet()}, {i}"
                #         pdfFile.write(ll)
                #     pdfFile.close()


### encore un problème d'affichage avec le rapport en PDF. A revoir
                with open(fichier, "wb") as pdfFile:
                    pdf = canvas.Canvas(pdfFile, pagesize=letter)
                     # Spécifier la police et la taille du texte
                    pdf.setFont("Helvetica", 20)

                    # Ajouter le titre du rapport
                    pdf.drawString(230, 700, "Etats des livres")
                    # Ajouter d'autres détails du rapport
                    for i in os.listdir(self.path): # permet d'accéder aux éléments de mon repertoire
                        chemin_file = os.path.join(self.path, i)
                        livre = base_livre.base_livre(chemin_file)
                        ll = f"{livre.titre()}\n"
                        # Coordonnées Y pour les lignes suivantes
                        y_coord = 350
                        # Ajouter les lignes de texte
                        pdf.drawString(100, y_coord, ll)
                        y_coord += 100  # Ajuster l'espacement entre les lignes
                    # Enregistrer le fichier PDF
                    pdf.save()
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
                        #section.content = self._generer_contenu_rapport_epub()
                section.content = _generer_contenu_html(self)
                # Ajoutez la section au livre
                book.add_item(section)
                # Ajoutez la section au livre comme une sorte de contenu
                book.spine = [section]
                # Ecriture du fichier EPUB
                epub.write_epub(fichier, book, {})

                print(f"Rapport généré au format {format}, nom du fichier : {fichier}")

        except IOError:
            raise NotImplementedError(" format non pris en charge ")





