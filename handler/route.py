#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
import index
import host
import user

urls = [
    (r'/',index.IndexHandler),
    (r'/login',index.LoginHandler),
    (r'/host',host.HostHandler),
    (r'/user',user.UserHandler),
]