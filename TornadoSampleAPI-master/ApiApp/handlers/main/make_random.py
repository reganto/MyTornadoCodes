#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = 'ReS4'

from ApiApp.handlers.base import WebBaseHandler


class MakeRandomCodeHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        int_size = self.get_argument("size", None)
        try:
            int_size = int(int_size)
        except:
            self.result['message'] = "Invalid INT size."
            self.finish(self.result)
            return

        if int_size:
            if 0 < int_size < 20:
                self.result['value'] = str(
                    random.randint(10000000000000000000000000, 99999999999999999999999999))[0:int_size]
                self.result['message'] = "Ok."
                self.result['status'] = True

            else:
                self.result['message'] = "0 < size < 20"
        else:
            self.result['message'] = "Invalid size."

        self.finish(self.result)

    def post(self, *args, **kwargs):
        start = self.get_argument("start", None)
        end = self.get_argument("end", None)

        if start and end:
            try:
                start = int(start)
                end = int(end)
            except:
                self.result['message'] = "Invalid Integers."
                self.finish(self.result)
                return

            if start < end:
                r = random.randint(start, end)
            else:
                self.result['message'] = "Start is bigger than End."
                self.finish(self.result)
                return
        else:
            r = random.randint(0, 9999999999999999999999)

        self.result['status'] = True
        self.result['value'] = r
        self.result['message'] = "Ok."
        self.finish(self.result)
