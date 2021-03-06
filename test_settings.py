# -*- coding: utf-8 -*-
"""
    jaryee.web
    ~~~~~~~~~~~~~~~~~~~

    Jaryee system application

    :copyright: (c) Power by Daqing Chan.
    :license, see LICENSE for more details.
"""

from datetime import timedelta

DEBUG = True
HOST = '0.0.0.0'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.1.103:3316/restapi?charset=utf8mb4'
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_RECYCLE = 20
SECRET_KEY = 'super-secret fuck'
JWT_SECRET_KEY = 'JSON-Web-Token-Projected-Every!!'
JWT_AUTH_URL_RULE = '/api/auth_token'
JWT_EXPIRATION_DELTA = timedelta(seconds=7200)
JWT_LEEWAY = 60
JWT_DEFAULT_REALM = 'Login Required'