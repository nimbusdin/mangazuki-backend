import sqlite3
from sqlite3 import Error
import urllib.request as urllib
import xmltodict

FEED_URL = "https://mangazuki.co/feed"


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, data):
    sql = """ INSERT INTO series(author, title, link, summary, content, date, trending)
              VALUES(?,?,?,?,?,?,?)"""
    cur = conn.cursor()
    i = 0
    for entry in data:
        author = entry['author']['name']
        title = entry['title']['#text']
        link = entry['id']
        summary = None
        content = None
        try:
            summary = entry['summary']['#text']
        except:
            summary = None
        try:
            content = entry['content']['#text']
        except:
            summary = None
        updated = entry['updated']
        updated = updated[0:10] + " " + updated[11:19] + ".000"
        if i % 2 == 0:
            trending = "True"
        else:
            trending = None
        # print(updated)
        cur.execute(sql, (author, title, link, summary, content, updated, trending))
        conn.commit()
        i += 1

def feed_connect(feed):
    file = open('mangazuki.xml', 'r')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data

if __name__ == '__main__':
    data = feed_connect(FEED_URL)
    conn = create_connection(r"./mangazuki.db")

    series_table = """ CREATE TABLE IF NOT EXISTS series (
                            id integer PRIMARY KEY,
                            author text,
                            title text NOT NULL,
                            link text NOT NULL,
                            summary text,
                            content text,
                            date text NOT NULL,
                            trending text
    );"""

    news_table = """ CREATE TABLE IF NOT EXISTS news (
                            id integer PRIMARY KEY,
                            heading text NOT NULL,
                            subheading text,
                            body text,
                            author text,
                            date text NOT NULL
    );"""

    if conn is not None:
        create_table(conn, series_table)
        create_table(conn, news_table)
        conn.commit()
    else:
        print("Error! cannot cerate the database connection.")

    insert_data(conn, data['feed']['entry'])
