#!/usr/bin/env python3
#
# FSND Prj 3: Log analysis


import psycopg2

DBNAME = "dbname=news"

SQL_THREE_POPULAR_ARTICLES = "select title, num from popular limit 3;"

SQL_POPULAR_AUTHORS = "select name, sum(num) from popular group by name \
    order by sum desc;"

db = psycopg2.connect(DBNAME)


def get_three_most_popular_articles():
    """Return the 3 most popular articles from the 'news' database
    This function uses the view 'popular', please see the README file
    for instructions on creating this view in the 'news database'."""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute(SQL_THREE_POPULAR_ARTICLES)
    list_articles = cur.fetchall()
    return list_articles
    db.close()


def get_most_popular_authors():
    """Return interesting info for one entry from the 'log' table
    This function uses the view 'popular', please see the README file
    for instructions on creating this view in the 'news database'."""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute(SQL_POPULAR_AUTHORS)
    list_authors = cur.fetchall()
    return list_authors
    db.close()


if __name__ == '__main__':
    article_list = get_three_most_popular_articles()
    print("The three most popular articles of all time:")
    for article in article_list:
        print("\t%s - %d views" % (article[0], article[1]))

    authors_list = get_most_popular_authors()
    print(authors_list)
