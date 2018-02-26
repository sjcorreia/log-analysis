#!/usr/bin/env python3
#
# Author: Steven Correia
# github: sjcorreia
# FSND Prj 3: Log analysis


import psycopg2

DBNAME = "dbname=news"

# The following query uses the view 'popular' in the 'news' database.
# Please refer to the README.md for instructions on creating this view.
SQL_THREE_POPULAR_ARTICLES = "select title, num from popular limit 3;"

# The following query uses the view 'popular' in the 'news' database.
# Please refer to the README.md for instructions on creating this view.
SQL_POPULAR_AUTHORS = "select name, sum(num) from popular group by name \
    order by sum desc;"

SQL_ERRORS_EACH_DAY = "select date, per_err from \
    (select date, ((cast(errors as float)/total) * 100) as per_err from \
    (select date(log.time), count(log.status) as total, \
    err_result.errors from \
    log join (select date(time), count(status) as errors from log \
    where status not like '%OK%' group by date(time)) as err_result \
    on date(log.time) = date(err_result.date) \
    group by date(log.time), err_result.errors) as error_table) as final \
    where per_err > 1;"

db = psycopg2.connect(DBNAME)


def query_database(sql_query):
    """Return the resulting table for input sql query.
    Args:
        sql_query (str): A correct SQL query.

    Returns:
        list: A list with the results of the SQL query.
    """
    db = psycopg2.connect(DBNAME)
    cur = db.cursor()
    cur.execute(sql_query)
    list_results = cur.fetchall()
    db.close()
    return list_results


if __name__ == '__main__':
    article_list = query_database(SQL_THREE_POPULAR_ARTICLES)
    print("The three most popular articles of all time:")
    for article in article_list:
        print("\t\"%s\" - %d views" % (article[0], article[1]))

    authors_list = query_database(SQL_POPULAR_AUTHORS)
    print("\nThe most popular authors of all time:")
    for author in authors_list:
        print("\t%s - %d views" % (author[0], author[1]))

    errors_list = query_database(SQL_ERRORS_EACH_DAY)
    print("\nRequests led to errors greater than 1% on the following days:")
    for error in errors_list:
        print('\t{0:%B %d, %Y} - {1:.1f}% errors'
              .format(error[0], error[1]))
