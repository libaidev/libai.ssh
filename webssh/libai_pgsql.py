# -* - coding: UTF-8 -* -
# !/usr/bin/python3

from typing import Optional, Awaitable

import psycopg2
import tornado.web


class PgsqlHandler(tornado.web.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        sql = self.get_argument("sql", default="select 1")
        db = self.get_argument("db", default="10.110.62.41|root|Jya3QE7M0e|icp_native|30862")
        # 10.110.62.41|root|Jya3QE7M0e|icp_native|30862
        db_arr = db.split("|")
        conn = psycopg2.connect(host=db_arr[0], user=db_arr[1], passwd=db_arr[2], db=db_arr[3], port=int(db_arr[4]))
        self._exec_sql(conn, sql)

    def _exec_sql(self, conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

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
