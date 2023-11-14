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

create_stmt = """
CREATE COLUMN FAMILY Posts
  WITH comparator = UTF8Type
  AND key_validation_class=UTF8Type
  AND default_validation_class = UTF8Type
  AND column_metadata = [
    {column_name: author, validation_class: UTF8Type},
    {column_name: title, validation_class: UTF8Type},
    {column_name: content, validation_class: UTF8Type},
    {column_name: date, validation_class: DateType}
  ];
  """

response = session.execute(create_stmt)
print(response)


yay = input('say nam nam')

print(f'did you say {yay}')