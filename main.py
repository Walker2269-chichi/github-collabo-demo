import sqlite3
CONN = sqlite3.connect("hello.db")
CURSOR = CONN.cursor()