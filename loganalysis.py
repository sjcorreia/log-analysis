#!/usr/bin/env python3
#
# Author: Steven Correia
# github: sjcorreia
# FSND Prj 3: Log analysis


import psycopg2

DBNAME = "dbname=news"

SQL_THREE_POPULAR_ARTICLES = "select title, num from popular limit 3;"

SQL_POPULAR_AUTHORS = "select name, sum(num) from popular group by name \
    order by sum desc;"

SQL_ERRORS_EACH_DAY = "select date(log.time), count(log.status) as total, \
    err_result.errors from \
    log join (select date(time), count(status) as errors from log \
    where status not like '%OK%' group by date(time)) as err_result \
    on date(log.time) = date(err_result.date) \
    group by date(log.time), err_result.errors;"

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
    """Return the most popular authors from the 'news' database
    This function uses the view 'popular', please see the README file
    for instructions on creating this view in the 'news database'."""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute(SQL_POPULAR_AUTHORS)
    list_authors = cur.fetchall()
    return list_authors
    db.close()


def get_errors_each_date():
    """Return the total queries, errors for each date in the 'log' table."""
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute(SQL_ERRORS_EACH_DAY)
    list_dates_errors = cur.fetchall()
    return list_dates_errors
    db.close()


if __name__ == '__main__':
    article_list = get_three_most_popular_articles()
    print("The three most popular articles of all time:")
    for article in article_list:
        print("\t\"%s\" - %d views" % (article[0], article[1]))

    authors_list = get_most_popular_authors()
    print("\nThe most popular authors of all time:")
    for author in authors_list:
        print("\t%s - %d views" % (author[0], author[1]))

    errors_list = get_errors_each_date()
    print("\nRequests led to errors greater than 1% on the following days:")
    for error in errors_list:
        percent_error = (error[2] / error[1]) * 100
        if percent_error > 1:
            print("\t%s - %.1f%% errors" % (error[0].strftime("%B %d, %Y"),
                  percent_error))
