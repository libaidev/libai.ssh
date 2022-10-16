# -* - coding: UTF-8 -* -
# !/usr/bin/python3

import tornado.web


class LibaiHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("libai.html")

    def post(self):
        pass
