#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = '1.0.0'
__license__ = 'MIT'
__author__ = 'Josh Welchez'
__email__ = 'jshwelz09@gmail.com'

import routes
from flask import Flask
from flask_cors import CORS
from globals import db, config

application = Flask(__name__)
CORS(application, resources={r"*": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'
db.connect()
application.config['SECRET_KEY'] = config.SECRET



@application.route('/')
def main_route():
    return 'Words Analysis and Grouping Engine'


routes.initialize_routes(application)


if __name__ == '__main__':
    # application.run(ssl_context='adhoc')
    application.run()
