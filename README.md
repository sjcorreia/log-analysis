# Log Analysis Project

The Log Analysis project is part of the Udacity Full Stack Nanodegree program. The goal of this project is to answer the following questions using queries to a PostgreSQL database. The questions being answered in this project are:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Throughout the course of this Nanodegree program, a [vagrant](https://www.vagrantup.com/) virtual machine is required on the host system. This virtual machine is a Linux based VM that provides a PostgreSQL database and support software needed to complete this project. The following [instructions](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) will guide you through installing the vagrant VM on to your machine. 

Once the vagrant VM is installed, the user will need to use the command `vagrant up` to start the VM.
Then the user can log into the VM using the `vagrant ssh` command.

Udacity provided the file `newsdata.sql` in a zipped format at the start of the project. 
This file will be copied to the `vagrant` directory.

We need to change to the `vagrant` directory and run the command `psql -d news -f newsdata.sql` to load the data.

## Source Code and Setup

The source code for this project can be found on my [github](https://github.com/sjcorreia/log-analysis) page.

This project encouraged us to use our new knowledge of SQL and possibly create a view to assist with the queries.

The view `popular` was created and used in the `loganalysis.py` file to help answer the first two questions, as they contained related information.

Once the user has connected to the VM and loaded the `newsdata` into a SQL database, she/he will need to connect to the database using the command `psql -d news` and run the following command:

```sql
create view popular as
	select articles.title, articles.author, authors.name, count(log.path) as num
	from articles left join log on log.path
	like concat('%',articles.slug,'%')
	join authors on articles.author = authors.id
	group by articles.title, articles.author, authors.name
	order by num desc;
```

## Running the code

The user will need to download and install [Python](https://www.python.org/downloads/), if it is not already installed.

This project was implemented usign Python 3 and I recommend using Python 3 for all future projects.

Executing the code is as simple as typing the command

	python3 loganalysis.py

into the terminal.

## Resources and References

The following links were helpful in creating the SQL queries and properly outputting the information using Python.

* [SQl Multiple Joins](https://stackoverflow.com/questions/8974328/mysql-multiple-joins-in-one-query) question on Stack Overflow.
* Using [`LIKE` in a join](https://stackoverflow.com/questions/1386166/how-to-use-a-like-with-a-join-in-sql) question on Stack Overflow.
* The PostgreSQL [date function](https://www.postgresql.org/docs/9.0/static/functions-datetime.html).
* Formatting for the [datetime](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior) object in Python.
* Properly displaying the [% symbol](https://stackoverflow.com/questions/10678229/how-can-i-selectively-escape-percent-in-python-strings) in a Python string, from Stack Overflow.
* Limiting the number of digits after the decimal point in a Python [float](https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points), from Stack Overflow.

## Python Code Quality

The source code was run through the command-line tool `pep8` to check that the code conforms to the [PEP8](https://www.python.org/dev/peps/pep-0008/) standards. The `pep8` tool recommened to install and use `pycodestyle` tool due to GitHub Issue #466. The source code was also checked using this tool, which did not report any errors.

This tool is run on the command line of the terminal as follows:

	pycodestyle loganalysis.py


## License

The contents of this repository are covered under the [MIT License](LICENSE).
