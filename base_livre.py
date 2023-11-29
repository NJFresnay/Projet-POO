#classe base_livre
#sous classes: PDF, EPUB

import io #lire URL
import os
import requests
from ebooklib import epub  #librairie pour traiter les documents de type "epub" #pip install EbookLib #EbookLib 0.18
from pypdf import PdfReader #librairie pour traiter les documents de type "pdf" #pip install pypdf #pypdf 3.17.1

class base_livre:
    def __init__(self,ressource):
        self.ressource = ressource
        
    def type(self): #j'ai changé ca comme tu as proposé
        if self.ressource.endswith(".pdf"):
            return PDF
        elif self.ressource.endswith(".epub"):
            return EPUB
        else:
            raise NotImplementedError("format non pris en charge!")

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

    def __init__(self, ressource):
        self.ressource = ressource
        if "://" in self.ressource:
            response = requests.get(self.ressource, verify=False)
            if response.status_code == 200:
                self.ressource = PdfReader(io.BytesIO(response.content))
            else:
                raise FileNotFoundError("ressource inaccessible")
        else:
            if not os.path.exists(self.ressource):
                raise FileNotFoundError(f"File '{self.ressource}' does not exist.")
            self.ressource = PdfReader(self.ressource)
    
    def type(self):
        return "PDF"

    def titre(self):
        return self.ressource.metadata.title

    def auteur(self):
        return self.ressource.metadata.author

    def langue(self):
        return NotImplementedError(None) 
    def sujet(self):
        return self.ressource.metadata.subject

    def date(self):
        return self.ressource.metadata.creation_date

class EPUB(base_livre):
    
    def __init__(self,ressource):
        self.ressource = ressource
        if "://" in self.ressource:
            response = requests.get(self.ressource,verify=False)
            # Raise an exception for bad responses and bad links
            if response.status_code == 200:
                self.ressource = epub.read_epub(io.BytesIO(response.content))
            else:
                raise FileNotFoundError("ressource inaccessible")

        # Check if the resource is a file path
        else:
            if not os.path.exists(self.ressource):
                raise FileNotFoundError(f"File '{self.ressource}' does not exist.")
            self.ressource = epub.read_epub(self.ressource)

    def type(self):
        return "EPUB"

    def titre(self):
        return self.ressource.get_metadata("DC","title")[0][0]

    def auteur(self):
        return self.ressource.get_metadata("DC","creator")[0][0]

    def langue(self):
        return self.ressource.get_metadata("DC","language")[0][0]
    
    def sujet(self):
        return NotImplementedError(None) #selon le documentation y a pas de metadata pour le sujet

    def date(self):
        return self.ressource.get_metadata("DC","date")[0][0]
