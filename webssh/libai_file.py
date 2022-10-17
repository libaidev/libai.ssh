# -* - coding: UTF-8 -* -
# !/usr/bin/python3

from typing import Optional, Awaitable
from tornado.escape import json_decode
import tornado.web
import os


class FileHandler(tornado.web.RequestHandler):
    doc_home = "d:/opslog"

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def file_filter(self, f):
        if f[-4:] in ['.txt', '.log', '.md']:
            return True
        else:
            return False

    def get(self):
        file_name = self.get_argument("filename", default="ls")
        file_path = self.doc_home
        if os.path.exists(file_name):
            (file_path, file_name) = os.path.split(file_name)

        if file_name == "ls":
            files = os.listdir(self.doc_home)
            files = list(filter(self.file_filter, files))
            with open(os.path.join(self.doc_home, "filelist.log"), "r", encoding="utf-8", errors="ignore") as f:
                files.extend(f.readlines())
            self.write("\n".join(files))
        else:
            self.set_header("file_name", file_name)
            self.set_header("file_path", file_path)
            with open(os.path.join(file_path, file_name), "r", encoding="utf-8", errors="ignore") as f:
                file_data = f.read()
            self.write(file_data)

    def post(self):
        data = json_decode(self.request.body)
        file_name = data['file_name']
        file_path = data['file_path']
        with open(os.path.join(file_path, file_name), mode='w+', encoding='UTF-8') as f:
            f.write(data['file_data'])
        self.write("save ok")

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json;charset=utf-8')
