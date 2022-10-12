# -* - coding: UTF-8 -* -
# !/usr/bin/python3

from typing import Optional, Awaitable

import pymysql
import tornado.web


class MysqlHandler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        sql = self.get_argument("sql", default="select 1")
        conn = pymysql.connect(host='10.110.62.41', user='root', passwd="Jya3QE7M0e", db='icp_native', port=30862)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

        print(result)
        count = 0
        html = ""
        for row in result:
            for item in row:
                html = html + str(item) + " | "
            html = html + "\n"
        self.write(html)

    def post(self):
        pass

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json;charset=utf-8')
