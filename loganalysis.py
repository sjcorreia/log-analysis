#!/usr/bin/env python3
#
# FSND Prj 3: Log analysis


import psycopg2

DBNAME = "dbname=news"

db = psycopg2.connect(DBNAME)


def get_most_popular_articles():
    """Return the 3 most popular articles from the 'news' database"""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute("select * from articles")
    list_articles = cur.fetchall()
    return list_articles
    db.close()


def get_info_from_logs():
    """Return the 3 most popular articles from the 'news' database"""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute("select * from log")
    list_logs = cur.fetchone()
    return list_logs
    db.close()


if __name__ == '__main__':
    # article_list = get_most_popular_articles()
    # print(article_list)
    log_list = get_info_from_logs()
    print(log_list)
