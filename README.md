# log-analysis
Udacity Full Stack Nanodegree project 3

created view

create view popular as
	select articles.title, articles.author, authors.name, count(log.path) as num
	from articles left join log on log.path
	like concat('%',articles.slug,'%')
	join authors on articles.author = authors.id
	group by articles.title, articles.author, authors.name
	order by num desc;

https://stackoverflow.com/questions/8974328/mysql-multiple-joins-in-one-query

https://stackoverflow.com/questions/1386166/how-to-use-a-like-with-a-join-in-sql

postgreSQL date function https://www.postgresql.org/docs/9.0/static/functions-datetime.html

https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

https://stackoverflow.com/questions/10678229/how-can-i-selectively-escape-percent-in-python-strings

https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

## License

The contents of this repository are covered under the [MIT License](LICENSE).
