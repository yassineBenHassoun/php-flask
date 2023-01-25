#!/usr/bin/python3
# -*-coding:UTF-8 -*

import os
import configparser
from flask import Flask, request, render_template

# Chemin de l'API
#pathApi = os.path.dirname(os.path.realpath(__file__))

# Récupération config
#configApi = configparser.ConfigParser()
#configApi.read(pathApi + '/../conf/config.ini')

# Création API
app = Flask(__name__)

import routes.version
import routes.installations

# Exécution et lancement du serveur
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')



