#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import random

__author__ = 'ReS4'

from ApiApp.handlers.base import WebBaseHandler, s


class UserProfileHandler(WebBaseHandler):
    def __init__(self, application, request, **kwargs):
        super(UserProfileHandler, self).__init__(application, request, **kwargs)
        self.users = []
        self.get_users()

    def get_users(self):
        try:
            with open(os.path.join(s.applications_root, "ApiApp", "users.json"), mode="r") as f:
                x = f.read()
                self.users = json.loads(x)
                f.close()

        except Exception as e:
            print(e)

    def save_users(self):
        try:
            with open(os.path.join(s.applications_root, "ApiApp", "users.json"), mode="w") as f:
                f.write(json.dumps(self.users))
                f.close()
                return True
        except Exception as e:
            return False

    def post(self, *args, **kwargs):
        user_id = self.get_argument("user_id", None)

        try:
            user_id = int(user_id)
        except:
            self.result['message'] = "Invalid userId."
            self.finish(self.result)
            return

        for i in self.users:
            if i['id'] == user_id or i['id'] == str(user_id):
                self.result['value'] = i
                self.result['status'] = True
                self.result['message'] = "Ok."

        if not self.result['value']:
            self.result['message'] = "User not found."

        self.finish(self.result)

    def put(self, *args, **kwargs):

        new_user = self.get_argument("user", None)

        try:
            new_user = json.loads(new_user)
        except:
            self.result['message'] = "Invalid JSON."
            self.finish(self.result)
            return

        try:
            if "id" in new_user.keys():
                try:
                    new_user['id'] = int(new_user['id'])
                except:
                    pass

                for i in self.users:
                    if new_user['id'] == i['id']:
                        self.result['message'] = "UserID exist."
                        self.finish(self.result)
                        return
            else:
                self.result['message'] = "There is no ID key in json."
                self.finish(self.result)
                return
        except:
            self.result['message'] = "Invalid JSON."
            self.finish(self.result)
            return

        self.users.append(new_user)
        if self.save_users():
            self.result['status'] = True
            self.result['message'] = "User saved."
            self.result['value'] = new_user['id']
        else:
            self.result['message'] = "Cannot Save user. check input value."

        self.finish(self.result)


class UploadHandler(WebBaseHandler):
    def __init__(self, application, request, **kwargs):
        super(UploadHandler, self).__init__(application, request, **kwargs)
        self.save_path = os.path.join(s.applications_root, "static")
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def post(self, *args, **kwargs):
        try:
            _file = self.request.files['file'][0]
            extension = os.path.splitext(_file['filename'])[-1].lower()

            photo_name = "{}{}".format(random.randint(1155551918949, 91555519189459), extension)
            full_name = os.path.join(self.save_path, photo_name)
            with open(full_name, 'wb') as output:
                output.write(_file['body'])
                output.close()

            self.result['message'] = "Upload Successful."
            self.result['value'] = photo_name
        except:
            self.result['message'] = "Invalid file."

        self.finish(self.result)
