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
        db = self.get_argument("db", default="10.110.62.41|root|Jya3QE7M0e|icp_native|30862")
        # host='10.110.62.41', user='root', passwd="Jya3QE7M0e", db='icp_native', port=30862
        # 10.110.62.41|root|Jya3QE7M0e|icp_native|30862
        db_arr = db.split("|")
        conn = pymysql.connect(host=db_arr[0], user=db_arr[1], passwd=db_arr[2], db=db_arr[3], port=int(db_arr[4]))
        self._exec_sql(conn, sql)

    def _exec_sql(self, conn, sql):
        # conn = self.mysql_conn["root@icp_native"]
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
