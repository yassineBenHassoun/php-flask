#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
import sqlite3
import sys


class Installation:

    def __init__(self):
        # Chemin de l'API
        pathApi = os.path.dirname(os.path.realpath(__file__))
    
        #Récupération config
        configApi = configparser.ConfigParser()
        configApi.read(pathApi + '/../../conf/config.ini')

        self._configApi = configApi
        self._bdSqlite = sqlite3.connect(pathApi + '/../data/dbInstallations.db')

    def liste(self):
        #listeInstallation = list()
        
        rq = self._bdSqlite.cursor()
        rq.execute("SELECT installations.nom, installations.commune, installations.capacite, proprietaires.nom FROM installations, proprietaires WHERE installations.idProprietaire = proprietaires.id ORDER BY installations.commune, installations.capacite")
        rows = rq.fetchall()
        rq.close()
           
        # Renvoyer la liste des installations et de leurs propriétaires triée par commune puis par capacité

        return(rows)

    def listeParProprietaire(self, id_proprietaire):
        
        # Renvoyer la liste des installations d'un proprietaire en particulier
        
        rq = self._bdSqlite.cursor()
        rq.execute("SELECT * FROM installations WHERE idProprietaire=?", (id_proprietaire,))
        rows = rq.fetchall()
        rq.close()
    
        return(rows)
    

    def creer(self,requestData):

        insertInstallation = list()
        pathApi = os.path.dirname(os.path.realpath(__file__))
        try:
        
            rq = self._bdSqlite.cursor()
            rq.execute("INSERT INTO installations (nom, commune, capacite, anneeInstallation, idProprietaire) VALUES (?,?,?,?,?)",
             (requestData["nom"], requestData["commune"], requestData["capacite"], requestData["anneeInstallation"], requestData["idProprietaire"]))
            self._bdSqlite.commit()
                    
            secondRq = self._bdSqlite.cursor()
            secondRq.execute("SELECT * FROM installations WHERE  id = (SELECT MAX(id)  FROM installations);")
            rows = secondRq.fetchall()
            secondRq.close()

            return(rows)
         
        except:
            self._bdSqlite.rollback()
            msg = "error in insert operation"
        finally:
            self._bdSqlite.close()
       
    
        