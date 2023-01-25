#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
import sqlite3
import sys

class Proprietaire:

    def __init__(self):
        # Chemin de l'API
        pathApi = os.path.dirname(os.path.realpath(__file__))
    
        #Récupération config
        configApi = configparser.ConfigParser()
        configApi.read(pathApi + '/../../conf/config.ini')

        self._configApi = configApi
        self._bdSqlite = sqlite3.connect(pathApi + '/../data/dbInstallations.db')

    def liste(self):
        listeInstallation = list()
        
        c = self._bdSqlite.cursor()
        c.execute("SELECT * FROM proprietaires")
        rows = c.fetchall()
        c.close()

        return(rows)
    
    def listeProprietaire(self, proprietaire_id):
            
        # Renvoyer la liste des installations d'un proprietaire en particulier
        
        rq = self._bdSqlite.cursor()
        rq.execute("SELECT * FROM proprietaires WHERE id=?", (proprietaire_id,))
        rows = rq.fetchall()
        rq.close()
    
        return(rows)

    def creer(self, requestData):

        try:
        
            rq = self._bdSqlite.cursor()
            rq.execute("INSERT INTO proprietaires (nom) VALUES (?)",(requestData["nom"]))
            self._bdSqlite.commit()
                    
            secondRq = self._bdSqlite.cursor()
            secondRq.execute("SELECT * FROM proprietaires WHERE  id = (SELECT MAX(id)  FROM proprietaires);")
            rows = secondRq.fetchall()
            secondRq.close()

            return(rows)
         
        except:
            self._bdSqlite.rollback()
            msg = "error in insert operation"
        finally:
            self._bdSqlite.close()
       