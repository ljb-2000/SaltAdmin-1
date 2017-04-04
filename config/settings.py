#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio

config = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'saltadmin2',
        'user': 'test',
        'pass': 'test',
        'charset': 'utf8'
    },
    'redis': {
        'host': '127.0.0.1',
        'port': 6503,
        'password': '',
        'db': '0'
    }
}

settings = dict(
    template_path = 'view',
    static_path = 'static',
    static_url_prefix = '/static/',
    xsrf_cookies = False,
    cookie_secret = "db884468559f4c432bf1c1775f3dc9da",
    ksid_name = '_ksid',
    session_key = "_k_session_",
    session_expires = 300,
    login_url = "/user/login",
    debug = True,
    autoreload = True
)