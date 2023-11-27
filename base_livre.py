#!env/bin/ python3

#classe base_livre
#sous classes: PDF, EPUB

import os
from ebooklib import epub #pip install EbookLib #EbookLib 0.18
from pypdf import PdfReader #pip install pypdf #pypdf 3.17.1

class base_livre:
    def __init__(self,ressource):
        self.ressource = ressourc
        if not os.path.exists(path):
            raise FileNotFoundError(f"Ce file '{ressource}' n'existe pas.")

    def type(self):
        fichier_extension = os.path.splitext(self.ressource)[1].lower()
        self.fichier_type = fichier_extension
        
        if self.fichier_type == ".pdf":
            return PDF
        elif self.fichier_type == ".epub":
            return EPUB
        else:
            raise NotImplementedError("format indéfini")

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
        return None

    def sujet(self):
        return None

    def date(self):
        livre = PdfReader(self.path)
        return livre.metadata.creation_date

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
        return None

    def date(self):
        livre = epub.read_epub(self.path)
        return livre.get_metadata("DC","date")

