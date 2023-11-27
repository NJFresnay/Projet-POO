import os
from ebooklib import epub  #librairie pour traiter les documents de type "ebook"
from pypdf import PdfReader #librairie pour traiter les documents de type "pdf"

class base_livre:
    def __init__(self,ressource):
        self.ressource = ressource
        if not os.path.exists(ressource): #vérification de l'existance du path
            raise FileNotFoundError(f"Ce fchier n'existe pas!")

    def type(self):
        # fichier_extension = os.path.splitext(self.ressource)[1].lower() #détecte l'extension du fichier
        # self.fichier_type = fichier_extension
        if self.ressource.endswith(".pdf"):
            return PDF
        elif self.ressource.endswith(".epub")":
            return EPUB
        else:
            raise ValueError("format non pris en charge")

    def titre(self):
        return self.type()(self.ressource).titre()

    def auteur(self):
        return self.type()(self.ressource).auteur()

    def langue(self):
        return self.type()(self.ressource).langue()

    def sujet(self):
        return self.type()(self.ressource).sujet()

    def date(self):
        return self.type()(self.ressource).date()

class PDF(base_livre):
    
    def type(self):
        return "PDF"

    def titre(self):
        livre = PdfReader(self.path)
        return livre.metadata.title

    def auteur(self):
        livre = PdfReader(self.path)
        return livre.metadata.author

    def langue(self):
        raise AttributeError("Information non fournie selon la documentation")

    def sujet(self):
        livre = PdfReader(self.path)
        return livre.metadata.subject

    def date(self):
        livre = PdfReader(self.path)
        return livre.metadata.creation_date

    def __repr__(self):
        return self.titre(), self.auteur(), self.Type(), self.date(), self.sujet()

    def __str__(self):
        return f"Titre: {self.titre()}, \nAuteur(s): {self.auteur()},\nType de fichier: {self.type()}, \nDate de publication: {self.date()}"

class EPUB(base_livre):
    
    def type(self):
        return "EPUB"

    def titre(self):
        livre = epub.read_epub(self.path)
        return livre.get_metadata("DC","title")

    def auteur(self):
        livre = epub.read_epub(self.path)
        return livre.get_metadata("DC","creator")

    def langue(self):
        livre = epub.read_epub(self.path)
        return livre.get_metadata("DC","language")
    
    def sujet(self):
        raise AttributeError("Information non fournie selon la documentation")

    def date(self):
        livre = epub.read_epub(self.path)
        return livre.get_metadata("DC","date")

# def extract_metadata_epub(epub_path):
#     book = epub.read_epub(epub_path)
#     metadata = {
#         'title': book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else None,
#         'author': ', '.join(author[0] for author in book.get_metadata('DC', 'creator')) if book.get_metadata('DC', 'creator') else None,
#         'language': book.get_metadata('DC', 'language')[0][0] if book.get_metadata('DC', 'language') else None,
#         'identifier': book.get_metadata('DC', 'identifier')[0][0] if book.get_metadata('DC', 'identifier') else None,
#         'subject': book.get_metadata('DC', 'subject')[0][0] if book.get_metadata('DC', 'subject') else None,
#         'date': book.get_metadata('DC', 'date')[0][0] if book.get_metadata('DC', 'date') else None,
#         'publisher': book.get_metadata('DC', 'publisher')[0][0] if book.get_metadata('DC', 'publisher') else None,
#         'description': book.get_metadata('DC', 'description')[0][0] if book.get_metadata('DC', 'description') else None,
#         # Ajoutez d'autres métadonnées selon vos besoins
#     }





    # def __repr__(self):
    #     return self.titre(), self.auteur(),self.langue(), self.Type(), self.date(), self.sujet()

    # def __str__(self):
    #     return f"Titre: {self.titre()}, \nAuteur(s): {self.auteur()}, \nlangue: {self.langue()},\nType de fichier: {self.Type()}, \nDate de publication: {self.date}, \nCatégorie: {self.sujet()}"

