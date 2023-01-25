#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response, jsonify, request
import configparser
import os
import time
import json
import sys

from __main__ import app

from classes.proprietaire import Proprietaire
from classes.installation import Installation

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
#configApi = configparser.ConfigParser()
#configApi.read(pathApi + '/../../conf/config.ini')
@app.route('/proprietaires', methods=['GET'])
def proprietairesGet(*args, **kwargs):

    proprietaires = Proprietaire()
    listeProprietaires = proprietaires.liste()

    response = make_response(json.dumps(listeProprietaires), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response


@app.route('/proprietaires', methods=['POST'])
def proprietairesPost():

    #Récupérer les arguments nécessaires à la création d'une nouvelle installation
    # Le propriétaire doit déjà exister
    
    prop = Proprietaire()
    requestData = request.get_json()
    getPropietaire = prop.listeProprietaire(requestData['idProprietaire'])
    
    if getPropietaire :
        install = Installation()
        registerInstall = install.creer(requestData)
        response = make_response(json.dumps(registerInstall), 200)
        response.headers["Content-Type"] = "text/json; charset=utf-8"
        return response
        
    else:
        
        error = {'error' : 'proprietaire not found'}
        response = make_response(json.dumps(error), 200)
        response.headers["Content-Type"] = "text/json; charset=utf-8"
        return response
        