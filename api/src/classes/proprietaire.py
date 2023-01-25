#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser

class Proprietaire:

    def __init__(self):
        # Chemin de l'API
        #pathApi = os.path.dirname(os.path.realpath(__file__))

        # Récupération config
        # configApi = configparser.ConfigParser()
        # configApi.read(pathApi + '/../../conf/config.ini')
        # self._configApi = configApi

        self._bdSqlite = sqlite3.connect(pathApi + '/../data/dbInstallations.db')

    def liste(self):
        listeInstallation = list()

        # Renvoyer la liste des proprietaires
        
        #  conn = sqlite3.connect("database.db")
        #  c = conn.cursor()
        #  c.execute("SELECT * FROM proprietaires")
        #  rows = c.fetchall()
        #  conn.close()

        return(listeInstallation)

    def creer():

        # conn = sqlite3.connect("database.db")
        # c = conn.cursor()
        # c.execute("SELECT * FROM proprietaires WHERE id=?", (id,))
        # row = c.fetchone()
        # conn.close()
        return(retour)