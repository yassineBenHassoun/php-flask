#!/usr/bin/python3
# -*-coding:UTF-8 -*

from flask import make_response, jsonify, request
import configparser
import os
import time
import json
import sys


from __main__ import app

from classes.installation import Installation

# Chemin de l'API
pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
# configApi = configparser.ConfigParser()
# configApi.read(pathApi + '/../../conf/config.ini')
@app.route('/installations', methods=['GET'])
def installationsGet(*args, **kwargs):

    installations = Installation()
    listeInstallations = installations.liste()
    response = make_response(json.dumps(listeInstallations), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/installations/parProprietaire/<id_propietaire>', methods=['GET'])
def installationsParProprietaireGet(id_propietaire):

    # Récupérer l'argument "proprietaire" sous forme d'id et renvoyer les installations correspondantes
    
    installations = Installation()
    listeInstallationsParProprietaire = installations.listeParProprietaire(id_propietaire)
    response = make_response(json.dumps(listeInstallationsParProprietaire), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"
    return response

@app.route('/installations', methods=['POST'])
def installationsPost():

#     # Récupérer les arguments nécessaires à la création d'une nouvelle installation
#     # Le propriétaire doit déjà exister

    installations = Installation()
    requestData = request.get_json()
    createInstall = installations.creer(requestData)
    
    response = make_response(json.dumps(createInstall), 200)
    response.headers["Content-Type"] = "text/json; charset=utf-8"


    return response
