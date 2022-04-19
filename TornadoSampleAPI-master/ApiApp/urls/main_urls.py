#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ApiApp.handlers.main import make_random, profile

__author__ = 'ReS4'

url_patterns = [
    ("/random", make_random.MakeRandomCodeHandler, None, "random"),
    ("/profile", profile.UserProfileHandler, None, "profile"),
    ("/upload", profile.UploadHandler, None, "upload"),

]
