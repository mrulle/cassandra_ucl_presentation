from cassandra.cluster import Cluster
import time


cluster = Cluster(['cassandra_1', 'cassandra_2', 'cassandra_3'])
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