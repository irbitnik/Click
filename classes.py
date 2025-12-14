import sqlite3 as sq
import requests as req
import settings as st


class Items:

    def __init__(self, url: str) -> None:
        self.price = self.get_price(url)

    @classmethod
    def get_price(cls, url: str) -> int:
        html = req.get(url, headers=st.headers).json()
        return html['listings'][0]['price']

    @staticmethod
    def get():
        with sq.connect('db.db') as con:
            cur = con.cursor()
            res = cur.execute('SELECT * FROM price').fetchall()
        return res

