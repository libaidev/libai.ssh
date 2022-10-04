import pymysql

from typing import Optional, Awaitable
from tornado.escape import json_decode
import tornado.web
import os


class MysqlHandler(tornado.web.RequestHandler):
    doc_home = "d:/opslog"

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        sql = self.get_argument("sql")
        conn = pymysql.connect(host='10.110.62.41', user='root', passwd="Jya3QE7M0e", db='icp_native', port=30862)
        cur = conn.cursor()
        cur.execute("SELECT * FROM product_type")
        for r in cur:
            print(r)
        cur.close()
        conn.close()

    def post(self):
        data = json_decode(self.request.body)
        self.get_arguments("file_path")
        file_path = os.path.join(self.doc_home, data['file_name'])
        with open(file_path, mode='w+', encoding='UTF-8') as f:
            f.write(data['file_data'])
        self.write("save ok")

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json;charset=utf-8')
