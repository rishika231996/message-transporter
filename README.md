Assignment Problem: Building a message transporter and Simple Api capability
Problem Statement:
Three small apps to be built
1. First app to take the file with crawled data and transport to the second app. Any
transporting mechanism be used such as RabbitMQ etc.
2. Second app to consume the transported data and persist in a storage layer on a
individual product level and perform aggregated calculations such as Score
3. Third app is to expose an API which can be used to either get the score for an
account or individual products by the account. Authentication layer can be
ignored.

App 1
Producer:
● Write a producer which reads data from file which has json data and send
the data to RabbitMQ or any of messaging queue

App 2
Consumer:
● Write the consumer which reads data from messaging queue and sanitize
data and write to DB (Postgres/Mysql)
Database Design:

● Design a database schema, which should have all the relevant fields
required for score computation.
● Use an appropriate database (e.g., SQLite) and provide the SQL script to
create the necessary tables.
Object-Oriented Programming:
● Follow OOP best practices while defining classes and functions.

App 3
Web API:
● Use a Python web framework (e.g., Flask, Django, FastApi) to create a
RESTful API for the score computation.
● Include endpoints to retrieve all the data from the table and score api

Above mentioned is the problem statement,  All the different apps are created and the rest api endpoints are:
1 - http://127.0.0.1:8000/products/
2 - http://127.0.0.1:8000/score/

The RabbitMQ server is created and postgres db is created with all the mentioned columns.
