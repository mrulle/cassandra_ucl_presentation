import os, time
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


cassandra_username = os.getenv('CASSANDRA_USER', 'cassandra')
cassandra_password = os.getenv('CASSANDRA_PASSWORD', 'cassandra')

auth_provider = PlainTextAuthProvider(
    username=cassandra_username, password=cassandra_password)

# skide protocol_version skulle være v. 4
# se https://stackoverflow.com/questions/40611082/cassandra-unable-to-connect-to-any-servers-via-django-while-cqlsh-works

cluster = Cluster(['cassandra_1', 'cassandra_2', 'cassandra_3'], auth_provider=auth_provider, protocol_version=4)
session = cluster.connect()

version = session.execute("SELECT release_version FROM system.local").one()
print(f'connected to cassandra {version} :-)')

stmts = [
    "CREATE KEYSPACE IF NOT EXISTS store WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };",
    "CREATE TABLE IF NOT EXISTS store.shopping_cart (userid text PRIMARY KEY,item_count int,last_update_timestamp timestamp);",
    "CREATE TABLE IF NOT EXISTS store.shopping_cart (userid text PRIMARY KEY,item_count int,last_update_timestamp timestamp);",
    "INSERT INTO store.shopping_cart(userid, item_count, last_update_timestamp)VALUES ('9876', 2, toTimeStamp(now()));",
    "INSERT INTO store.shopping_cart(userid, item_count, last_update_timestamp)VALUES ('1234', 5, toTimeStamp(now()));"
]

for stmt in stmts:
  response = session.execute(stmt)
  print(response)

select_stmt = "select item_count,last_update_timestamp from store.shopping_cart where userid = '1234'"
response = session.execute(select_stmt)
print(f'response: {response[0]}')


print(f'db seeded')